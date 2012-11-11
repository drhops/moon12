# Create your views here.
from artful.models import Artist, D_ARTISTS
from moon12.urls import render_to_response


def root(request):
  return render_to_response('index.html', {})

def opening(request):
  return render_to_response('opening.html', {})

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
