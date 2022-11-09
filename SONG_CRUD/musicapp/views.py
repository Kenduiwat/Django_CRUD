from rest_framework import generics

from .models import Artiste, Song , Lyrics
from .serializers import ArtisteSerializer, SongSerializer , LyricsSerializer

class ArtisteList(generics.ListCreateAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer
    
    '''def get_queryset(self):
        queryset = Artiste.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter (itemlocation=location)
        return queryset'''
    

class ArtisteDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArtisteSerializer
    queryset = Artiste.objects.all()
        
        
class SongList(generics.ListCreateAPIView):
    serializer_class = SongSerializer
    queryset = Song.objects.all()
    
    
class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SongSerializer
    queryset = Song.objects.all()
    
    
    
class LyricsList(generics.ListCreateAPIView):
    serializer_class = LyricsSerializer
    queryset = Lyrics.objects.all()
    
class LyricsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LyricsSerializer
    queryset = Lyrics.objects.all()
    