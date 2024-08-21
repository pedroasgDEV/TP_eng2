""" from flask import Flask
from app.routes.users import users_bp
from app.routes.admins import admins_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(users_bp, url_prefix='/api/users')
    app.register_blueprint(admins_bp, url_prefix='/api/admins')
    
    return app """