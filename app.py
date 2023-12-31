from flask import Flask, request, jsonify
from flask_parameter_validation import Query
import math
import datetime
import json

app = Flask(__name__)

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
        


@app.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'Test'}), 200

@app.route('/hello-world', methods=['GET'])
def helloWorld():
    return jsonify({'message': 'Hello-world'}), 200

@app.route('/sosanhso',methods=['GET'])
def sosanhso():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    if a == b:
        return jsonify({'result': 'Same'})
    if a != b:
        return jsonify({ 'result': 'Not implement'})
    
@app.route('/year-now',methods=['GET'])
def yearNow():
    Year_now = datetime.datetime.now().year
    year_Now = request.args.get('year_Now', type=int)

    if year_Now is not None:
        year_Now = Year_now
    return jsonify({'result': f'{Year_now}'})

@app.route('/sqrt', methods=['GET'])
def sqrt(number: float = Query(True)):
        
        number = request.args.get('number', type=float)

        if number < 0:
            return jsonify({'error': 'Invalid input: Please provide a non-negative number'}), 400
        else:
            number_sqrt = math.sqrt(number)
            return jsonify({'result': f'{number_sqrt}'}), 200

@app.route('/giaithua', methods=['GET'])
def giaithua():
        
        number = request.args.get('number', type=int)
        giaithua = 1
        for i in range(1, number + 1):
            giaithua *= i
        return jsonify({'result': giaithua})

@app.route('/sort-desc', methods=['GET'])
def array1():
        array = request.args.get('array')
        array_desc = sorted(json.loads(array))
        return jsonify({'result': array_desc})

@app.route('/sort-asc', methods=['GET'])
def array2():
        array = request.args.get('array')
        array_asc = sorted(json.loads(array), reverse=True)
        return jsonify({'result': array_asc})

@app.route('/currency', methods=['GET'])
def currency():
    From = request.args.get('from', type=str)
    to = request.args.get('to', type=str)
    value = request.args.get('value', type=float)
    ti_le_VND = 23000
    if From == 'VND' and to == 'USD':
        result_VND_to_USD = round(value / ti_le_VND,1)
        return jsonify({'result': f'{result_VND_to_USD}'}), 200
    elif From == 'USD' and to == 'VND':
        result_USD_to_VND = value * ti_le_VND
        return jsonify({'result': f'{result_USD_to_VND}'}), 200
    else:
        return jsonify({'error': 'Invalid currency conversion'}), 400

@app.route('/count-number', methods=['GET'])
def count_number():
    number = request.args.get('number', type=str)
    if not number.isnumeric():
        return jsonify({'error': 'Invalid number'}), 400
    else:
        result = len(number) 
        return jsonify({'result': f'{result}'}), 200

if __name__ == "__main__":
    app.run(debug=True)