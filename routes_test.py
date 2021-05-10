import pytest
from flask import Flask 
from server import app
import flask_unittest
import os
import unittest
from unittest import TestCase
from server import app



############################################TESTING STRATEGY#######################################################################
#ARRANGE
#ACT
# #ASSERT
############################################PYTESTS###############################################################################

def test_always_passes():
    """Test that pytest is working"""
    assert True

def test_always_fails(): 
    """Tests that pytest is working and will always FAIL"""
    assert False 

def test_homepage():
    """Tests homepage response""" 
    response = app.test_client().get('/')
    
    assert response.status_code == 200 
    
#TESTS TO IMPLEMENT 

#def login()
#TO DO
#auth tests integrate blueprint/ auth routes

# def test_upload()
    #TO DO - what happens when user doesn't choose a file to upload? what if they choose wrong file type? 
    #If they try to upload too large of files or too many

# def test_delete()
#TO DO 
# Ensures user can delete their images but not anyone else's 
# Tests if users can delete more than one image 

#def presigned url
#TO DO 
#Checks that users have credentials to temp. access S3 bucket 

#OTHER TO DO
# What if user can't reach S3 bucket
# What if image is unavailable
# 

@pytest.fixture
def client():
    client = api.test_client()
    return client 



# ### for @app.route('upload') what should be returned - a redirect back to bucket info
# errored our because I did not have secret key set yet 5.6.21

####################################UNITTESTS###############################################################################

# class TestCase(TestCase):
  
#     def create_app(self):
#         app.config.from_object('config.TestConfiguration')
#         return app 

    
    # def setUp(self):

    #     ctx = app.app_context()
    #     print(ctx)
    #     ctx.push()
        
    #     print(app)
    #     # with app.app_context():
        #     # current_app is available(you will see <Flask 'app'> in terminal)
        #     print(current_app)
        # # out of context manager - RuntimeError: Working outside of application context.
        # print(current_app)

    # def test_example(self):
    #     pass
    #     # app.config['TESTING'] = True
    #     # app.config['WTF_CSRF_ENABLED'] = False
    #     # self.app = app.test_client()


    # def test_homepage(self):
    #     # tester = app.client(self)
    #     response = self.client.get('/', content_type='html/text')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.data, b'AESTHETICA')


if __name__ == '__main__':
    unittest.main()