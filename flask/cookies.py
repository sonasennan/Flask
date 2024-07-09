from flask import Flask,request,make_response,render_template

app=Flask(__name__)

# @app.route('/',methods=['GET','POST'])
# def register():
#     if request.method == 'POST':
#         un=request.form['username']
#         resp=make_response(render_template('welcome.html',data=un))
#         resp.set_cookie('username',un)
#         return resp
#     return render_template('login.html')
@app.route('/',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        uname=request.form['username']
        passwd=request.form['password']
        resp=make_response(render_template('login.html'))
        resp.set_cookie('Username',uname)
        resp.set_cookie('Password',passwd)
        return resp
    return render_template('register.html')

@app.route('/log',methods=['GET','POST'])
def show_cookie():
    if request.method == 'POST':
        ucookies=request.cookies.get('Username')
        pcookies=request.cookies.get('Password')
        user_form = request.form['username']
        if user_form == ucookies:
            return f"hii {user_form}"
    return render_template("login.html")
        



