from ..extensions import db

class User(db.Model):
    __tablename__ = "USERS"
    UUID = db.Column(db.String(256), primary_key=True, nullable=False)
    USERNAME = db.Column(db.String(50), nullable=False)
    PASSWORD = db.Column(db.String(256), nullable=False)

    def show_user_created(self):
        return {
            "UUID": self.UUID,
            "USERNAME": self.USERNAME
        }

