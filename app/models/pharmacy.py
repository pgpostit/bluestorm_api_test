from flask_restx import fields

from app.extensions import api

pharmacy_model = api.model("Pharmacy", {
    "UUID": fields.String(attribute="UUID"),
    "Name": fields.String(attribute="NAME"),
    "City": fields.String(attribute="CITY"),
})

