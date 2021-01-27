from App import app
from flask import jsonify,request,abort,send_from_directory
import datetime
from marshmallow import Schema, fields , pre_load
from marshmallow.validate import Length, Range
from App.Model import create_user_obj,query,get_cv_url
from functools import wraps






def Authentication(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        key = request.headers.get('X-ADMIN')
        print(key)
        if str(key) == str(1):
            
            return func(*args, **kwargs)

        return abort(403)
    return wrapped













@app.route('/api/registration',methods=['POST'])
def new_user():
    print(request.form.to_dict())
    
    v = RegistrationInput()
    validation = v.validate(data=request.form.to_dict())
    if validation:
        return jsonify({'erorrs':validation})

    f = validate_files()
    if f:
        return jsonify({'erorrs':{'cv':['missing required file']}})

    #create user
    create_user_obj()

    return jsonify(success=True)
    








@app.route('/api/admin',methods=['GET'])
@Authentication
def admin_panel():
    
    skip = request.args.get('skip')
    limit = request.args.get('limit')
    if limit == None:
        limit=4
    v = AdminPanelInput()
    validation = v.validate(data={'skip':skip,'limit':limit})
    if validation:
        return jsonify({'erorrs':validation})
    
    users = query(int(skip),int(limit))
    return jsonify({'users':users})
    




@app.route('/api/download/<string:userid>',methods=['GET'])
@Authentication
def download_cv(userid):

    userid = int(userid)
    subpath = get_cv_url(userid)
    if subpath == None:
        return jsonify({'erorrs':'No User With this ID'})
    
    filename = subpath.split('/')[-1]
    path = app.config['BASE_DIR'] + '\Cvs'
    
    return send_from_directory(path,filename=filename)




















class AdminPanelInput(Schema):
    skip = fields.Int(required=True,validate=Range(min=0))
    limit = fields.Int(required=True,validate=Range(min=1,max=50))





class RegistrationInput(Schema):
    name = fields.Str(required=True,error_messages={'required':'please provide you full name'})
    birth_date = fields.Str(required=True , error_messages={'required':'the right format for birth_date is y-m-d '})
    year_of_exp = fields.Int(required=True,validate=Range(min=0) )
    dep = fields.Str(required=True,allow_none=False,validate=Length(min=2))



    @pre_load
    def pre_val(self, in_data, **kwargs):
        DEP = {'it':1,'hr':2,'finance':3}

        if not all(i in in_data for i in ['name','birth_date','dep']):
            return in_data
        #name
        in_data['name'] = in_data['name'].lower().strip()
        if len(in_data['name'].split(' ')) < 3:
            in_data.pop('name')


        #date
        in_data['birth_date'] = in_data['birth_date'].strip()
        
        if len(in_data['birth_date'].split('-')) == 3:
            try:
                
                datetime.datetime.strptime(in_data['birth_date'],'%Y-%m-%d')
                
            except:
                print(in_data['birth_date'])
                in_data.pop('birth_date')
        else:
            in_data.pop('birth_date')


        #dep
        in_data['dep'] = in_data['dep'].lower().strip().replace(' ', '-')
        if in_data['dep'] not in DEP:
            in_data.pop('dep')

        return in_data


    

def validate_files():
    try:
        file = request.files.get('cv')
        ext = file.filename.split('.')[-1]
        if ext.lower() in ['pdf','docx']:
            return False
    except : 
        pass
    
    return True
