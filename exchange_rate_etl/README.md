

**Overview**
**Data Source**

The pipeline uses data from the ExchangeRate-API, a public API providing real-time exchange rates.
    
Base URL: https://v6.exchangerate-api.com/v6/d6c06f55edf64bb0d48a4a51/latest/USD
    
Data includes exchange rates for multiple currencies relative to a specified base currency.

**Transformation Steps**

The raw data is extracted in JSON format.

The relevant exchange rate information is transformed into a Pandas DataFrame with the following columns:
    
1) currency: Three-letter currency code (e.g., USD, EUR).
        
2) rate: Exchange rate relative to the base currency.
        
3) date: The timestamp of the data extraction (automatically added).

**Destination of the Data**

The transformed data is loaded into a SQLite database located in the instance directory:
    
 1) Database Name: exchange_rates.db.
        
 2) Table Name: exchange_rate.

**Pipeline Automation**

The pipeline is automated using a Python script (etl_service.py) that executes the following steps:
    
1) Extraction: Fetches data from the API using the requests library
        
2) Transformation: Processes the JSON response into a structured DataFrame
        
3) Loading: Stores the transformed data into the SQLite database using SQLAlchemy

