import pytest
from .. import create_app, db
import json

@pytest.fixture
def app():
    app = create_app("sqlite:///:memory:")

    with app.app_context():
        db.create_all()

    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def register_user(client, username, password):
    url = "/users/register"
    headers = {"Content-Type": "application/json"}
    body = json.dumps({"USERNAME": username, "PASSWORD": password})
    response = client.post(url, headers=headers, data=body)
    assert response.status_code == 201

def login_user(client, username, password):
    url = "/users/login"
    headers = {"Content-Type": "application/json"}
    body = json.dumps({"USERNAME": username, "PASSWORD": password})
    response = client.post(url, headers=headers, data=body)
    assert response.status_code == 200
    return response.json.get('access_token')

@pytest.fixture
def authenticated_user_token(client):
    register_user(client, "testuser", "testpassword")
    token = login_user(client, "testuser", "testpassword")
    return token

class TestPatients:
    def test_list_all_patients(self, client, authenticated_user_token):
        url = "/patients"
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {authenticated_user_token}"}
        response = client.get(url, headers=headers)
        assert response.status_code == 200

    def test_get_patient_by_id(self, client, authenticated_user_token):
        patient_id = "PATIENT0001"
        url = f"/patients/patient/id:{patient_id}"
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {authenticated_user_token}"}
        response = client.get(url, headers=headers)
        assert response.status_code == 200

    def test_get_patients_by_first_name(self, client, authenticated_user_token):
        first_name = "PAULO"
        url = f"/patients/patient/first_name:{first_name}"
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {authenticated_user_token}"}
        response = client.get(url, headers=headers)
        assert response.status_code == 200

    def test_get_patients_by_full_name(self, client, authenticated_user_token):
        full_name = "PAULO&GARCIA"
        url = f"/patients/patient/full_name:{full_name}"
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {authenticated_user_token}"}
        response = client.get(url, headers=headers)
        assert response.status_code == 200

class TestPharmacies:
    def test_list_all_pharmacies(self, client):
        url = "/pharmacies"
        headers = {"Content-Type": "application/json"}
        response = client.get(url, headers=headers)
        assert response.status_code == 200

    def test_get_pharmacy_by_id(self, client):
        pharmacy_id = "PHARM0001"
        url = f"/pharmacies/pharmacy/id:{pharmacy_id}"
        headers = {"Content-Type": "application/json"}
        response = client.get(url, headers=headers)
        assert response.status_code == 200

    def test_get_pharmacies_by_name(self, client):
        pharmacy_name = "DROGASIL"
        url = f"/pharmacies/pharmacy/name:{pharmacy_name}"
        headers = {"Content-Type": "application/json"}
        response = client.get(url, headers=headers)
        assert response.status_code == 200

    def test_list_pharmacies_by_city(self, client):
        city = "CAMPINAS"
        url = f"/pharmacies/city:{city}"
        headers = {"Content-Type": "application/json"}
        response = client.get(url, headers=headers)
        assert response.status_code == 200

class TestTransactions:
    def test_list_all_transactions(self, client, authenticated_user_token):
        url = "/transactions"
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {authenticated_user_token}"}
        response = client.get(url, headers=headers)
        assert response.status_code == 200

    def test_get_transaction_by_uuid(self, client, authenticated_user_token):
        transaction_uuid = "TRAN0001"
        url = f"/transactions/id:{transaction_uuid}"
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {authenticated_user_token}"}
        response = client.get(url, headers=headers)
        assert response.status_code == 200

    def test_get_transactions_by_amount_lower_than(self, client, authenticated_user_token):
        amount = 3.5
        url = f"/transactions/amount/lower_than:{amount}"
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {authenticated_user_token}"}
        response = client.get(url, headers=headers)
        assert response.status_code == 200

    def test_get_transactions_by_amount_higher_than(self, client, authenticated_user_token):
        amount = 3.5
        url = f"/transactions/amount/higher_than:{amount}"
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {authenticated_user_token}"}
        response = client.get(url, headers=headers)
        assert response.status_code == 200

    def test_get_transactions_by_patient_name(self, client, authenticated_user_token):
        patient_name = "PAULO"
        url = f"/transactions/patient/name:{patient_name}"
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {authenticated_user_token}"}
        response = client.get(url, headers=headers)
        assert response.status_code == 200

    def test_get_transactions_by_patient_id(self, client, authenticated_user_token):
        patient_id = "PATIENT0001"
        url = f"/transactions/patient/id:{patient_id}"
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {authenticated_user_token}"}
        response = client.get(url, headers=headers)
        assert response.status_code == 200

    def test_get_transactions_by_pharmacy_id(self, client, authenticated_user_token):
        pharmacy_id = "PHARM0001"
        url = f"/transactions/pharmacy/id:{pharmacy_id}"
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {authenticated_user_token}"}
        response = client.get(url, headers=headers)
        assert response.status_code == 200

    def test_get_transactions_by_pharmacy_name(self, client, authenticated_user_token):
        pharmacy_name = "DROGASIL"
        url = f"/transactions/pharmacy/name:{pharmacy_name}"
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {authenticated_user_token}"}
        response = client.get(url, headers=headers)
        assert response.status_code == 200

    def test_get_transactions_by_pharmacy_city(self, client, authenticated_user_token):
        pharmacy_city = "CAMPINAS"
        url = f"/transactions/pharmacy/city:{pharmacy_city}"
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {authenticated_user_token}"}
        response = client.get(url, headers=headers)
        assert response.status_code == 200

class TestUsers:
    def test_register_user(self, client):
        register_user(client, "novousuario", "novasenha")

    def test_user_login(self, client):
        register_user(client, "usuarioexistente", "senhacorreta")
        login_user(client, "usuarioexistente", "senhacorreta")
