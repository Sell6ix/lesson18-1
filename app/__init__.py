import os
import dotenv
from flask import Flask


def create_app() -> Flask:
    dotenv.load_dotenv(override=True)
    app = Flask(__name__)

    if os.environ.get("APP_CONFIG") == "development":
        from config.development import Config
        app.config.from_object(Config())
    else:
        from config.development import Config
        app.config.from_object(Config())

    app.app_context().push()
    return app
