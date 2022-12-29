from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from AppRestFramework.models import Post
from AppRestFramework.api.serializers import PostSerializer
import requests
import time
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer


@api_view(('GET',))

def external_api_view(request):
    if request.method == "GET":
        attempt_num = 0  # keep track of how many times we've retried
        while attempt_num ==0 :
            url = 'https://la2.api.riotgames.com/tft/league/v1/challenger?api_key=RGAPI-ceaca4d3-8752-4c9f-ac15-37d733866bd5'

            r = requests.get(url)
            if r.status_code == 200:
                data = r.json()
                print(r.json())
                return Response(data, status=status.HTTP_200_OK)
            else:
                attempt_num += 1
                # You can probably use a logger to log the error here
                time.sleep(5)  # Wait for 5 seconds before re-trying
        return Response({"error": "Request failed"}, status=r.status_code)
    else:
        return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)
