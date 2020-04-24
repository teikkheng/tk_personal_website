from flask import Flask
from flaskwebsite.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from flaskwebsite.main.routes import main
    from flaskwebsite.errors.handlers import errors
    from flaskwebsite.sarcasm_classifier.routes import sarcasm_classifier

    app.register_blueprint(main)
    app.register_blueprint(errors)
    app.register_blueprint(sarcasm_classifier)

    return app
