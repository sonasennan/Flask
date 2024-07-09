from flask import Flask, render_template ,request,session



app = Flask(__name__)
app.secret_key="hello"
@app.route('/',methods=['GET','POST'])
def register():
    
    if request.method=='POST':
        username = request.form['username']
        session_username = session.get('username')
        if username == session_username:
            return 'logged in'
        

        else:
            session['username']=request.form['username']
            return 'you are signed up'
    return render_template('login.html')

    