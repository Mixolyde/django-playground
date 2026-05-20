from django.urls import path
from . import views

urlpatterns = [
    path('', views.SongListView.as_view(), name='song-list'),
    path('artists/', views.ArtistListView.as_view(), name='artist-list'),
    path('song/<int:pk>/', views.SongDetailView.as_view(), name='song-detail'),
    path('song/add/', views.SongCreateView.as_view(), name='song-add'),
    path('artist/add/', views.ArtistCreateView.as_view(), name='artist-add'),
]
