from flask import Flask

from .extensions import api, db, jwt

from .resources.patient import patient_ns
from .resources.pharmacy import pharmacy_ns
from .resources.transaction import transaction_ns
from .resources.user import user_ns

def create_app(database_uri="sqlite:///backend_test.db"):
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "testsecretkey"

    api.init_app(app)
    db.init_app(app)
    jwt.init_app(app)

    api.add_namespace(patient_ns)
    api.add_namespace(pharmacy_ns)
    api.add_namespace(transaction_ns)
    api.add_namespace(user_ns)

    return app

