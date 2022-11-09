from django.db import models

# Create your models here.


class Artiste (models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Age = models.IntegerField()
'''
    def __str__(self):
        return self.FirstName + ' ' + self.LastName'''
    

class Song (models.Model):
    Artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    Title = models.CharField(max_length=255)
    Date_release = models.DateField()
    Likes = models.IntegerField()
    #Artiste_id = models.CharField(max_length=50)

    '''def __str__(self):
        return self.Artiste_id'''



class Lyrics (models.Model):
    Song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    Content = models.TextField()
    #Song_id = models.CharField(max_length=50)

    '''def __str__(self):
        return self.Song_id'''