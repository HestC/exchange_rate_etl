
# Load project libraries
import os
from flask import Flask, render_template, jsonify
import pandas as pd
import requests
from sqlalchemy import create_engine



# Initialize Flask app, explicitly pointing to the correct templates folder
app = Flask(__name__, template_folder="exchange_rate_etl/app/templates")

# Database configuration
DATABASE_URL = "sqlite:///exchange_rate.db"  # Existing database
engine = create_engine(DATABASE_URL)

# Route: Reload exchange rates data
@app.route('/reload', methods=['GET'])
def reload_data():
    """
    Fetch exchange rates from the API, save them to the database,
    and print debug information for troubleshooting.
    """
    try:
        # Fetch exchange rates from the API
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()

        # Debug: Print the raw API response
        print("API Response:", data)

        # Check if 'rates' key exists
        if "rates" in data:
            rates_df = pd.DataFrame(data['rates'].items(), columns=['Currency', 'Rate'])
            print("DataFrame Created:", rates_df)  # Debug: Confirm DataFrame

            # Save to SQLite database
            rates_df.to_sql("exchange_rates", engine, if_exists="replace", index=False)

            return jsonify({"status": "success", "message": "Data reloaded successfully!"})
        else:
            print("Error: 'rates' key not found in API response.")
            return jsonify({"status": "error", "message": "'rates' key not found in API response."})
    except Exception as e:
        print("Error occurred:", e)
        return jsonify({"status": "error", "message": str(e)})

# Route: Display exchange rates as a bar chart
@app.route('/chart', methods=['GET'])
def show_chart():
    """
    Display a bar chart of the top 10 exchange rates.
    """
    try:
        # Query the top 10 exchange rates from the database
        query = "SELECT Currency, Rate FROM exchange_rates ORDER BY Rate DESC LIMIT 10"
        rates_df = pd.read_sql(query, engine)

        # Handle case where the database is empty
        if rates_df.empty:
            print("Error: No data found in the database.")
            return jsonify({"status": "error", "message": "No data found in the database."})

        # Prepare data for the bar chart
        labels = rates_df['Currency'].tolist()
        data = rates_df['Rate'].tolist()
        print("Labels for Chart:", labels)
        print("Data for Chart:", data)

        # Render the chart
        return render_template("chart.html", labels=labels, data=data)

    except Exception as e:
        print("Error in /chart route:", e)
        return jsonify({"status": "error", "message": str(e)})

# Run the app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
