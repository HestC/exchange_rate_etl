
**Exchange Rate ETL Project**
**Overview Data Source**

The pipeline uses data from the ExchangeRate-API, a public API providing real-time exchange rates.

Base URL: https://v6.exchangerate-api.com/v6/d6c06f55edf64bb0d48a4a51/latest/USD

Data includes exchange rates for multiple currencies relative to a specified base currency.

Transformation Steps

The raw data is extracted in JSON format.

The relevant exchange rate information is transformed into a Pandas DataFrame with the following columns:

    currency: Three-letter currency code (e.g., USD, EUR).

    rate: Exchange rate relative to the base currency.

    date: The timestamp of the data extraction (automatically added).

Destination of the Data

The transformed data is loaded into a SQLite database located in the instance directory:

    Database Name: exchange_rates.db.

    Table Name: exchange_rate.

Pipeline Automation

The pipeline is automated using a Python script (etl_service.py) that executes the following steps:

    Extraction: Fetches data from the API using the requests library

    Transformation: Processes the JSON response into a structured DataFrame

    Loading: Stores the transformed data into the SQLite database using SQLAlchemy

