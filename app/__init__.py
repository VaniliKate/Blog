from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

from .config import configuration_options
bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()

def create_app(configuration):
    app = Flask(__name__)
    app.config.from_object(configuration_options[configuration])
   
    print(app.config)


    print(app.config.get('SQLALCHEMY_DATABASE_URI'))
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    manager = LoginManager()
    manager.login_view = 'auth.login'
    manager.init_app(app)
    

    from .models import User
    @manager.user_loader
    def user_loader(user_id):
        return User.query.get(user_id)
    

    from .requests import configure_request
    configure_request(app)

    from .auth.views import auth as auth_blueprint
    from .views import app as app_blueprint
    from .pitches.views import pitch as pitch_blueprint
    from .categories.views import category as category_blueprint
    from .profile.views import profile as profile_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(app_blueprint)
    app.register_blueprint(category_blueprint)
    app.register_blueprint(pitch_blueprint)
    app.register_blueprint(profile_blueprint)
    
    return app