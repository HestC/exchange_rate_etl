
 #app/exchange_rate.py


from app import db
from datetime import datetime

#class ExchangeRate(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    date = db.Column(db.DateTime, default=datetime.utcnow)
#    currency = db.Column(db.String(3), nullable=False)
#    rate = db.Column(db.Float, nullable=False)

#    def __repr__(self):
#        return f'<ExchangeRate {self.currency} on {self.date}>'








#from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()

#class ExchangeRate(db.Model):
#    __tablename__ = 'exchange_rates'

#    id = db.Column(db.Integer, primary_key=True)
#    currency = db.Column(db.String(3), nullable=False)
#    rate = db.Column(db.Float, nullable=False)

#    def __repr__(self):
#        return f"<ExchangeRate {self.currency}: {self.rate}>"


# app/exchange_rate.py

#from . import db

#class ExchangeRate(db.Model):
   # id = db.Column(db.Integer, primary_key=True)
   # currency = db.Column(db.String(3), nullable=False)
   # rate = db.Column(db.Float, nullable=False)

#revision 4
"""
This module defines the ExchangeRate model for interacting with the exchange_rate table in the database.
The model includes the table name, columns, and their constraints.
"""

from app import db  # Import SQLAlchemy instance
from datetime import datetime  # Import for automatic timestamping

class ExchangeRate(db.Model):
    """
    ExchangeRate model maps to the exchange_rate table in the database.
    """
    __tablename__ = 'exchange_rate'  # Table name must match the existing table in the database

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each row
    currency = db.Column(db.String(3), nullable=False)  # Currency code (e.g., USD, EUR)
    rate = db.Column(db.Float, nullable=False)  # Exchange rate value
    date = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp for the record creation

    def __repr__(self):
        """
        Define how the object is printed for debugging.
        Example: <ExchangeRate USD on 2024-12-12>
        """
        return f'<ExchangeRate {self.currency} on {self.date}>'
