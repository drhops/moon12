from artful.models import Artist, D_ARTISTS, D_EVENTS, D_EXHIBIT
from moon12.urls import render_to_response


def root(request):
  lsArtists = list((k, v) for k, v in D_ARTISTS.iteritems())
  lsArtists.sort(key=lambda (k,v): v['display_order'])
  lsArtists = [k for (k, v) in lsArtists]
  
  dData = {
    'dCurrentExhibit': D_EXHIBIT,
    'dArtists': D_ARTISTS,
    'lsArtists': lsArtists,
    'dEvents': D_EVENTS, 
  }
  return render_to_response('home.html', dData)

def opening(request):
  return render_to_response('opening.html', {})

def about(request):
  return render_to_response('about.html', {})

def events(request):
  dData = {
    'dEvents': D_EVENTS,
    'dFutureEvents': dict((k,v) for k,v in D_EVENTS.iteritems() if v.get('future') == True),
    'dPastEvents': dict((k,v) for k,v in D_EVENTS.iteritems() if v.get('future') != True),
  }
  return render_to_response('events.html', dData)

def exhibits(request):
  sCurrentArtistId = D_EXHIBIT['artist']
  dData = {
    'dCurrentExhibit': D_EXHIBIT,
    'dCurrentArtist': D_ARTISTS[sCurrentArtistId],
    'sCurrentArtistId': sCurrentArtistId,
  }
  return render_to_response('exhibits.html', dData)

def artists(request):
  lsArtists = list((k, v) for k, v in D_ARTISTS.iteritems())
  lsArtists.sort(key=lambda (k,v): v['display_order'])
  lsArtists = [k for (k, v) in lsArtists]
  
  dData = {
    'dArtists': D_ARTISTS,
    'lsArtists': lsArtists,
  }
  return render_to_response('artists.html', dData)

def artist_bio(request, sArtistId):
  dArtist = D_ARTISTS.get(sArtistId, {})
  
  for dImage in dArtist.get('images', []):
    sSource = dImage.get('source')
    dImage.update({
      'source_image': '/static/images/artists/%s/album/%s' % (sArtistId, sSource),
      'source_thumb': '/static/images/artists/%s/album/thumbs/%s' % (sArtistId, sSource),
      'source_slide': '/static/images/artists/%s/album/slides/%s' % (sArtistId, sSource),
    })
  
  if not dArtist:
    pass
    # return 404    
  dData = {
    'dArtist': dArtist,
  }
  return render_to_response('artist/bio.html', dData)

def artist_gallery(request, sArtistId):
  dArtist = D_ARTISTS.get(sArtistId, {})
  
  for dImage in dArtist.get('images', []):
    sSource = dImage.get('source')
    dImage.update({
      'source_image': '/static/images/artists/%s/album/%s' % (sArtistId, sSource),
      'source_thumb': '/static/images/artists/%s/album/thumbs/%s' % (sArtistId, sSource),
      'source_slide': '/static/images/artists/%s/album/slides/%s' % (sArtistId, sSource),
    })
  
  if not dArtist:
    pass
    # return 404    
  dData = {
    'dArtist': dArtist,
  }
  return render_to_response('artist/gallery.html', dData)
