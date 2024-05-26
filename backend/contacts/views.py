from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import logging

logger = logging.getLogger(__name__)


@api_view(['GET'])
def get_contacts(request):
    logger.debug(f"Request headers: {request.headers}")
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    contacts = response.json()
    return Response(contacts)
