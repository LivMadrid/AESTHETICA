import pytest
from flask import Flask 
from server import app
# import unittest

####TESTING STRATEGY####
#ARRANGE
#ACT
#ASSERT


def test_always_passes():
    assert True

def test_always_fails(): 
    assert False 

def test_homepage():
    response = app.test_client().get('/')
    
    assert response.status_code == 200 
    
@pytest.fixture
def client():
    client = api.test_client()
    return client 

# import unittest
# from unittest import TestCase
# from server import app

# class AESTHETICATestCase(TestCase):

#     def setUp(self):


#     def test_homepage(self):
#         tester = app.client(self)
#         response = tester.get('/', content_type='html/text')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.data, b'AESTHETICA')


# if __name__ == '__main__':
#     unittest.main()