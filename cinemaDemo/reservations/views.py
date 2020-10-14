from django.shortcuts import render

from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieSerializer, SeatSerializer

from .models import Movie, Seat
# Create your views here.

@api_view(['GET'])
def apiMovieOverview(request):
	api_urls = {
		'List':'/movie-list/',
		'Detail View':'/movie-detail/<str:pk>/',
		'Create':'/movie-create/',
		'Update':'/movie-update/<str:pk>/',
		'Delete':'/movie-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def movieList(request):
	movies = Movie.objects.all().order_by('-id')
	serializer = MovieSerializer(movies, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def movieDetail(request, pk):
	movies = Movie.objects.get(id=pk)
	serializer = MovieSerializer(movies, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def movieCreate(request):
	serializer = MovieSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def movieUpdate(request, pk):
	movie = Movie.objects.get(id=pk)
	serializer = MovieSerializer(instance=movie, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def movieDelete(request, pk):
	movie = Movie.objects.get(id=pk)
	movie.delete()

	return Response('Item succsesfully delete!')

#seat api
@api_view(['GET'])
def apiSeatOverview(request):
	api_urls = {
		'List':'/seat-list/',
		'Detail View':'/seat-detail/<str:pk>/',
		'Create':'/seat-create/',
		'Update':'/seat-update/<str:pk>/',
		'Delete':'/seat-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def seatList(request):
	seats = Seat.objects.all().order_by('-id')
	serializer = SeatSerializer(seats, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def seatDetail(request, pk):
	seats = Seat.objects.get(id=pk)
	serializer = SeatSerializer(seats, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def seatCreate(request):
	serializer = SeatSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def seatUpdate(request, pk):
	seat = Seat.objects.get(id=pk)
	serializer = SeatSerializer(instance=seat, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def seatDelete(request, pk):
	seat = Seat.objects.get(id=pk)
	seat.delete()

	return Response('Item succsesfully delete!')
