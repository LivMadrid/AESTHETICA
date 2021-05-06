from flask import Flask, render_template, request, session, redirect, jsonify
from flask_bootstrap import Bootstrap
import boto3
# import requests 
import os
from config import S3_BUCKET, S3_KEY, S3_SECRET
from filters import datetimeformat, file_type



s3_resource = boto3.resource(
    's3',
    aws_access_key_id=S3_KEY,
    aws_secret_access_key=S3_SECRET
)

app = Flask(__name__)
Bootstrap(app)
app.jinja_env.filters['datetimeformat'] = datetimeformat
app.jinja_env.filters['file_type'] = file_type





@app.route('/')
def homepage():
    """Display Homepage"""
    return render_template('homepage.html')

@app.route('/files')
def files():
    s3_resource = boto3.resource('s3')
    my_bucket = s3_resource.Bucket(S3_BUCKET)
    summaries = my_bucket.objects.all()
    #s3 down - what to do --- for tests#### try s3.myburckst.all except s3 render dif. template service unavialble
    return render_template('files.html', my_bucket=my_bucket, files=summaries)


# @app.route('/login')
# def login():
#     """User login page"""


# @app.route('/register')
# def register():
#     """User registration page"""

# @app.route('/user_image_repository')
# def user_image_repository():
#     """Displays user uploaded images"""

# @app.route('/signout')
# def signout():
#     """User sign out of account"""



if __name__ == "__main__":
    app.run()
