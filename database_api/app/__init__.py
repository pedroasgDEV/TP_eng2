""" from flask import Flask
from app.routes.users import user_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(user_bp, url_prefix='/api/user')

    return app """