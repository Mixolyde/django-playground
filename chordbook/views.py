from django.shortcuts import render, get_object_or_404, redirect
from .models import Artist, Song
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy, reverse

class ArtistCreateView(CreateView):
    model = Artist
    fields = ['name']
    template_name = 'chordbook/artist_form.html'
    success_url = reverse_lazy('song-list')

class ArtistListView(ListView):
    model = Artist
    template_name = 'chordbook/artist_list.html'
    context_object_name = 'artists'
    queryset = Artist.objects.prefetch_related('songs').all()

class SongCreateView(CreateView):
    model = Song
    fields = ['artist', 'title', 'progression']
    template_name = 'chordbook/song_form.html'
    success_url = reverse_lazy('song-list')

class SongDetailView(DetailView):
    model = Song
    template_name = 'chordbook/song_detail.html'
    context_object_name = 'song'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from_source = self.request.GET.get('from')
        
        if from_source == 'artists':
            back_url = reverse('artist-list')
        else:
            back_url = reverse('song-list')
            
        context['back_url'] = back_url
        return context

class SongListView(ListView):
    model = Song
    template_name = 'chordbook/song_list.html'
    context_object_name = 'songs'
