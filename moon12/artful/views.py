from artful.models import Artist, D_EVENTS, D_EXHIBIT, Image
from moon12.urls import render_to_response
from collections import OrderedDict

def getArtistsData():
  lmArtists = Artist.objects.all()

  dArtists = {}
  for mArtist in lmArtists:
    mArtist.images = Image.objects.filter(artist=mArtist)
    mArtist.home_image_70 = appendBeforeFileExtension(mArtist.home_image, 70)
    mArtist.home_image_250 = appendBeforeFileExtension(mArtist.home_image, 250)
    dArtists[mArtist.username] = mArtist

  return dArtists

def appendBeforeFileExtension(filename, appendage):
	lsPieces = filename.rsplit('.', 2)
	lsPieces[0] = "%s%s" % (lsPieces[0], appendage)
	return '.'.join(lsPieces)

def root(request):
  dArtists = getArtistsData()
  lsArtists = [mArtist.username for mArtist in Artist.objects.all().order_by('display_order')]

  dData = {
    'dCurrentExhibit': D_EXHIBIT,
    'dCurrentExhibitArtist': dArtists[D_EXHIBIT['artist']],
    'dArtists': dArtists,
    'lsArtists': lsArtists,
    'dEvents': OrderedDict(sorted(D_EVENTS.items(), key= lambda x: x[1]['dates'], reverse=True)),
  }
  return render_to_response('home.html', dData)

def opening(request):
  return render_to_response('opening.html', {})

def about(request):
  return render_to_response('about.html', {})

def events(request):
  dFutureEvents = dict((k,v) for k,v in D_EVENTS.iteritems() if v.get('future') == True)
  dPastEvents = dict((k,v) for k,v in D_EVENTS.iteritems() if v.get('future') != True)
  dData = {
    'dEvents': OrderedDict(sorted(D_EVENTS.items(), key= lambda x: x[1]['dates'], reverse=True)),
    'dFutureEvents': OrderedDict(sorted(dFutureEvents.items(), key= lambda x: x[1]['dates'], reverse=True)),
    'dPastEvents': OrderedDict(sorted(dPastEvents.items(), key= lambda x: x[1]['dates'], reverse=True)),
  }
  return render_to_response('events.html', dData)

def exhibits(request):
  sCurrentArtistId = D_EXHIBIT['artist']
  dData = {
    'dCurrentExhibit': D_EXHIBIT,
    'dCurrentArtist': Artist.objects.get(username=sCurrentArtistId),
    'sCurrentArtistId': sCurrentArtistId,
  }
  return render_to_response('exhibits.html', dData)

def artists(request):
  dArtists = getArtistsData()
  lsArtists = [mArtist.username for mArtist in Artist.objects.all().order_by('display_order')]

  dData = {
    'dArtists': dArtists,
    'lsArtists': lsArtists,
  }
  return render_to_response('artists.html', dData)

def getArtistData(sArtistId):
  mArtist = Artist.objects.get(username=sArtistId)
  lmImages = Image.objects.filter(artist=mArtist)

  for mImage in lmImages:
    sSource = mImage.source
    mImage.source_image = '/static/images/artists/%s/album/%s' % (sArtistId, sSource)
    mImage.source_thumb = '/static/images/artists/%s/album/thumbs/%s' % (sArtistId, sSource)
    mImage.source_slide = '/static/images/artists/%s/album/slides/%s' % (sArtistId, sSource)

  mArtist.images = lmImages
  return mArtist

def event_photos(request, sEventId):
  dEvent = D_EVENTS.get(sEventId)
  dEvent['ldImages'] = []
  for image in dEvent.get('images'):
  	dEvent['ldImages'].append({
  	  'image': image.replace('/album/slides', ''),
  	  'slide': image,
  	})

  dData = {
    'dEvent': dEvent,
    'sEventId': sEventId,
  }
  return render_to_response('event/photos.html', dData)

def artist_statement(request, sArtistId):
  dData = {
    'dArtist': getArtistData(sArtistId),
  }
  return render_to_response('artist/statement.html', dData)

def artist_bio(request, sArtistId):
  dData = {
    'dArtist': getArtistData(sArtistId),
  }
  return render_to_response('artist/bio.html', dData)

def artist_essays(request, sArtistId):
  dData = {
    'dArtist': getArtistData(sArtistId),
  }
  return render_to_response('artist/essays.html', dData)

def artist_videos(request, sArtistId):
  dData = {
    'dArtist': getArtistData(sArtistId),
  }
  return render_to_response('artist/videos.html', dData)

def artist_gallery(request, sArtistId):
  dData = {
    'dArtist': getArtistData(sArtistId),
  }
  return render_to_response('artist/gallery.html', dData)
