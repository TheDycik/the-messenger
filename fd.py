from flask import Flask
from flask import request
from flask import abort
import datetime
import time

app = Flask(__name__)
messages = [
    {'name': 'dyde', 'time': time.time(), 'text': 'salam'},
    {'name': 'kozel', 'time': time.time(), 'text': 'waleikum'}
]
users = {
    'chyvak': '23123'
}


@app.route("/")
def hello_view():
    return "<h1>Welcome to the homepage! <a href='/status'> status </a> <a href='/messages> messages </a></h1>"


@app.route("/status")
def status_view():
    return {
        'status': True,
        'usercount': len(users),
        'messagescount': len(messages),
        'name': 'DycChat',
        'time': datetime.datetime.now()
    }


@app.route("/send", methods=['POST'])
def send_view():
    name = request.json.get('name')
    password = request.json.get('password')
    text = request.json.get('text')

    for token in [name, password, text]:
        if not isinstance(token, str) or 0 == len(token) or len(token) > 1024:
            abort(400)

    if name in users:
        # auth
        if users[name] != password:
            abort(401)
    else:
        # sign up
        users[name] = password

    messages.append({'name': name, 'text': text, 'time': time.time()})
    if text == 'time':
        messages.append({'name': 'Ботяра', 'text': f'Current time is {datetime.datetime.now()}', 'time': time.time()})
    elif text == 'joke':
        messages.append({'name': 'Ботяра', 'text': 'Шел медведь по лесу, видит машина горит. Сел медведь в машину и сгорел!', 'time': time.time()})
    elif text == 'help':
        messages.append({'name': 'Ботяра', 'text': 'Hello, friend! My commands are:\n help(for help lol),\n time(Ull know the current time),\n joke(funny joke about bear:( ),\n', 'time': time.time()})

    return {'ok': True}


def filter_dicts(elements, key, min_value):
    new_elements = []
    for element in elements:
        if element[key] > min_value:
            new_elements.append(element)
    return new_elements


@app.route("/messages")
def messages_view():

    try:
        after = float(request.args['after'])
    except:
        abort(400)

    filtered_messages = filter_dicts(messages, key='time', min_value=after)
    return {'messages': filtered_messages}


app.run()
