from flask_restx import Resource, Namespace
from ..authorization import authorizations, jwt_auth_required

from app.models.patient import patient_model
from app.schemas.patient import Patient


patient_ns = Namespace("patients", description="Patients data operations.")

patient = Patient()

@patient_ns.route("", doc={"description": "List all patients."})
class PatientsList(Resource):

    method_decorators = [jwt_auth_required]

    @patient_ns.doc(security="jsonWebToken")
    @patient_ns.marshal_list_with(patient_model)
    def get(self):
        """
        List all patients.
        """
        return patient.query.all()

@patient_ns.route("/patient/id:<string:uuid>", doc={"description": "Get a patient by id."})
class PatientById(Resource):

    method_decorators = [jwt_auth_required]

    @patient_ns.doc(security="jsonWebToken")
    @patient_ns.marshal_list_with(patient_model)
    def get(self, uuid):
        """
        Get a patient by UUID.
        """
        selected_patient = Patient.query.filter_by(UUID=uuid).first()
        return selected_patient

@patient_ns.route("/patient/first_name:<string:fName>", doc={"description": "Get patients by first name."})
class PatientByFirstName(Resource):

    method_decorators = [jwt_auth_required]

    @patient_ns.doc(security="jsonWebToken")
    @patient_ns.marshal_list_with(patient_model)
    def get(self, fName):
        """
        Get patients by first name.
        """
        selected_patient = patient.query.filter_by(FIRST_NAME=fName).all()
        return selected_patient

@patient_ns.route("/patient/full_name:<string:fName>&<string:lName>", doc={"description": "Get patients by full name."})
class PatientByFullName(Resource):

    method_decorators = [jwt_auth_required]

    @patient_ns.doc(security="jsonWebToken")
    @patient_ns.marshal_list_with(patient_model)
    def get(self, fName, lName):
        """
        Get patients by full name.
        """
        selected_patient = patient.query.filter_by(FIRST_NAME=fName, LAST_NAME=lName).all()
        return selected_patient

