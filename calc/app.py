from flask import Flask, request
import operations

app = Flask(__name__)

OPERATIONS = {
    "add": operations.add,
    "sub":operations.sub,
    "mult":operations.mult,
    "div":operations.div,
}

@app.route('/')
def home():
    return "Calculator App with Flask"

@app.route('/add')
def op_add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = str(operations.add(a,b))
    return result

@app.route('/sub')
def op_sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = str(operations.sub(a,b))
    return result

@app.route('/mult')
def op_mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = str(operations.mult(a,b))
    return result

@app.route('/div')
def op_div():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = str(operations.div(a,b))
    return result
    

@app.route('/math/<operation>')
def result(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    if operation not in OPERATIONS:
        return f"Invalid operation: {operation}, use add, sub, mult or div"
    result = str(OPERATIONS[operation](a,b))
    
    return result


