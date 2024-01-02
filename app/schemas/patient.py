from ..extensions import db

class Patient(db.Model):
    __tablename__ = "PATIENTS"
    UUID = db.Column(db.String(256), primary_key=True, index=True)
    FIRST_NAME = db.Column(db.String(30))
    LAST_NAME = db.Column(db.String(30))
    DATE_OF_BIRTH = db.Column(db.DateTime)