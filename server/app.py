#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:string>')
def print_string(string):
    print(f'{string}')
    return f'{string}'

@app.route('/count/<int:count>')
def count(count):
    result = ''
    for i in range(0, count):
        result += f'{i}\n'
    return result

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        add = num1 + num2
        return f"{add}"
    elif operation == '-':
        subtract = num1 - num2
        return f"{subtract}"
    elif operation == '*':
        multiply = num1 * num2
        return f"{multiply}"
    elif operation == 'div':
        divide = num1 / num2
        return f"{divide}"
    elif operation == '%':
        remainder = num1 % num2
        return f"{remainder}"
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)
