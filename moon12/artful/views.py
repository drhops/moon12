# Create your views here.
from artful.models import Artist
from moon12.urls import render_to_response

def root(request):
  return render_to_response('index.html', {})

def opening(request):
  return render_to_response('opening.html', {})

def artist(request, sArtistname):
  oArtist = Artist.objects.get(username=sArtistname)
  return render_to_response('artist.html', {'artist_full_name': oArtist.full_name})
