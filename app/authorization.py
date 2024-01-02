from flask_jwt_extended import jwt_required

authorizations = {
    "jsonWebToken": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization"
    }
}

jwt_auth_required = jwt_required()

