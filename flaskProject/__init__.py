from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c27370d323cb6bcf32215586bf2ddd72'

## -----------------------------------------for MySQL--------------------------------------------------
# username = 'root'
# password = ''
# host = 'localhost'
# database = ''
# app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{username}:{password}@{host}/{database}'
## -----------------------------------------for MySQL--------------------------------------------------



## -----------------------------------------for sqlite--------------------------------------------------
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///site.db'
## -----------------------------------------for sqlite--------------------------------------------------


## -----------------------------------------for openshift--------------------------------------------------
# app.config['SQLALCHEMY_DATABASE_URI'] = environ['OPENSHIFT_MYSQL_DB_URL'] + environ['OPENSHIFT_APP_NAME']
## -----------------------------------------for openshift--------------------------------------------------

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskProject import routes
