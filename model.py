"""Model for User Data and Metadata for images"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import UserMixin, LoginManager


db = SQLAlchemy()
# login = LoginManager()



class User(db.Model):
    """a user"""

    __tablename__ = 'users'


    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    user_fname = db.Column(db.String(100), nullable=False)
    user_lname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    image_id = db.Column(db.Integer, db.ForeignKey('image.image_id'))

    user = db.relationship('Image', backref='image')

    # @login.user_loader
    # def load_user(user_id):
    #     return User.query.get(user_id)



    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        """Display user info"""
        return f'<User user_id={self.user_id} username={self.username} user_fname={self.user_fname} user_lname={self.user_lname} email={self.email}>'


class Image(db.Model):
    """Image MetaData """

    __tablename__= 'image'

    image_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image_filename = db.Column(db.String)
    image_description = db.Column(db.String)
    image_url = db.Column(db.String)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    
    
    # user = db.relationship('User', backref='users')

    def __repr__(self):
        """Image MetaData"""
        return f'<Image image_id={self.image_id} image_filename={self.image_filename} image_description={self.image_description} self.image_url={self.image_url}>'


# def test_user():
#     test_user = User(email='test@test.com', user_fname='test', user_lname='test', username='test1', password_hash='testpass')
#     db.session.add(test_user)
#     db.session.commit()
#     user = User.query.first()
#     return user 

# def test_image():
#     test_image = Image(image_name= 'test image', image_description='test image description', image_url=' https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/%22Evolution%22_and_life_in_vaporwave_flavours._%2848475685782%29.png/1200px-%22Evolution%22_and_life_in_vaporwave_flavours._%2848475685782%29.png')
#     db.session.add(test_image)
#     db.session.commit()
#     image = Image.query.first()
#     return image

def connect_to_db(flask_app, db_uri='postgresql:///userdata', echo=False):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')



if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
   