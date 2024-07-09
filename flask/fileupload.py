from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def upload():
    if request.method=='POST':
        file=request.files['f']
        file.save('/home/redmi/flask/uploaded_files/files')
        return 'SUCCESSFULLY UPLOADED FILE'
    return render_template('upload.html')