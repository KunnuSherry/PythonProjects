from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
from flask_migrate import Migrate
import redis
from flask_session import Session

# Initialize the SQLAlchemy instance
db = SQLAlchemy()
DB_NAME = "database.db"

# Initialize the Redis instance
redis_client = redis.StrictRedis.from_url(
    os.getenv('REDIS_URL', 'redis://default:VdeAgoBZmtVNW8267FMjVfvz1NbULl7s@redis-14184.c61.us-east-1-3.ec2.redns.redis-cloud.com:14184'),
    decode_responses=True
)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "sangyasharma"

    # Use an environment variable for the database URI or fallback to a default URI
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgres://postgres.gslsqdasmlnujfuzrpns:ZlvzXokdrU7wB7Lg@aws-0-us-east-1.pooler.supabase.com:6543/postgres?sslmode=require&supa=base-pooler.x')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional: disable modification tracking

    # Configuring Flask-Session to use Redis
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_PERMANENT'] = False
    app.config['SESSION_USE_SIGNER'] = True
    app.config['SESSION_REDIS'] = redis_client  # Using the Redis client for session management

    # Initialize the app with Redis and SQLAlchemy
    db.init_app(app)
    migrate = Migrate(app, db)

    # Register Blueprints
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Initialize LoginManager for Flask-Login
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        from .models import User  # Importing here to avoid circular import issues
        return User.query.get(int(id))

    create_database(app)

    return app

def create_database(app):
    # Check if the database exists, and create it if not
    db_path = f'./{DB_NAME}'
    if app.config['SQLALCHEMY_DATABASE_URI'] != 'postgres://postgres.gslsqdasmlnujfuzrpns:ZlvzXokdrU7wB7Lg@aws-0-us-east-1.pooler.supabase.com:6543/postgres?sslmode=require&supa=base-pooler.x' and not os.path.exists(db_path):
        with app.app_context():
            db.create_all()
        print('Created Database!')
    else:
        print('Using in-memory database or existing database.')

