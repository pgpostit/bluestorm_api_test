from ..extensions import db

class Pharmacy(db.Model):
    __tablename__ = "PHARMACIES"
    UUID = db.Column(db.String(256), primary_key=True, index=True)
    NAME = db.Column(db.String(50))
    CITY = db.Column(db.String(50))