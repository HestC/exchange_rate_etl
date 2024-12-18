
#routes /__init__.py

#from flask import Blueprint

# Create a blueprint object
#bp = Blueprint('main', __name__)

# Import routes here to register them with the blueprint
#from . import user_routes  # Import user routes (if you create this file)


# app/routes/__init__.py

#from flask import Blueprint

# Create a blueprint object for organizing routes.
#bp = Blueprint('main', __name__)

# Import route definitions here to register them with this blueprint.
#from . import user_routes  # Import user routes from user_routes.py.
#from . import product_routes  # Import product routes from product_routes.py.


#from flask import Blueprint, render_template
#from app.services.etl_service import fetch_exchange_rates

#main = Blueprint('main', __name__)

#@main.route('/')
#def index():
#    fetch_exchange_rates()  # Fetch exchange rates when accessing the index route
#    exchange_rates = ExchangeRate.query.all()  # Query all exchange rates
#    return render_template('index.html', exchange_rates=exchange_rates)


# revision code

from flask import Blueprint, render_template  # Add render_template to imports
from flask import Blueprint

# Create a Blueprint named 'main'
bp = Blueprint("main", __name__)

# Define the base route ("/") using the Blueprint
@bp.route("/")
def index():
    return "Welcome to the International Exchange Rate ETL Service!"


# chart code

@bp.route("/chart")
def chart():
    # Query data from the database
    from app.models import ExchangeRate  # Import model inside the route to avoid issues
    exchange_rates = ExchangeRate.query.all()

    # Prepare data for Chart.js
    labels = [rate.currency for rate in exchange_rates]
    data = [rate.rate for rate in exchange_rates]

    # Pass data to the chart template
    return render_template("chart.html", labels=labels, data=data)


# histogram route

#from flask import Blueprint, render_template
#from app.models import ExchangeRate
#import numpy as np

#bp = Blueprint("main", __name__)

#@bp.route("/")
#def index():
#    return "Welcome to the Exchange Rate ETL Project"

#@bp.route("/histogram")
#def histogram():
    # Query data from the database
#    exchange_rates = [rate.rate for rate in ExchangeRate.query.all()]

    # Calculate histogram bins and frequencies using NumPy
#    bins = np.histogram_bin_edges(exchange_rates, bins='auto')  # Automatically determine bins
#    frequencies, edges = np.histogram(exchange_rates, bins=bins)

    # Prepare data for Chart.js
 #   bin_labels = [f"{round(edges[i], 2)} - {round(edges[i+1], 2)}" for i in range(len(edges) - 1)]

    # Pass data to the template
#    return render_template("histogram.html", labels=bin_labels, data=frequencies.tolist())
