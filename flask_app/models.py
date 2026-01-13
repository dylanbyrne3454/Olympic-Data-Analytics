from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SurveyResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Integer
    age = db.Column(db.String(100), nullable=False) # String
    country = db.Column(db.String(100), nullable=False) # String
    gender = db.Column(db.String(20), nullable=False) # String
    watch_olympics = db.Column(db.String(20), nullable=False) # String
    summer_vs_winter = db.Column(db.String(20), nullable=False) # String
    athlete = db.Column(db.String(20), nullable=False)# String
    sport = db.Column(db.String(20), nullable=False) # String
    how_long = db.Column(db.Integer) # Integer
    become_olympian = db.Column(db.Boolean) # Boolean

    def __repr__(self):
        return f"Age : {self.age}, Gender: {self.gender}"