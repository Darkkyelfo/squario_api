from django.contrib.sites import requests
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def send_command(request):
    response = requests.get('http://example.com')
    return Response(response)
