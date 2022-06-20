import imp
from app import db

class Joke(db.Model):
    __tablename__ = 'joke'

    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.Text(), nullable = False)
    type = db.Column(db.String(256), nullable = False)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
    
    def update(self, description):
        self.description = description
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @staticmethod  
    def get_by_id(id):
        return Joke.query.get(id)