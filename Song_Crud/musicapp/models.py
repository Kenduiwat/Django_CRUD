from django.db import models

# Create your models here.


class Artiste (models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Age = models.IntegerField()

    

class Song (models.Model):
    Artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    Title = models.CharField(max_length=255)
    Date_release = models.DateField()
    Likes = models.IntegerField()
    #Artiste_id = models.CharField(max_length=50)




class Lyrics (models.Model):
    Song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    Content = models.TextField()
    #Song_id = models.CharField(max_length=50)
