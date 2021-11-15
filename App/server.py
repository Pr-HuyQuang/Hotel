import json

import flask
from flask import Flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin
from request.traffic import User

import query as queRy

# Nếu lỗi thư viện thì run in terminal: pip install -r setup.txt
# Khai bao cong cua server
my_port = '8000'
scale = 0.00392
conf_threshold = 0.5
nms_threshold = 0.4

# Doan ma khoi tao server
app = Flask(__name__)
CORS(app)

# Khai bao ham xu ly request index
@app.route('/')
@cross_origin()
def index():
    return "Welcome to flask API!"

# Khai bao ham xu ly request hello_word
@app.route('/getGV', methods=['GET'])
@cross_origin()
def login():
    # Lay staff id, pass cua client gui len
    staff_id = request.args.get('staff_id')
    staff_pass = request.args.get('staff_pass')
    a = queRy.getGV(staff_id,staff_pass)
    js= json.dumps(a)
    return js

# Khai bao ham xu ly request detect
@app.route('/login', methods=['POST'])
@cross_origin()
def detect():
    try:
        username=request.form["username"]
        password=request.form["password"]
        a = queRy.Login(username,password)
        if(a==1):
            return 1
        else:
            return 0
        # data = request.get_json()
        # image_b64 = request.form.get('image')

    except:
        return 0
# Thuc thi server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=my_port)