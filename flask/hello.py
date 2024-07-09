from flask import url_for
from flask import Flask

app = Flask(__name__)

# @app.route("/home/")
# def hello_world():
#     return "<p>Hello, World!</p>"

@app.route('/')
def index():
    return 'index'

@app.route('/login/')
def login():
    return 'login'

# @app.route('/user/<username>')
# def profile(username):
#     return 'username'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
# print(url_for('profile',username='Sona')) 
