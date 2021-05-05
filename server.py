from flask import Flask, render_template, request, session, redirect, jsonify
from flask_bootstrap import Bootstrap
import boto3
from config import S3_BUCKET, S3_KEY, S3_SECRET

s3_resource = boto3.resource(
    's3',
    aws_access_key_id=S3_KEY
    aws_secret_access_key=S3_SECRETS
)

app = Flask(__name__)
Bootstrap(app)





@app.route('/')
def homepage():
    """Display Homepage"""
    return render_template('homepage.html')

# @app.route('/login')
# def login():
#     """User login page"""

# @app.route('/signup')
# def signup():
#     """User signup page"""

# @app.route('/user_image_repository')
# def user_image_repository():
#     """Displays user uploaded images"""

# @app.route('/signout')
# def signout():
#     """User sign out of account"""



if __name__ == "__main__":
    app.run()
