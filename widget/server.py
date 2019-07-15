from flask import Flask, jsonify, render_template, request, redirect, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import hashlib

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/Widget"
app.secret_key = 'ODM4YmE0NjQ3OWNiNDc2M2U0ZDYz'
mongo = PyMongo(app)


@app.route('/')
def index():
	if 'username' in session:
		tasks = mongo.db.users.find_one({'username':session['username']})
		data = []
		for task in tasks['tasks']:
			data.append(mongo.db.tasks.find({'_id': ObjectId(task)}))
		return jsonify(data)
	return redirect(url_for('login'))


@app.route('/changetask', methods=['GET', 'POST'])
def change_tasks():
	if 'username' in session:
		data = mongo.db.users.find_one({'username':session['username']})
		tasks = []
		for task in data['tasks']:
			tasks.append(mongo.db.tasks.find_one({'_id': ObjectId(task)}))
		print(tasks)

		if request.method == 'POST':
			if request.form.get('add') is not None:
				task = request.form['task']
				mongo.db.tasks.insert_one({'task': task})
				data = mongo.db.users.find_one({'username':session['username']})['tasks']
				data.append(ObjectId(mongo.db.tasks.find_one({'task': task})['_id']))
				mongo.db.users.update({'username':session['username']}, {'$set': {'tasks': data}})
				return redirect(url_for('change_tasks'))
			else:
				delete_task = list(dict(request.form).keys())[0]
				data = [task['tasks']for task in mongo.db.users.find({'username':session['username']})]
				data.remove([ObjectId(delete_task)])
				mongo.db.users.update({'username':session['username']}, {'$set': {'tasks': data}})
				mongo.db.tasks.remove({'_id': ObjectId(delete_task)})
				return redirect(url_for('change_tasks'))

		return render_template('index.html', tasks=tasks)


@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		user = request.form['username']
		password = hashlib.md5(request.form['password'].encode('utf-8')).hexdigest()
		if mongo.db.users.find_one({'username':user}):
			if mongo.db.users.find_one({'password': password}):
				session['username'] = user
				return redirect(url_for('index'))
	return render_template('login.html')


@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect(url_for('index'))


if __name__ == '__main__':
	app.run(debug=True)
