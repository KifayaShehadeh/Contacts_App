from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

@api_view(['GET'])
def get_contacts(request):
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    contacts = response.json()
    print(contacts)
    return Response(contacts)
