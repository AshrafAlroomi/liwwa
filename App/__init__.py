from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

database_username ="root"
database_password ="root"


app = Flask(__name__)

url = 'mysql+pymysql://{}:{}@localhost/mysql'.format(database_username,database_password)
app.config['SECRET_KEY'] = 'qwriojqoirjqwrijqwoirjqwoirjiqwjr39208ndsncx,mvosfaewqr'
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['BASE_DIR'] = dir_path = os.path.dirname(os.path.realpath(__file__))

db = SQLAlchemy(app)

from App import Model

db.create_all()
db.session.commit()



from App.Views import index
from App.Resources import new_user,admin_panel,download_cv





