from app import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    attempts = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "number": self.number,
            "attempts": self.attempts
        }
