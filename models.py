from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Dog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_path = db.Column(db.String(256), nullable=False)
    detected_at = db.Column(db.DateTime, default=datetime.utcnow)
    location = db.Column(db.String(128), nullable=True)
    count = db.Column(db.Integer, default=1)
    health = db.Column(db.String(64), default="Unknown")
    age = db.Column(db.String(32), default="Unknown")
    size = db.Column(db.String(32), default="Unknown")
    adopted = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "image_path": self.image_path,
            "detected_at": self.detected_at.isoformat(),
            "location": self.location,
            "count": self.count,
            "health": self.health,
            "age": self.age,
            "size": self.size,
            "adopted": self.adopted
        }
