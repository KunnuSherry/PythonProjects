from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "sangyasharma"

    # Use an environment variable for the database URI or fallback to an in-memory database
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///:memory:')
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

def create_database(app):
    # Check if the database path exists, but skip creation for in-memory database
    db_path = f'./{DB_NAME}'
    if app.config['SQLALCHEMY_DATABASE_URI'] != 'sqlite:///:memory:' and not os.path.exists(db_path):
        with app.app_context():
            db.create_all()
        print('Created Database!')
    else:
        print('Using in-memory database or existing database.')
