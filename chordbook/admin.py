from django.contrib import admin
from .models import Artist, Song

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'updated_at')
    list_filter = ('artist',)
    search_fields = ('title', 'artist__name')
