from . import db
from datetime import datetime

class Movies(db.Model):
    __tablename__ = 'movies'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    poster = db.Column(db.String(200)) 
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, title, description, poster, created_at):
        self.title = title
        self.description = description
        self.poster = poster
        self.created_at = created_at 

    def photo_path(self):
        if self.photo:
            return f'static/uploads/{self.photo}'
        else:
            return None
        
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True
    
    def is_annonymous(self):
        return False
    
    def get_id(self):
        try:
            return #unicode(self, id) #python 2 support
        except NameError:
            return str(self.id) #python 3 support
        
    def __repr__(self):
        return f'<Movie {self.id} - {self.title}>'