from django.test import TestCase, Client
from rest_framework import status
from django.urls import reverse
from Admin.models import Auth  




class RegistrationAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_registration_success(self):
        # Test successful registration
        url = reverse('registration')  

        data = {
            'fname': 'John',
            'lname': 'Doe',
            'email': 'john.doe@example.com',
            'password': 'testpassword',
            'address': '123 Main St',
            'contact': '1234567890',
            'birthday': '2022-09-17',
            'gender': 'male',
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data['status'])
        self.assertEqual(response.data['message'], 'Account Created Successfully')




    def test_registration_validation_error(self):
        # Test registration with missing required fields
        url = reverse('registration')  
        data = {
            'fname': 'John',
            'lname': 'Doe',
            # Missing some required fields
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertFalse(response.data['status'])


    
    def test_email_verification_fail(self):
        # Test registration with invalid email address
        url = reverse('registration')  
        data = {
            'fname': 'John',
            'lname': 'Doe',
            'email': 'john.doe',
            'password': 'testpassword',
            'address': '123 Main St',
            'contact': '1234567890',
            'birthday': '2022-09-17',
            'gender': 'male',
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertFalse(response.data['status'])
