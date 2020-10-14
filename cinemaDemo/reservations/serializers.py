from rest_framework import serializers
from .models import Movie, Seat

class MovieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movie
		fields ='__all__'

class SeatSerializer(serializers.ModelSerializer):
	class Meta:
		model = Seat
		fields = '__all__'
