from flask import Flask

from app.config import Config
from app.routes.main import bp as main_bp
from app.routes.api_ml import bp as api_ml_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(main_bp)
    app.register_blueprint(api_ml_bp)
    return app
