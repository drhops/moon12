# This Python file uses the following encoding: utf-8
'''
Models for Moon12.

Created on Oct 30, 2012
@author: Daniel Hopkins (drhops@gmail.com)
'''
from django.contrib import admin
from django.db import models

EMAIL_MAX_LENGTH = 25

D_EVENTS = {
  'soap-making': {
    'title': u'手工皂講座',
    'description': u'山月桂工作坊將在11/24於夢12美學空間舉辦手工皂講座，屆時有興趣的朋友都將可以免費參加，先來一睹為快，看看這些彷彿藝術品一般的手工皂吧！',
    'dates': '11/24',
    'image': '/static/images/events/soap.jpg',
    'future': True,
  },
  'opening': {
    'title': u'夢12開幕',
    'description': u'十月二十七日下午三點夢12開幕了，當天超過百位好朋友從紐澤西、成都、台中、新竹趕來，帶來一場溫馨的聚會，各個角落散發著濃郁的友情。在這一刻，我們的夢想慢慢開始藴釀...',
    'dates': '10/27',
    'image': '/static/images/events/opening.jpg',
    'future': False,
  },
}

D_EXHIBIT = {
  'title': u'金權盛世-熱帶雨林篇',
  'subtitle': u'藝術家洪天宇個展',
  'dates': '11/10 - 12/10',
  'description': u'藝術家洪天宇個展：金權盛世-熱帶雨林篇，將於11.10（六）下午三點開幕，藝術家現場親自導覧，展期一個月。',
  'image': '/static/images/exhibits/mcdonalds.jpg',
  'artist': 'hong-tian-yu',
}


class Artist(models.Model):
  """Model to represent an artist."""
  username = models.CharField(max_length=25, db_index=True, unique=True, blank=True, null=True)
  full_name = models.CharField(max_length=255)
  description = models.TextField()
  display_order = models.IntegerField()
  home_image = models.CharField(max_length=255)
  last_modified = models.DateTimeField(null=True, editable=False)

  def __unicode__(self):
    return self.full_name
  
  def get_first_name(self):
    return self.full_name.split(" ")[0]


class Image(models.Model):
  def __unicode__(self):
    return '%s | %s' % (self.artist.full_name, self.title)
  
  artist = models.ForeignKey('Artist')
  description = models.TextField()
  title = models.CharField(max_length=255)
  medium = models.CharField(max_length=255)
  year = models.CharField(max_length=255)
  dimensions = models.CharField(max_length=255)
  source = models.CharField(max_length=255)
  

admin.site.register(Artist)
admin.site.register(Image) 
