import random
from bottle import route, run, template


@route('/')
def home():
    return "Your lucky number is {}.".format(random.randint(1, 10))


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


run(host='localhost', port=8080)