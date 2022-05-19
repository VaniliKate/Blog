# Student Number : c1956308

## Deployed at:

The site is deployed at :
[HERE](http://flask-blog-flask-blog-project.apps.cs.cf.ac.uk/) : http://flask-blog-flask-blog-project.apps.cs.cf.ac.uk/

### CHECKSUM: b8e68e70822ee4719e299267720a6c51eb0ea367

# Main Technologies Used
Main Technologies used for development of this particular project include:
1. **Python** (As main programming language for backend)
2. **MySQL** (Database)
3. **Flask** (A python micro framework for web application development)
4. **Html, Css, JavaScript** (For frontend development)

## Other Technologies:
Other technologies used in development include:
1. *bcrypt* (For encrypting and verifying passwords.)
2. *Flask-Login* (For authenticating users.)
3. *WTForms & Flask-WTF* (For form creation and data verification.)
4. *SQLAlchemy & Flask-SQLAlchemy* (For database interaction using ORM.)
5. *mysql-connector-python* (For connecting to mysql database.)
6. *Pillow* (For image manipulation (resizing) )
7. *email-validator* (Work in coordination with WTForms for email validation.)
8. *Werkzeug* (For debugging and testing.)

# Working
The application mainly consists on a "flaskProject" module, an app.py file and a config.py file.
- app.py file only run the flask app

The flaskProject Module has following files and directories:
- static (A directory containing all static assets like .css files and blog images are uploaded in a subdirectory [blog_images] in this directory).
- init.py (initializes all variables used throughout the application like database login managers etc.)
- forms.py (Contains all forms created using WTForms.)
- models.py (Contain database models)
- routes.py (Contain all functionalities to be performed when a route is accessed.)

#### note:
**Dockerfile** is also included for building and running container on (openshift server)

## How to use:

1. install all required packages from requirements.txt file.`pip install -r requirements.txt`
2. run app.py `python3 app.py`

The site currently uses an SQLite database (for convenience as there are built issues in deploying app on openshift) for changing that open init.py file in flaskProject module and uncomment and fill out MySQL settings . Then run config.py file first and then app.py file.
#### note:
sqlite database is already loaded with some data for convinience and testing.
- login credentials for admin 
-- email : iftikharR1@cardiff.ac.uk
-- password : 12345678
- test account : 
-- email : ellen@gmail.com
-- password : 12345678