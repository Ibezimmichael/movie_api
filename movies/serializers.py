from rest_framework import serializers
from .models import MovieData


class MovieSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = MovieData
        fields = '__all__'

