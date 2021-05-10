from model import db, User, Image, connect_to_db
"""Helper functions to access database using SQLAlchemy"""


########################################USER########################################################
def create_user(username, user_fname, user_lname, email, password_hash):
    """Create new user"""

    user = User(username=username,
            user_fname=user_fname,
            user_lname=user_lname,
            email=email,
            password_hash=password_hash)

        
    db.session.add(user)
    db.session.commit()  

    return user      

def get_all_users():
    """Retrieve all users in db"""

    return User.query.all()

def get_user_from_email():
    """Retrieve user with email"""

    return User.query.filter(User.email == email).first()

def get_user_from_username(username):
    """Retrieve user with username"""

    return User.query.filter(User.username == username).first()

def get_user_from_userid():
    """Retrieve user with user id"""

    return User.quey.filter(User.user_id == user_id).first 

####################################IMAGE#############################################################

def create_image(image_filename, image_description, image_url):
    """Create new image to be stored"""

    image = Image(image_filename=image_filename,
                  image_description=image_description,
                  image_url=image_url)
    
    db.session.add(image)
    db.session.commit()

def get_all_images():
    """Retrieve all images from db"""

    return Image.query.all()

def get_image_from_id():
    """Retrieve image from id"""
    
    return Image.query.filter(Image.image_id == image_id).first

def get_image_from_filename():
    """Retrieve image by filename"""

    return Image.query.filter(Image.image_filename == image_filename).first

def get_image_from_url():
    """Retrieve image by url"""
    
    return Image.query.filter(Image.image_url == image_url).first

if __name__ == '__main__':
    from server import app
    connect_to_db(app)