import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)

    # Default database path: Use a writable 'instance' folder in the project
    db_path = os.path.join(app.instance_path, "exchange_rates.db")

    # Ensure the instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    # SQLAlchemy database URI
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # Create tables if they don’t exist
    with app.app_context():
        db.create_all()

    # Register the existing Blueprint
    from app.routes import bp
    app.register_blueprint(bp)

    return app
