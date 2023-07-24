from django.test import TestCase, Client
from rest_framework import status
from django.urls import reverse
from Admin.models import Auth


class RegistrationAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def print_test_case_name(self):
        test_case_name = self._testMethodName
        print(f"Running test case: {test_case_name}")

    def test_registration_success(self):
        
        self.print_test_case_name()
        url = reverse('registration-signup')  

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
        self.print_test_case_name()
        url = reverse('registration-signup')  
        data = {
            'fname': 'John',
            'lname': 'Doe',
            'email': 'john.doe@example.com',
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertFalse(response.data['status'])

    def test_email_verification_fail(self):
        self.print_test_case_name()
        url = reverse('registration-signup')  
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

    def test_password_verification_fail(self):
        self.print_test_case_name()
        url = reverse('registration-signup')  
        data = {
            'fname': 'John',
            'lname': 'Doe',
            'email': 'john.doe@example.com',
            'password': '1234',
            'address': '123 Main St',
            'contact': '1234567890',
            'birthday': '2022-09-17',
            'gender': 'male',
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertFalse(response.data['status'])
