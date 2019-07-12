from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	tasks = []
	with open('tasks.txt', 'r') as file:
		for line in file:
			tasks.append(line.replace('\n', ''))
	#tasks = ['доделать программу отчётности','эколог(компоненты Wi)','vk bot(начать)']
	return jsonify(tasks)

@app.route('/changetask', methods=['GET','POST'])
def change_tasks():
	tasks = []
	with open('tasks.txt', 'r') as file:
		i = 0
		for line in file:
			tasks.append({'number':str(i), 'text':line.replace('\n', '')})
			i+=1
	if request.method == 'POST':
		if request.form.get('add') != None:
			text = request.form['task']
			tasks.append({'number': i, 'text': text})
		else:
			delete_task = list(dict(request.form).keys())[0]
			del tasks[int(delete_task)]
			print(tasks)

		with open('tasks.txt', 'w') as file:
			for task in tasks:
				file.write(task['text'])
				file.write('\n')
	else:
		print(tasks)
	return render_template('index.html', tasks=tasks)
if __name__ == '__main__':
	app.run(debug=True)
