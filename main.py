from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def route():
    param = {'title': 'Марс'}
    return render_template('base.html', **param)


@app.route('/index/<name>')
def index(name):
    param = {'title': name}
    return render_template('base.html', **param)


@app.route('/training/<prof>')
def training(prof):
    param = {'title': 'Тренировка', 'profession': prof}
    return render_template('training.html', **param)


@app.route('/list_prof/<list_type>')
def list_prof(list_type):
    param = {'title': 'Список профессий', 'type': list_type}
    return render_template('professions.html', **param)


if __name__ == '__main__':
    app.run()
