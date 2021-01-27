from App import app
from flask import  jsonify,request,render_template
from App.Resources import new_user

@app.route('/',methods=['GET','POST'])
def index():
    errors = {}
    if request.method == 'POST':

        RESP = new_user().json
        
        if RESP.get('success') == True:
            return render_template('thank you.html')
        else:
            return render_template('registration.html' , errors = RESP.get('erorrs'))

    return render_template('registration.html' , errors=errors)

@app.route('/admin',methods=['GET'])
def admin():
    return render_template('admin.html')



