

# this code handles extraction,transformations and loading

        # app/services/etl_service.py

#import requests
#import pandas as pd
#from ..models import ExchangeRate, db
from app.models import ExchangeRate, db


# configuration
#API_KEY = "d6c06f55edf64bb0d48a4a51"  #  actual API key
#BASE_CURRENCY = "USD"  # Change the base currency as needed
#API_URL = f"https://v6.exchangerate-api.com/v6/d6c06f55edf64bb0d48a4a51/latest/{BASE_CURRENCY}"


#def extract():
#    """Fetch exchange rates using API key and base currency."""
#   try:
#        response = requests.get(API_URL)  # Send GET request to the API
#       if response.status_code == 200:
#            print("Extraction successful.")
#           return response.json()
#        else:
#            print(f"Failed to fetch data. Status Code: {response.status_code}")
#            return None
#    except Exception as e:
#        print(f"An error occurred: {e}")
#        return None

#def transform(data):
#    """Transform the extracted data into a DataFrame."""
#    if data and 'conversion_rates' in data:
#        # Flatten the rates data into a DataFrame
#        df = pd.DataFrame(data['conversion_rates'].items(), columns=['currency', 'rate'])
#        print("Transformation successful.")
#        return df
#    else:
#        print("Invalid data for transformation.")
#        return None

#def load(df):
#    """Load the DataFrame into the SQLite database."""
#    if df is not None:
#        for _, row in df.iterrows():
#            rate = ExchangeRate(currency=row['currency'], rate=row['rate'])
#            db.session.add(rate)
#        db.session.commit()
#        print("Data loaded into the database successfully.")
#    else:
#        print("No data to load.")

# Run ETL Pipeline
#if __name__ == "__main__":
 #   data = extract()
#    if data:
#        df = transform(data)
#        load(df)

# revised code
# this code handles extraction,transformations and loading
# app/services/etl_service.py


from app import create_app  # Import the Flask app factory
from app.models import ExchangeRate, db  # Import the ExchangeRate model and db
import pandas as pd
import requests

# Configuration
#API_KEY = "d6c06f55edf64bb0d48a4a51"  # API key
#BASE_CURRENCY = "USD"
#API_URL = f"https://v6.exchangerate-api.com/v6/d6c06f55edf64bb0d48a4a51/latest/{BASE_CURRENCY}"
#def extract():
#    """Fetch exchange rates from the API."""
#    try:
#        response = requests.get(API_URL)  # Send a GET request to the API
#        if response.status_code == 200:
#            print("Extraction successful.")
#            return response.json()  # Return JSON data
#        else:
#            print(f"Failed to fetch data. Status code: {response.status_code}")
#            return None
#    except Exception as e:
#        print(f"An error occurred during extraction: {e}")
#        return None

#def transform(data):
#    """Transform the extracted data into a Pandas DataFrame."""
#    if data and 'conversion_rates' in data:
#        # Convert rates dictionary into a DataFrame
#        df = pd.DataFrame(data['conversion_rates'].items(), columns=['currency', 'rate'])
#        print("Transformation successful.")
#        return df
#    else:
#        print("Invalid data for transformation.")
#        return None

#def load(df):
#    """
#    Load the transformed data into the database.
#    Each currency-rate pair is inserted into the ExchangeRate table.
#    """
#    if df is not None:
#        for _, row in df.iterrows():
#            rate = ExchangeRate(currency=row['currency'], rate=row['rate'])  # Create ExchangeRate object
#            db.session.add(rate)  # Add the object to the session
#        db.session.commit()  # Commit the session to save changes
#        print("Data loaded into the database successfully.")
#    else:
#        print("No data to load.")

# Main ETL function
#def run_etl():
#    """Run the ETL process inside the Flask application context."""
#    app = create_app()  # Create the Flask app
#    with app.app_context():  # Ensure the app context is active
#        data = extract()  # Step 1: Extract data
#        if data:
#            df = transform(data)  # Step 2: Transform data
#            load(df)  # Step 3: Load data

# Execute the ETL pipeline
#if __name__ == "__main__":
#    run_etl()



#revised code
#load necessary libraries
from app import create_app  # Import the Flask app factory function
from app.models import ExchangeRate, db  # Import database and ExchangeRate model
import pandas as pd
import requests


# check extracted data --revised API configuration
def extract():
    """
    Fetch exchange rates from the API.
    Handles API errors and verifies data.
    """
    import requests

    # Replace 'YOUR_API_KEY' with your actual API key
    API_KEY = "d6c06f55edf64bb0d48a4a51"
    API_URL = f"https://v6.exchangerate-api.com/v6/d6c06f55edf64bb0d48a4a51/latest/USD"

    # Fetch data
    response = requests.get(API_URL)
    data = response.json()

    # print raw data for debugging
    print("Extracted Data:")
    print(data)

    # Check for errors in response
    if data.get("result") == "error":
        print(f"API Error: {data.get('error-type')}")
        return {}

    return data


















#def transform(data):
    """
#    Transform the extracted data into a Pandas DataFrame.
#    Args:
#        data (dict): The API response data.
#    Returns:
#        DataFrame: A DataFrame containing currency and rate columns if successful, otherwise None.
    """
#    if data and 'conversion_rates' in data:
#        # Convert the 'conversion_rates' dictionary to a DataFrame
#        df = pd.DataFrame(data['conversion_rates'].items(), columns=['currency', 'rate'])
#        print("Transformation successful.")
#        return df
#    else:
#        print("Invalid data for transformation.")
#        return None


#revised transform code


import pandas as pd
from datetime import datetime

def transform(data):
    """
    Transform the extracted JSON data into a Pandas DataFrame.

    Columns:
    - currency: Three-letter currency code.
    - rate: Exchange rate relative to the base currency.
    - date: The timestamp of data extraction.
    """
    # Ensure 'conversion_rates' key exists in the response
    rates = data.get('conversion_rates', {})
    if not rates:
        print("No conversion_rates data found in the extracted JSON.")
        return pd.DataFrame(columns=['currency', 'rate', 'date'])

    # Add a timestamp
    timestamp = datetime.utcnow()

    # Convert to DataFrame
    df = pd.DataFrame(list(rates.items()), columns=['currency', 'rate'])
    df['date'] = timestamp

    # Print the transformed DataFrame for verification
    print("Transformed DataFrame:")
    print(df.head())  # Display the first few rows
    return df




























def load(df):
    """
    Load the transformed data into the SQLite database.
    Args:
        df (DataFrame): A DataFrame containing currency-rate pairs.
    """
    if df is not None:
        try:
            # Iterate through the DataFrame rows and add each currency-rate pair to the database
            for _, row in df.iterrows():
                rate = ExchangeRate(currency=row['currency'], rate=row['rate'])
                db.session.add(rate)  # Add the object to the session
            db.session.commit()  # Commit the transaction
            print("Data loaded into the database successfully.")
        except Exception as e:
            print(f"An error occurred during loading: {e}")
    else:
        print("No data to load.")


def run_etl():
    """
    Execute the entire ETL pipeline (extract, transform, load) within the Flask application context.
    """
    app = create_app()  # Create the Flask application
    with app.app_context():  # Activate the application context
        data = extract()  # Step 1: Extract data
        if data:
            df = transform(data)  # Step 2: Transform data
            load(df)  # Step 3: Load data


# Run the ETL process when this file is executed directly
if __name__ == "__main__":
    run_etl()
