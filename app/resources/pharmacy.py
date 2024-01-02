from flask_restx import Resource, Namespace

from app.models.pharmacy import pharmacy_model
from app.schemas.pharmacy import Pharmacy

pharmacy_ns = Namespace("pharmacies", description="Pharmacy data operations.")

pharmacy = Pharmacy()

@pharmacy_ns.route("", doc={"description": "List all pharmacies."})
class PharmaciesList(Resource):
    @pharmacy_ns.marshal_list_with(pharmacy_model)
    def get(self):
        """
        List all pharmacies.
        """
        return pharmacy.query.all()

@pharmacy_ns.route("/pharmacy/id:<string:uuid>", doc={"description": "List all pharmacies."})
class PharmacyBiId(Resource):
    @pharmacy_ns.marshal_with(pharmacy_model)
    def get(self, uuid):
        """
        Get a pharmacy by id.
        """
        return pharmacy.query.filter_by(UUID=uuid).first()

@pharmacy_ns.route("/pharmacy/name:<string:name>", doc={"description": "List all pharmacies."})
class PharmaciesByName(Resource):
    @pharmacy_ns.marshal_list_with(pharmacy_model)
    def get(self, name):
        """
        Get pharmacies by name.
        """
        return pharmacy.query.filter_by(NAME=name).all()
    
@pharmacy_ns.route("/city:<string:city>", doc={"description": "List all pharmacies."})
class PharmaciesByCity(Resource):
    @pharmacy_ns.marshal_list_with(pharmacy_model)
    def get(self, city):
        """
        List pharmacies by city.
        """
        return pharmacy.query.filter_by(CITY=city).all()

