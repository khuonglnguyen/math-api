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
    
@app.route('/div', methods=['GET'])
def div():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)

    if a is not None and b is not None:
        result = a / b
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'Invalid input'}), 400