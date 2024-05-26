from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.views.decorators.csrf import csrf_exempt
import logging

# contacts/views.py
logger = logging.getLogger(__name__)

from django.http import HttpResponse

@api_view(['GET', 'OPTIONS'])
def get_contacts(request):
    if request.method == 'OPTIONS':
        response = HttpResponse()
        response['Allow'] = 'GET, OPTIONS'
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        return response

    logger.debug(f"Request headers: {request.headers}")
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    contacts = response.json()
    return Response(contacts)
