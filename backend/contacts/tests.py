from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
import requests

class ContactsAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('contacts:get_contacts')
        self.mock_response = [
            {
                "id": 1,
                "name": "Leanne Graham",
                "username": "Bret",
                "email": "Sincere@april.biz",
                "address": {
                    "street": "Kulas Light",
                    "suite": "Apt. 556",
                    "city": "Gwenborough",
                    "zipcode": "92998-3874",
                    "geo": {
                        "lat": "-37.3159",
                        "lng": "81.1496"
                    }
                },
                "phone": "1-770-736-8031 x56442",
                "website": "hildegard.org",
                "company": {
                    "name": "Romaguera-Crona",
                    "catchPhrase": "Multi-layered client-server neural-net",
                    "bs": "harness real-time e-markets"
                }
            },
            # Add more mock contacts if needed
        ]

    def test_get_contacts_success(self):
        # Mock the requests.get call to return the mock_response
        requests.get = lambda url: MockResponse(self.mock_response, 200)
        
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(self.mock_response))
        self.assertEqual(response.data[0]['name'], self.mock_response[0]['name'])

    def test_get_contacts_content(self):
        # Mock the requests.get call to return the mock_response
        requests.get = lambda url: MockResponse(self.mock_response, 200)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for contact in response.data:
            self.assertIn('name', contact)
            self.assertIn('email', contact)
            self.assertIn('address', contact)
            self.assertIn('phone', contact)
            self.assertIn('website', contact)
            self.assertIn('company', contact)

class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data
