
from rest_framework import serializers
from .models import User
from .models import Layer

class UserSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = User
        fields = ('id', 'identifier','name', 'email', 'region','date_created', 'date_modified')
        read_only_fields = ('id', 'date_created', 'date_modified')

class LayerSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Layer
        fields = ('id', 'identifier','name', 'hight', 'width','date_created', 'date_modified')
        read_only_fields = ('id', 'date_created', 'date_modified')