from app import db

class Client(db.Model):
    __tablename__ == "clients"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    
    email = db.Column(db.String(120))
