from flask import Flask,request
from markupsafe import escape

app = Flask(__name__)

# @app.route('/user/',methods=['GET','POST'])
# def show_user_profile():
#     # show the user profile for that user
#     if request.method=='GET':
#         return "Listing all users."
#     elif request.method=='POST':
#         return "Creating a new user."



@app.route('/log/<int:user_id>', methods=['GET', 'POST','PATCH'])
def haii(user_id):
    if request.method == 'GET':
        return f"listing all the users {user_id}"
    elif  request.method == "POST" :
        return f"creating new user {user_id}"
    elif request.method == 'PATCH':
        return f"updates {user_id}"
    