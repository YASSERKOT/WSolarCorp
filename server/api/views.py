from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse

from .serializers import UserSerializer
from .models import User

from .serializers import LayerSerializer
from .models import Layer

from .models import Regions

import json

class CreateUserView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def perform_create(self, serializer):
        """Save the post data when creating a new user."""
        serializer.save()

class CreateLayerView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Layer.objects.all()
    serializer_class = LayerSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new layer."""
        serializer.save()

class Layer_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Layer.objects.all()
    serializer_class = LayerSerializer

def showRegions(self):
    """ This method defines the display behaviour of our rest api for the regions from the database files"""
    lst_results = Regions.getAllRegions()
    return HttpResponse(lst_results, content_type="application/json")

def showFiltredRegions(self, arg):
    """ This method defines the display behaviour of our rest api for the regions from the database files"""
    lst_results = Regions.getRegion(arg)

    return HttpResponse(lst_results, content_type="application/json")