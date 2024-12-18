

from app import create_app, db  # Import Flask app factory and SQLAlchemy instance
from app.models import ExchangeRate  # Import the ExchangeRate model

# Initialize the Flask app
#app = create_app()

#with app.app_context():  # Activate the application context
    # Check and print the existing tables in the database
   # print("Existing tables:", db.engine.table_names())  # Lists tables in the database


#revision 2

"""
Script to Inspect Database Tables Using SQLAlchemy.
This script initializes the Flask app, connects to the database, 
and lists the existing tables using SQLAlchemy's inspect module.
"""

from app import create_app, db  # Import Flask app factory and SQLAlchemy instance
from sqlalchemy import inspect  # Import inspect module to get table information
from app.models import ExchangeRate  # Import the ExchangeRate model (if needed)

# Initialize the Flask app
app = create_app()

# Activate the application context
with app.app_context():  
    # Use SQLAlchemy's inspect module to interact with the database engine
    inspector = inspect(db.engine)  # Get the database engine
    tables = inspector.get_table_names()  # Get the list of table names
    print("Existing tables:", tables)  # Print the existing tables





"""
#Test Script to Verify SQLite Access to exchange_rates.db
"""

#import sqlite3

# Path to the database file
#db_path = "/Users/chester/exchange_rate_etl/exchange_rate_etl/instance/exchange_rates.db"

#try:
 #   # Try connecting to the database
 #   conn = sqlite3.connect(db_path)
#    print("Successfully connected to the database.")
#    conn.close()
#except sqlite3.OperationalError as e:
 #   print(f"SQLite Error: {e}")
