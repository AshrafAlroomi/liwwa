from App import db
from flask import request
import datetime
import json 

class CVSDATA(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    full_name = db.Column(db.String(128))
    birth_date = db.Column(db.Date)
    year_of_exp = db.Column(db.Integer)
    dep_id = db.Column(db.Integer)
    reg_date = db.Column(db.Date)
    cv_url = db.Column(db.String(128))


    def __init__(self,full_name,birth_date,year_of_exp,dep_id , reg_date,cv_url):
        self.full_name =full_name
        self.birth_date = birth_date
        self.year_of_exp =year_of_exp
        self.dep_id = dep_id
        self.reg_date = reg_date
        self.cv_url = cv_url
        
    def __repr__(self):
        return self.cv_url




def query(skip=0,limit=4):
    DEP = {1:'IT',2:'Hr',3:'Finance'}
    users = CVSDATA.query.order_by(CVSDATA.reg_date).limit(limit).offset(skip).all()
    resp = []
    
    for row in users:
        date = row.birth_date.strftime("%Y-%m-%d")
        
        resp.append({'Full Name':row.full_name,'Birthday':date,'Experience':row.year_of_exp , 'Department' :DEP[row.dep_id] })
    return resp




def create_user_obj(R=None):
    if R == None:
        R = request.form.to_dict()
    DEP = {'it':1,'hr':2,'finance':3}
    DATE = datetime.datetime.strptime(R['birth_date'],'%Y-%m-%d')
    FULLNAME = R['name'].strip()
    EXP = R['year_of_exp']
    DEPID = DEP[R['dep']]
    REG_DATE = datetime.datetime.now()
    URL =save_file()


    new_user = CVSDATA(full_name=FULLNAME
                    ,birth_date=DATE
                    ,year_of_exp=EXP
                    ,dep_id=DEPID,
                    reg_date=REG_DATE,
                    cv_url = URL)
    
    db.session.add(new_user)
    db.session.commit()
    






def get_cv_url(id):
    
    user = CVSDATA.query.get(id)
    if user:
        return user.cv_url
    else:
        return None








import uuid
def save_file():
    name_ = str(uuid.uuid4().int)[0:15]
    file = request.files.get('cv')
    ext = file.filename.split('.')[-1]
    url = 'App/Cvs/{}_cv.{}'.format(name_,ext)
    file.save(url)
    
    return url



    


