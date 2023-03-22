
#this file makes the folder website a python package

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create__app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asdfjasldkfjaasdfasd  asdfasdf'           
    #kind of encrypt or secure the cookies and the session data related to our website. more of like the secret key or our app
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    #now in order to include the auth and view files in this init file, we first have to import them    
    from .views import views
    from .auth import auth

    #then register the blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Note 

    create_database(app)


    return app

def create_database(app):
    if not path.exist('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')