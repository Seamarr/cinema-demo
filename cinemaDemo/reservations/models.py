from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    movieImage = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title

class Seat(models.Model):
    label = models.CharField(max_length=3)
    corMovie = models.ForeignKey(Movie, on_delete= models.CASCADE, related_name="seats")
    isReserved = models.BooleanField(default=False)
    isSelected = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.label} for {self.corMovie}'
