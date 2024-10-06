from flask import Flask
from app.routes.forum import forum_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(forum_bp, url_prefix='/api/forum')

    return app