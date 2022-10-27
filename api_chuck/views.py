from django.shortcuts import render
from .services import  get_api_chuck
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class Apichuck(APIView):
    def get(self, request):
        data = get_api_chuck("https://api.chucknorris.io/jokes/random")
        print(len(data))
        return Response({'data':data})