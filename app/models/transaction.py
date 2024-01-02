from flask_restx import fields
from app.extensions import api
from .patient import patient_model
from .pharmacy import pharmacy_model

transaction_model = api.model("Transaction", {
    "UUID": fields.String(attribute="UUID"),
    "amount": fields.Float(attribute="AMOUNT"),
    "timestamp": fields.DateTime(attribute="TIMESTAMP"),
    "patient_data": fields.Nested(patient_model, attribute="patient"),
    "pharmacy_data": fields.Nested(pharmacy_model, attribute="pharmacy")
})

