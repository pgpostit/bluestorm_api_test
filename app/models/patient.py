from flask_restx import fields

from app.extensions import api

patient_model = api.model("Patient", {
    "UUID": fields.String(attribute="UUID"),
    "fName": fields.String(attribute="FIRST_NAME"),
    "lName": fields.String(attribute="LAST_NAME"),
    "Birthday": fields.DateTime(attribute="DATE_OF_BIRTH"),
})

