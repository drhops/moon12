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
    'future': False,
    'images': [
'/static/images/events/soap-making/album/slides/IMG_8326.JPG',
'/static/images/events/soap-making/album/slides/IMG_8327.JPG',
'/static/images/events/soap-making/album/slides/IMG_8328.JPG',
'/static/images/events/soap-making/album/slides/IMG_8329.JPG',
'/static/images/events/soap-making/album/slides/IMG_8330.JPG',
'/static/images/events/soap-making/album/slides/IMG_8331.JPG',
'/static/images/events/soap-making/album/slides/IMG_8332.JPG',
'/static/images/events/soap-making/album/slides/IMG_8333.JPG',
'/static/images/events/soap-making/album/slides/IMG_8334.JPG',
'/static/images/events/soap-making/album/slides/IMG_8335.JPG',
'/static/images/events/soap-making/album/slides/IMG_8336.JPG',
'/static/images/events/soap-making/album/slides/IMG_8337.JPG',
'/static/images/events/soap-making/album/slides/IMG_8338.JPG',
'/static/images/events/soap-making/album/slides/IMG_8339.JPG',
'/static/images/events/soap-making/album/slides/IMG_8340.JPG',
'/static/images/events/soap-making/album/slides/IMG_8341.JPG',
'/static/images/events/soap-making/album/slides/IMG_8342.JPG',
'/static/images/events/soap-making/album/slides/IMG_8343.JPG',
'/static/images/events/soap-making/album/slides/IMG_8344.JPG',
'/static/images/events/soap-making/album/slides/IMG_8345.JPG',
'/static/images/events/soap-making/album/slides/IMG_8346.JPG',
'/static/images/events/soap-making/album/slides/IMG_8347.JPG',
'/static/images/events/soap-making/album/slides/IMG_8348.JPG',
'/static/images/events/soap-making/album/slides/IMG_8349.JPG',
'/static/images/events/soap-making/album/slides/IMG_8350.JPG',
'/static/images/events/soap-making/album/slides/IMG_8351.JPG',
'/static/images/events/soap-making/album/slides/IMG_8352.JPG',
'/static/images/events/soap-making/album/slides/IMG_8353.JPG',
'/static/images/events/soap-making/album/slides/IMG_8354.JPG',
'/static/images/events/soap-making/album/slides/IMG_8355.JPG',
'/static/images/events/soap-making/album/slides/IMG_8356.JPG',
'/static/images/events/soap-making/album/slides/IMG_8357.JPG',
'/static/images/events/soap-making/album/slides/IMG_8358.JPG',
'/static/images/events/soap-making/album/slides/IMG_8359.JPG',
'/static/images/events/soap-making/album/slides/IMG_8360.JPG',
'/static/images/events/soap-making/album/slides/IMG_8361.JPG',
'/static/images/events/soap-making/album/slides/IMG_8362.JPG',
'/static/images/events/soap-making/album/slides/IMG_8363.JPG',
'/static/images/events/soap-making/album/slides/IMG_8364.JPG',
'/static/images/events/soap-making/album/slides/IMG_8365.JPG',
'/static/images/events/soap-making/album/slides/IMG_8366.JPG',
'/static/images/events/soap-making/album/slides/IMG_8367.JPG',
'/static/images/events/soap-making/album/slides/IMG_8368.JPG',
'/static/images/events/soap-making/album/slides/IMG_8369.JPG',
'/static/images/events/soap-making/album/slides/IMG_8370.JPG',
'/static/images/events/soap-making/album/slides/IMG_8371.JPG',
'/static/images/events/soap-making/album/slides/IMG_8372.JPG',
'/static/images/events/soap-making/album/slides/IMG_8373.JPG',
'/static/images/events/soap-making/album/slides/IMG_8374.JPG',
'/static/images/events/soap-making/album/slides/IMG_8375.JPG',
'/static/images/events/soap-making/album/slides/IMG_8378.JPG',
'/static/images/events/soap-making/album/slides/IMG_8379.JPG',
'/static/images/events/soap-making/album/slides/IMG_8380.JPG',
'/static/images/events/soap-making/album/slides/IMG_8381.JPG',
'/static/images/events/soap-making/album/slides/IMG_8382.JPG',
'/static/images/events/soap-making/album/slides/IMG_8383.JPG',
'/static/images/events/soap-making/album/slides/IMG_8384.JPG',
'/static/images/events/soap-making/album/slides/IMG_8385.JPG',
	],
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
  'image': u'/static/images/exhibits/洪天宇_滴血的歡樂.jpg',
  'artist': 'tien-yu-hung',
}


class Artist(models.Model):
  """Model to represent an artist."""
  username = models.CharField(max_length=25, db_index=True, unique=True, blank=True, null=True)
  full_name = models.CharField(max_length=255)
  description = models.TextField(blank=True, null=True)
  statement = models.TextField(blank=True, null=True)
  essays = models.TextField(blank=True, null=True)
  videos = models.TextField(blank=True, null=True)
  display_order = models.IntegerField(blank=True, null=True)
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
  description = models.TextField(blank=True, null=True)
  title = models.CharField(max_length=255, blank=True, null=True)
  medium = models.CharField(max_length=255, blank=True, null=True)
  year = models.CharField(max_length=255, blank=True, null=True)
  dimensions = models.CharField(max_length=255, blank=True, null=True)
  source = models.CharField(max_length=255, blank=True, null=True)


admin.site.register(Artist)
admin.site.register(Image)
