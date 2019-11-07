from flask import Flask, redirect, render_template, request

app = Flask(__name__)
comments=[{'text': 'hello', 'author':'Ivan', 'img':'/static/img/cards/default.jpg'}]
@app.route('/')
def hello():
    return render_template('index.html', title='Home', cards=[{'id': 0, 'name': 'Microbot', 'address': 'http://192.168.1.66:30243', 'img': '/static/img/cards/default.jpg'},
                                                              {'id': 1, 'name': 'bWAPP', 'address': 'http://192.168.1.66:31946', 'img': '/static/img/cards/bWAPP.jpg'},
                                                              {'id': 2, 'name': 'DVWA', 'address': 'http://192.168.1.66:32189', 'img': '/static/img/cards/dvwa.jpg'},
                                                              {'id': 0, 'name': 'Microbot', 'address': 'http://192.168.1.66:30243', 'img': '/static/img/cards/default.jpg'},
                                                              {'id': 1, 'name': 'bWAPP', 'address': 'http://192.168.1.66:31946', 'img': '/static/img/cards/bWAPP.jpg'},
                                                              {'id': 2, 'name': 'DVWA', 'address': 'http://192.168.1.66:32189', 'img': '/static/img/cards/dvwa.jpg'},
                                                              {'id': 0, 'name': 'Microbot', 'address': 'http://192.168.1.66:30243', 'img': '/static/img/cards/default.jpg'},
                                                              {'id': 1, 'name': 'bWAPP', 'address': 'http://192.168.1.66:31946', 'img': '/static/img/cards/bWAPP.jpg'},
                                                              {'id': 2, 'name': 'DVWA', 'address': 'http://192.168.1.66:32189', 'img': '/static/img/cards/dvwa.jpg'}])

@app.route('/project/<int:id>', methods=['GET', 'POST'])
def project_info(id):

    if request.method == 'POST':
        comments.append({'text': request.form.get('text'), 'author':'Ivan', 'img':'/static/img/cards/default.jpg'})
        print(request.form.get('text'))


    return render_template('info.html', comments=comments)


@app.route('/infosec/docs')
def infosec_docs():
    return render_template('infosec_docs.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
