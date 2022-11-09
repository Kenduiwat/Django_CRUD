from django.urls import path
#from .import views

from .views import ArtisteList, ArtisteDetail, SongList, SongDetail, LyricsList, LyricsDetail


urlpatterns = [
    path('Artiste/', ArtisteList.as_view()),
    path('Artiste/<int:pk>/', ArtisteDetail.as_view()),
    path('Song/', SongList.as_view()),
    path('Song/<int:pk>/', SongDetail.as_view()),
    path('Lyrics/', LyricsList.as_view()),
    path('Lyrics/<int:pk>/', LyricsDetail.as_view()),
]