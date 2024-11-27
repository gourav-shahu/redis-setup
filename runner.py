from flask import Flask
from utils.extensions import init_extensions


def create_app():
    app = Flask(__name__)
    init_extensions(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=8000)
