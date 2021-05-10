import boto3
import logging
from config import S3_BUCKET, S3_KEY, S3_SECRET
from botocore.exceptions import ClientError
import requests 
import json 

# s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

def get_s3_resource():
    """   """
    if S3_KEY and S3_SECRET:
        return boto3.resource(
            's3',
            aws_access_key_id=S3_KEY,
            aws_secret_access_key=S3_SECRET
        )
    else:
        return boto3.resource('s3')

def get_bucket():
    """Returns Bucket Object""" 
    s3_resource = get_s3_resource()
    return s3_resource.Bucket(S3_BUCKET)


####Code below only works if I set the .env variable for bucket_name as a string - however this makes the uploader/file page not work
#TO DO 
#FIX BELOW FOR SECURE ACCESS FUNCTIONALITY 

# bucket_name = 'aesthetica'

# file_key = "nostalgia.jpg"
# ###############################################################FOR ACCESS###################################################################
# ####################THIS DISPLAYS: the AWS access key in plain sight 
# def create_presigned_url(bucket_name, file_key , expiration=3600):
#     """Generates presigned URL for the S3 object 
#         PARAMS: bucket_name string
#                 object_in_bucket string
#                 expiration time in seconds the presigned URL will last
#                 sig. version string
#                 return - the presigned URL as a string -- else if errors return None
#     """
# # def get_presigned_url():
#     s3_client = boto3.client('s3',
#             aws_access_key_id=S3_KEY,
#             aws_secret_access_key=S3_SECRET
#             )
   
#     try:
#         response = s3_client.generate_presigned_url('get_object', 
#         Params={
#             'Bucket': bucket_name,
#             'Key': file_key ,  
#             #from file upload page?! ????????????????????????????????????????????????????????????????????????????????????????????????????????,
#         },
#         ExpiresIn=3600)
#         # for key in s3.list_objects(Bucket=S3_BUCKET, Prefix=file_key)['Contents']:
#         #    print(key['Key'])
#     except ClientError as e:
#             logging.error(e)
#             return None 
#         # response contains presigned URL
#     return response

# generated_signed_url = create_presigned_url(bucket_name, file_key, 3600)
# if generated_signed_url is not None:
#     response = requests.get(generated_signed_url)

# print(response)
# print(generated_signed_url)

# ##############################FOR UPLOADS#####################################################################################################
# def create_presigned_url(bucket_name, file_key, fields=None, conditions=None, expiration=3600):
      
#     s3_client = boto3.client('s3',
#                             aws_access_key_id=S3_KEY,
#                             aws_secret_access_key=S3_SECRET
#                             )
   
#     try:
#         response = s3_client.generate_presigned_post(bucket_name,
#                                                     file_key,
#                                                     Fields=fields,
#                                                     Conditions=conditions,
#                                                     ExpiresIn=expiration)

#     except ClientError as e:
#         logging.error(e)
#         return None 

#     return response

# # if response is None:
# #     exit(1)




# with open(file_key, 'rb') as f:
#     files = {'file': (file_key, f)}
#     http_response = requests.post(response['url'], data=response['fields'], files=files)
#     logging.info(f'File upload HTTP status code: {http_response.status_code}')
# THIS PRINTS THE AWS ACCESS KEY in plain sight !!!###WARNING###############################


# generated_presigned_post = create_presigned_url(bucket_name, file_key)
# print(generated_presigned_post)