from app import app
from flask import request, jsonify
import math

@app.route('/add', methods=['GET'])
def add():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)

    if a is not None and b is not None:
        result = a + b
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'Invalid input'}), 400
    
@app.route('/sub', methods=['GET'])
def sub():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)

    if a is not None and b is not None:
        result = a - b
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'Invalid input'}), 400

@app.route('/mul', methods=['GET'])
def mul():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)

    if a is not None and b is not None:
        result = a * b
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'Invalid input'}), 400
    
@app.route('/div', methods=['GET'])
def div():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)

    if a is not None and b is not None:
        result = a / b
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'Invalid input'}), 400

@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    if username == 'admin' and password == 'admin':
        result = True
        return jsonify({'result': result})
    if username == 'admin' or password == 'admin':
        result = False
        return jsonify({'resule': result}), 401
    else:
        result = False
        return jsonify({'error': result}), 400
    
@app.route('/ptb2', methods=['GET'])
def ptb2():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    c = request.args.get('c', type=int)

    delta = b*b - (4 * a * c)
    
    if a == 0 and b == 0:
        return jsonify({'message': 'Pt vô số nghiệm'})
    if a == 0 and b != 0:
        return jsonify({'message': f'x = {-c/b}'}), 401
    if a != 0:
        if delta < 0:
            return jsonify({'message': 'Pt vô nghiệm'})
        if delta == 0:
            return jsonify({'messgae': f'PT có nghiệm kép: x1 = x2 = {-b/2*a}'})
        if delta > 0:
            x1 =(-b+math.sqrt(delta))/2*a
            x2 = (-b-math.sqrt(delta))/2*a
            return jsonify({'messgae': f'PT có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}'})