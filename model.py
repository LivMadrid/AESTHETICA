"""Model for User Data and Metadata for images"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() 

class User(db.Model):
    """a user"""

    __tablename__ = 'users'


    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    user_fname = db.Column(db.String, nullable=False)
    user_lname = db.Column(db.String, nullable=False)
    email = db.Column(db.string, nullable=False, unique=True)
    password = db.Column(db.string, nullable=False, unique=False)


    def __repr__(self):
        """Display user info"""
        return f'<User user_id={self.user_id} username={self.username} user_fname={self.user_fname} user_lname={self.user_lname} email={self.email}>'


class ImageMetaData(db.Model):
    """Image MetaData """

    __tablename__= 'image_metadata'

    image_id = db.Column(db.Integer)
    image_description = db.column(db.String)


    def __repr__(self):
        """Image MetaData"""
        return f'<ImageMetaData image_id={self.image_id} image_description={self.image_description}>'