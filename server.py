from flask import Flask, render_template, request, session, redirect, url_for, jsonify, flash
from flask_bootstrap import Bootstrap
from filters import datetimeformat, file_type
import requests 
import os
from resources import get_bucket

from model import db, User, Image, connect_to_db
import crud






app = Flask(__name__)
Bootstrap(app)
# login = LoginManager(app)
# login.init_app(app)
app.secret_key = 'pickles'
app.jinja_env.filters['datetimeformat'] = datetimeformat
app.jinja_env.filters['file_type'] = file_type
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userdata.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)




@app.route('/')
def homepage():
    """Display Homepage"""
    return render_template('homepage.html')

@app.route('/files')
def files():
    """Connects with S3 and displays (allfiles in S3) information on page"""
   
    my_bucket = get_bucket()
    #summaries get us the key(filename / date modified)
    summaries = my_bucket.objects.all()
    #s3 down - what to do --- for tests#### try s3.myburckst.all except s3 render dif. template service unavialble
    return render_template('files.html', my_bucket=my_bucket, files=summaries)

@app.route('/upload', methods=['POST'])
def upload_image():
    """Upload an image to S3"""
    #the dict will contain a key 'file' which is same on input form -- this is a FileStorage object from Werkzeug
    file = request.files['file']

   
    my_bucket = get_bucket()
    my_bucket.Object(file.filename).put(Body=file)

    # get_presigned_url('file')

    flash(f'Photo uploaded successfully!')
    return redirect(url_for('files'))

@app.route('/delete', methods=['POST'])
def delete_image():
    """Deletes an image off of S3"""

    key = request.form['key']
    
    my_bucket = get_bucket()
    my_bucket.Object(key).delete()

    flash(f'Photo deleted successfully!')
    return redirect(url_for('files'))


@app.route('/login')
def log_in():
    """Takes user to login page""" 
   
    return render_template('login.html')



@app.route('/login', methods=['POST'])
def login():
    """Get info from login form and return user profile"""
    print("########################################################################################")
    username = request.form.get('username')
    print(username)

    password = request.form.get('password')

    session['user'] = username  
    print(session['user'])

    if session['user']:
        flash(f'logged in as {username}')
        return render_template('user_image_repository.html', username=username)
    else:
        flash(f'incorrect username or password')
        return redirect('/login')
    # if current_user.is_authenticated:
    #     return redirct(url_for('/'))
    # form = LoginForm()
    # if form.validate_on_submit():
    #     user = get_user_from_username()
    #     if user is None or not user.check_password(form.passowrd.data):
    #         flash('Invaild username or password :(')
    #         return redirect(url_for('login'))
    #     login_user(user, remember=form.remember_me.data)
    #     return redirect(url_for('/'))
    # return render_template

# return 


@app.route('/register1')
def register_form():
    """Takes user to registration page""" 
   
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register_user():
    """Get user data from registration form"""

    print('###############################################################################')


    username = request.form.get('username')
    user_fname = request.form.get('fname')
    user_lname = request.form.get('lname')
    email = request.form.get('email')
    password_hash = request.form.get('password')

    # session['user'] = username
    # print(session['user'])
    
    if not crud.get_user_from_username(username):

        user = crud.create_user(username, user_fname, user_lname, email, password_hash)

        user.password(password)
        user.verify_password(password_hash)

        flash(f'Account Created! Please Login')

        return redirect("/login")
    
    else:
        
        if User.query.filter(User.username == username).all():
            flash(f'An account with this username already exists')
        
        return redirect("/register")

    # return render_template('register.html')
    # if existing_user:
    #     flash('An account with this username already exists . Login or Try again')
    #     return render_template('login.html')
    # else:
    #     user = crud.create_user(username, user_fname, user_lname, email, password_hash)
    #     flash('Account created! Please login ')
    #     return redirect('login.html')

# @app.route('/user_image_repository', methods=['GET', 'POST'])
# def user_image_repository():
#     """Displays user uploaded images"""

#     username = session['user']
#     user = crud.get_user_from_username(username)
#     print(user, username, '#####')

#     url = get_presigned_url()


#     return jsonify(url)


    # return render_template('user_image_repository.html', user=user)

# @app.route('/signout')
# def signout():
#     """User sign out of account"""

@app.route('/logout')
def logout():
    """Logs user out"""

    return redirect(url_for('/'))

if __name__ == "__main__":
    connect_to_db(app)
    app.run()
