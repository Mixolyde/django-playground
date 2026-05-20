from django.shortcuts import render, get_object_or_404, redirect
from .models import Artist, Song
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

class SongListView(ListView):
    model = Song
    template_name = 'chordbook/song_list.html'
    context_object_name = 'songs'

class SongDetailView(DetailView):
    model = Song
    template_name = 'chordbook/song_detail.html'
    context_object_name = 'song'

class SongCreateView(CreateView):
    model = Song
    fields = ['title', 'artist', 'progression']
    template_name = 'chordbook/song_form.html'
    success_url = reverse_lazy('song-list')

class ArtistCreateView(CreateView):
    model = Artist
    fields = ['name']
    template_name = 'chordbook/artist_form.html'
    success_url = reverse_lazy('song-list')
