from django.urls import path
from . import views

urlpatterns = [
	#movie api
	path('movie', views.apiMovieOverview, name="api-overview-movie"),
	path('movie-list/', views.movieList, name="movie-list"),
	path('movie-detail/<str:pk>/', views.movieDetail, name="movie-detail"),
	path('movie-create/', views.movieCreate, name="movie-create"),

	path('movie-update/<str:pk>/', views.movieUpdate, name="movie-update"),
	path('movie-delete/<str:pk>/', views.movieDelete, name="movie-delete"),

	#seat api
	path('seat', views.apiSeatOverview, name="api-overview-seat"),
	path('seat-list/', views.seatList, name="seat-list"),
	path('seat-detail/<str:pk>/', views.seatDetail, name="seat-detail"),
	path('seat-create/', views.seatCreate, name="seat-create"),

	path('seat-update/<str:pk>/', views.seatUpdate, name="seat-update"),
	path('seat-delete/<str:pk>/', views.seatDelete, name="seat-delete"),
]
