from ..extensions import db

class Transaction(db.Model):
    __tablename__ = "TRANSACTIONS"
    UUID = db.Column(db.String(256), primary_key=True, index=True)
    PATIENT_UUID = db.Column(db.String(256), db.ForeignKey('PATIENTS.UUID'))
    PHARMACY_UUID = db.Column(db.String(256), db.ForeignKey('PHARMACIES.UUID'))
    AMOUNT = db.Column(db.Float)
    TIMESTAMP = db.Column(db.DateTime)

    patient = db.relationship('Patient', backref=db.backref('transactions', lazy=True))
    pharmacy = db.relationship('Pharmacy', backref=db.backref('transactions', lazy=True))


