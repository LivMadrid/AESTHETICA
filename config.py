import os 

#########RETRIEVES S3 SECRET ACCESS KEYS#############################
S3_BUCKET = os.environ.get('S3_BUCKET')
S3_KEY = os.environ.get('S3_KEY')
S3_SECRET = os.environ.get('S3_SECRET_ACCESS_KEY')

# DATABASE_URL = os.environ['DATABASE_URL']