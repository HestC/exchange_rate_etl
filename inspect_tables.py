"""
Script to Inspect Database Tables Using SQLAlchemy.
Fixes the module search path, initializes the Flask app,
and lists the existing database tables.
"""

import sys
import os

# Step 1: Adjust the path to point to the nested project directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "exchange_rate_etl"))
sys.path.insert(0, project_root)

# Step 2: Import Flask app factory and database
from app import create_app, db
from sqlalchemy import inspect

# Initialize the Flask app
app = create_app()

# Activate the application context and inspect the database
with app.app_context():
    inspector = inspect(db.engine)
    tables = inspector.get_table_names()
    print("Existing tables:", tables)
