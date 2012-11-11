# Create your views here.
from artful.models import Artist, D_ARTISTS
from moon12.urls import render_to_response


def root(request):
  return render_to_response('index.html', {})

def opening(request):
  return render_to_response('opening.html', {})

def about(request):
  return render_to_response('about.html', {})

def events(request):
  return render_to_response('events.html', {})

def exhibits(request):
  return render_to_response('exhibits.html', {})

def artists(request):
  dData = {
    'dArtists': D_ARTISTS,
  }
  return render_to_response('artists.html', dData)

def artist(request, sArtistName):
  #oArtist = Artist.objects.get(username=sArtistname)
  dArtist = D_ARTISTS.get(sArtistName)
  if not dArtist:
    pass
    # return 404
  dData = {
    'dArtist': dArtist,
  }
  return render_to_response('artist.html', dData)
