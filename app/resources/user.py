from flask_restx import Resource, Namespace
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

from app.models.user import user_model, login_model
from app.schemas.user import User
from ..extensions import db

user_ns = Namespace("users", description="Users methods and authentications.")

user = User()

@user_ns.route("/register")
class Register(Resource):

    @user_ns.expect(login_model)
    def post(self):
        user_data = user_ns.payload
        users_count = db.session.query(User).count()
        user_id = f'USER{(users_count+1):04}'
        user_data['id'] = user_id
        new_user = User(
            UUID=user_id,
            USERNAME=user_data["USERNAME"],
            PASSWORD=generate_password_hash(user_data["PASSWORD"])
        )

        check_user = User.query.filter_by(USERNAME=user_data["USERNAME"]).first()
        if check_user:
            return{"error": "User already exists."}, 409

        db.session.add(new_user)
        db.session.commit()

        return new_user.show_user_created(), 201
    
@user_ns.route("/login")
class Login(Resource):

    @user_ns.expect(login_model)
    def post(self):
        user_data = user_ns.payload
        user = User.query.filter_by(USERNAME=user_data["USERNAME"]).first()
        if not user:
            return {"error": "User doesn't exist."}, 401
        if not check_password_hash(user.PASSWORD, user_data["PASSWORD"]):
            return{"error": "Incorrect password"}, 401
        return {"access_token": create_access_token(user.USERNAME)}
    
    