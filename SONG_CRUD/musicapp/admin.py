from django.contrib import admin

# Register your models here.

from .models import Song, Artiste, Lyrics

admin.site.register(Artiste)
admin.site.register(Song)
admin.site.register(Lyrics)
