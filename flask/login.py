from flask import Flask, render_template ,request

app = Flask(__name__)


@app.route("/" , methods=['GET','POST'])
def userlogin():
    d={}
    d.update({'sonasennan':'one','aiswarya':'two','reshma':'three','haritha':'four'})
    if request.method=='POST':
        un=request.form['username']
        pw=request.form['password']
        for i in d:
            if un in d.keys() and pw in d.values():
                return render_template('success.html',username=un)
            else:
                return render_template('failed.html')
    return render_template('login.html')