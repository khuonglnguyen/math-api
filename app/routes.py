from app import app
from flask import request, jsonify

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