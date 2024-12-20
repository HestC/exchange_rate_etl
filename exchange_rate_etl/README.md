
# Exchange Rate ETL Project - Inner README

## Overview

This project extracts real-time exchange rate data from the Exchange Rate API, processes it into a usable format, and stores it in a relational database. It also includes a visualization feature to display exchange rate trends using Chart.js, integrated into a Flask web application deployed on Render.com.

This inner README provides a detailed walkthrough of the specific components and operations that constitute the pipeline.

* Note there is an outer README.md on the main **exchange_rate_etL** Github page.
---

## Project Directory Structure

```
exchange_rate_etl/
├── app/
│   ├── templates/
│   ├── static/
│   ├── __init__.py
│   └── routes.py
├── data/
│   └── exchange_rates.db
├── tests/
├── config.py
├── etl_pipeline.py
├── requirements.txt
├── README.md (this file)
└── deploy.yml
```

---

## Core Components

### 1. **ETL Pipeline** (`etl_pipeline.py`)
- **Extract**: 
  - Connects to the Exchange Rate API to fetch real-time exchange rate data.
  - Uses the `requests` library to make API calls.

- **Transform**: 
  - Cleans and structures the data, converting it into a format suitable for relational storage.
  - Handles missing or malformed data gracefully.

- **Load**:
  - Stores the transformed data into a relational database (`SQLite`) using SQLAlchemy ORM.

### 2. **Flask Web Application**
- Located in the `app/` directory.
- Provides routes for:
  - Displaying a Chart.js visualization of the exchange rate data.
  - Triggering manual ETL pipeline execution.
- Serves HTML templates and static assets for the user interface.

### 3. **Visualization**
- **Chart.js**:
  - Displays exchange rate trends in a dynamic bar chart.
  - Fetches data from Flask endpoints to render real-time visualizations.

### 4. **Deployment**
- **Render.com**:
  - The application is deployed for external access.
  - `deploy.yml` includes configuration details for deployment automation.

---

## Setup Instructions

### Prerequisites
1. Python 3.11 installed (macOS or Windows).
2. Install SQLAlchemy for database management.
3. Install `virtualenv` to manage project dependencies in an isolated environment.

### Environment Setup
1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd exchange_rate_etl
   ```
2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Environment Variables
1. Create a `.env` file in the root directory.
2. Add the following environment variables:
   ```
   API_KEY=<your_exchange_rate_api_key>
   DATABASE_URL=sqlite:///data/exchange_rates.db
   ```

### Initializing the Database
1. Ensure the `data/` directory exists:
   ```bash
   mkdir -p data  # On Windows use `mkdir data`
   ```
2. Run the following command to create and initialize the database:
   ```bash
   python -c "from etl_pipeline import initialize_db; initialize_db()"
   ```
   This will create the `exchange_rates.db` file in the `data/` directory.

### Running the Project Locally
1. Run the ETL pipeline manually to populate initial data:
   ```bash
   python etl_pipeline.py
   ```
2. Start the Flask application:
   ```bash
   flask run
   ```
3. Access the app at `http://127.0.0.1:5000`.

### Running Tests
1. **Unit Tests**:
   - Ensure the virtual environment is active.
   - Run the tests located in the `tests/` directory:
     ```bash
     pytest tests/
     ```
2. Tests validate data extraction, transformation, and database loading processes.

---

## Testing
- **Unit Tests**:
  - Located in the `tests/` directory.
  - Validate data extraction, transformation, and database loading processes.

---

## Deployment to Render.com
1. Push the repository to GitHub.
2. Connect the Render service to the repository.
3. Use the `deploy.yml` file to automate deployment.

---

## Future Enhancements
- Integration with additional APIs for diverse financial data.
- Enhanced data transformations using Pandas for complex analytics.
- Advanced visualizations, including line charts and real-time updates.



























































