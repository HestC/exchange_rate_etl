
#  Exchange Rate ETL Project

## Overview

The Exchange Rate ETL Project is a data pipeline designed to handle the extraction, transformation, and loading of exchange rate data from the Exchange Rate API,a public API providing real-time exchange rates. The project focuses on processing real-time currency exchange data, storing it in a relational database, and providing visual insights using a bar chart built with Chart.js. The API was developed using Flask, and has two main endpoints.

   * /reload endpoint: reloads data and produces a table of realtime currency exchange rates
     
   * /visualization: produces a bar chart of the top 10 currencies





* Note: This repository includes an additional inner README file within the exchange_rate_etl directory. The inner README provides deeper insights into the specific components and detailed operations of the project.



## Data Source

The pipeline uses data from the ExchangeRate-API, a public API providing real-time exchange rates.  https://www.exchangerate-api.com/

Base URL: https://v6.exchangerate-api.com/v6/d6c06f55edf64bb0d48a4a51/latest/USD

The dataset includes key features such as exchange rates for multiple currencies relative to a specified base currency, in this case the US dollar ($USD).

* reload end point: http://127.0.0.1:5001/reload

* visualization endpoint: http://127.0.0.1:5001/chart

data is loaded using the app.py file via the command line in the IDE terminal: python ap.py


## Transformation Steps

The raw data is extracted in JSON format.

The relevant exchange rate information is transformed into a Pandas DataFrame with the following columns:

 * currency: Three-letter currency code (e.g., USD, EUR).

 * rate: Exchange rate relative to the base currency.

 * date: The timestamp of the data extraction (automatically added).

## Destination of the Data

The transformed data is loaded into a SQLite database using SQlalchemy located in the instance directory:

 * Database Name: exchange_rates.db.

 * Table Name: exchange_rate.

## Pipeline Automation

The pipeline is automated using a Python script (etl_service.py) that executes the following steps:

* Extraction: Extracts data from the Exchange_Rates API using the requests library

* Transformation: Processes the JSON response into a structured data frame

* Loading: Stores the transformed data into the SQLite database using SQLAlchemy
  

  


