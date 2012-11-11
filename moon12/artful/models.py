'''
Models for Moon12.

Created on Oct 30, 2012
@author: Daniel Hopkins (drhops@gmail.com)
'''
from django.db import models

EMAIL_MAX_LENGTH = 25

D_ARTISTS = {
  'dbchang': {
    'full_name': 'Debbie Chang',
    'email': 'dbchang@gmail.com',
    'description': 'amazing watercolorist and oil texturizer, as well as incredible perfection and technical precision in drawing',
    'images': [
      {
        'title': 'dbc pic0',
        'description': 'gorgeous drop',
        'source': 'http://farm4.static.flickr.com/3261/2538183196_8baf9a8015.jpg',
        'source_small': 'http://farm4.static.flickr.com/3261/2538183196_8baf9a8015_s.jpg',
        'source_big': 'http://farm4.static.flickr.com/3261/2538183196_8baf9a8015_b.jpg',
      },
      {
        'title': 'dbc pic1',
        'description': 'gorgeous leaf',
        'source': 'http://farm3.static.flickr.com/2093/2538168854_f75e408156.jpg',
        'source_small': 'http://farm3.static.flickr.com/2093/2538168854_f75e408156_s.jpg',
        'source_big': 'http://farm3.static.flickr.com/2093/2538168854_f75e408156_b.jpg',
      },
      {
        'title': 'dbc pic2',
        'description': 'too good to be described',
        'source': 'http://farm4.static.flickr.com/3153/2538167690_c812461b7b.jpg',
        'source_small': 'http://farm4.static.flickr.com/3153/2538167690_c812461b7b_s.jpg',
        'source_big': 'http://farm4.static.flickr.com/3153/2538167690_c812461b7b_b.jpg',
      },
    ],
  },
  'drhops': {
    'full_name': 'Daniel Hopkins',
    'email': 'drhops@gmail.com',
    'description': 'Dan is a freaking godlike artist/coder',
    'images': [
      {
        'title': 'dhop pic0',
        'description': 'gorgeous drop',
        'source': 'http://farm4.static.flickr.com/3261/2538183196_8baf9a8015.jpg',
        'source_small': 'http://farm4.static.flickr.com/3261/2538183196_8baf9a8015_s.jpg',
        'source_big': 'http://farm4.static.flickr.com/3261/2538183196_8baf9a8015_b.jpg',
      },
      {
        'title': 'dhop pic1',
        'description': 'gorgeous leaf',
        'source': 'http://farm3.static.flickr.com/2093/2538168854_f75e408156.jpg',
        'source_small': 'http://farm3.static.flickr.com/2093/2538168854_f75e408156_s.jpg',
        'source_big': 'http://farm3.static.flickr.com/2093/2538168854_f75e408156_b.jpg',
      },
      {
        'title': 'dhop pic2',
        'description': 'too good to be described',
        'source': 'http://farm4.static.flickr.com/3153/2538167690_c812461b7b.jpg',
        'source_small': 'http://farm4.static.flickr.com/3153/2538167690_c812461b7b_s.jpg',
        'source_big': 'http://farm4.static.flickr.com/3153/2538167690_c812461b7b_b.jpg',
      },
    ],
  },
}

class Artist(models.Model):
  """Model to represent an artist."""
  full_name = models.CharField(max_length=255)
  username = models.CharField(max_length=25, db_index=True, unique=True, blank=True, null=True)
  email = models.EmailField(max_length=EMAIL_MAX_LENGTH, blank=True, null=True, db_index=True, unique=True)
  short_bio = models.CharField(max_length=255, blank=True, null=True)
  website = models.CharField(max_length=255, blank=True, null=True)
  last_modified = models.DateTimeField(null=True, editable=False)

  def get_first_name(self):
    return self.full_name.split(" ")[0]
