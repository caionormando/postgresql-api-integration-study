from api.api import db


class Candidate(db.Model):
    __tablename__ = 'Candidates'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    job = db.Column(db.String())
    location = db.Column(db.Integer())
    name = db.Column(db.String())
    level = db.Column(db.Integer())

    def __init__(self, name, job, location, level) -> None:
        self.name = name
        self.job = job
        self.location = location
        self.level = level

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'job': self.job,
            'location': self.location,
            'name': self.name,
            'level': self.level
        }

