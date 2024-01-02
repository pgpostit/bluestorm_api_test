from flask_restx import Resource, Namespace
from ..authorization import authorizations, jwt_auth_required


from app.models.transaction import transaction_model
from app.schemas.transaction import Transaction
from app.schemas.patient import Patient
from app.schemas.pharmacy import Pharmacy

transaction_ns = Namespace("transactions", authorizations=authorizations, description="Transaction data between pharmacies and patients.")

transaction = Transaction()

@transaction_ns.route("", doc={"description": "List all transactions"})
class TransactionsList(Resource):
    method_decorators = [jwt_auth_required]

    @transaction_ns.doc(security="jsonWebToken")
    @transaction_ns.marshal_list_with(transaction_model)
    def get(self):
        """
        List all transactions.
        """
        return transaction.query.all()

@transaction_ns.route("/id:<string:uuid>", doc={"description": "Get a transaction by UUID"})
class TransactionsById(Resource):

    method_decorators = [jwt_auth_required]

    @transaction_ns.doc(security="jsonWebToken")
    @transaction_ns.marshal_with(transaction_model)
    def get(self, uuid):
        """
        Get a transaction by UUID.
        """
        return transaction.query.filter_by(UUID=uuid).first()

@transaction_ns.route("/amount/lower_than:<float:amount>", doc={"description": "Get transactions by amount"})
class TransactionsByEqualOrHigherAmount(Resource):

    method_decorators = [jwt_auth_required]

    @transaction_ns.doc(security="jsonWebToken")
    @transaction_ns.marshal_list_with(transaction_model)
    def get(self, amount):
        """
        Get transactions with amount greater than or equal to the specified value.
        """
        return transaction.query.filter(Transaction.AMOUNT >= amount).all()

@transaction_ns.route("/amount/higher_than:<float:amount>", doc={"description": "Get transactions by amount"})
class TransactionsByEqualOrHigherAmount(Resource):

    method_decorators = [jwt_auth_required]

    @transaction_ns.doc(security="jsonWebToken")
    @transaction_ns.marshal_list_with(transaction_model)
    def get(self, amount):
        """
        Get transactions with amount lower than or equal to the specified value.
        """
        return transaction.query.filter(Transaction.AMOUNT <= amount).all()
    
@transaction_ns.route("/patient/name:<string:fName>", doc={"description": "Get transactions by patient name"})
class TransactionsByPatientName(Resource):

    method_decorators = [jwt_auth_required]

    @transaction_ns.doc(security="jsonWebToken")
    @transaction_ns.marshal_list_with(transaction_model)
    def get(self, fName):
        """
        Get transactions by patient name.
        """
        return Transaction.query.join(Patient).filter(Patient.FIRST_NAME == fName).all()

@transaction_ns.route("/patient/id:<string:uuid>", doc={"description": "Get transactions by patient ID"})
class TransactionsByPatientId(Resource):

    method_decorators = [jwt_auth_required]

    @transaction_ns.doc(security="jsonWebToken")
    @transaction_ns.marshal_list_with(transaction_model)
    def get(self, uuid):
        """
        Get transactions by patient ID.
        """
        return Transaction.query.join(Patient).filter(Patient.UUID == uuid).all()

@transaction_ns.route("/pharmacy/id:<string:uuid>", doc={"description": "Get transactions by pharmacy ID"})
class TransactionsByPharmacyId(Resource):

    method_decorators = [jwt_auth_required]

    @transaction_ns.doc(security="jsonWebToken")
    @transaction_ns.marshal_list_with(transaction_model)
    def get(self, uuid):
        """
        Get transactions by pharmacy ID.
        """
        return Transaction.query.join(Pharmacy).filter(Pharmacy.UUID == uuid).all()

@transaction_ns.route("/pharmacy/name:<string:name>", doc={"description": "Get transactions by pharmacy name"})
class TransactionsByPharmacyName(Resource):

    method_decorators = [jwt_auth_required]

    @transaction_ns.doc(security="jsonWebToken")
    @transaction_ns.marshal_list_with(transaction_model)
    def get(self, name):
        """
        Get transactions by pharmacy name.
        """
        return Transaction.query.join(Pharmacy).filter(Pharmacy.NAME == name).all()

@transaction_ns.route("/pharmacy/city:<string:city>", doc={"description": "Get transactions by pharmacy city"})
class TransactionsByCity(Resource):

    method_decorators = [jwt_auth_required]

    @transaction_ns.doc(security="jsonWebToken")
    @transaction_ns.marshal_list_with(transaction_model)
    def get(self, city):
        """
        Get transactions by pharmacy city.
        """
        return Transaction.query.join(Pharmacy).filter(Pharmacy.CITY == city).all()

