from django.shortcuts import render
from rest_framework import generics

from .serializers import UserSerializer
from .models import User

from .serializers import LayerSerializer
from .models import Layer

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

class CreateRegionsView(generics.ListCreateAPIView):
    """ This class defines the create behaviour of our rest api for the regions from the database files"""
    #queryset = os.path.curdir()

# This is the view for the Home page where we are going to 
#class HomePageView(TemplateView):
#    def get(self, request, **kwargs):
#        return render(request, 'index.html', context=None)