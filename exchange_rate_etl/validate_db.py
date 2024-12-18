
# here I validate that the database is properly loading

"""
Validation Script: This script checks the data loaded into the database.
It queries the exchange_rate table and prints the first 10 rows for verification.
"""

from app import create_app, db  # Import Flask app and SQLAlchemy instance
from app.models import ExchangeRate  # Import the ExchangeRate model

# initialize the Flask app
app = create_app()

with app.app_context():  # Activate the application context
    # Query the database for the first 10 rows
    records = ExchangeRate.query.limit(10).all()

    # print the retrieved records
    print("Loaded data:")
    for record in records:
        print(f"Currency: {record.currency}, Rate: {record.rate}, Date: {record.date}")
