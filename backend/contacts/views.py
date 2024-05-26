from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests


@api_view(['GET'])
def get_contacts(request):
    print(request.headers)  # Debug line to print request headers
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    contacts = response.json()
    return Response(contacts)
