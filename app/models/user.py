from flask_restx import fields
from app.extensions import api

user_model = api.model("Transaction", {
    "UUID": fields.String(attribute="UUID"),
    "USERNAME": fields.String(attribute="USERNAME"),
})

login_model = api.model("LoginModel", {
    "USERNAME": fields.String(attribute="USERNAME"),
    "PASSWORD": fields.String(attribute="PASSWORD")
})

