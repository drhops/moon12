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
  'opening-0414': {
    'title': u'吳怡蒨個展開幕',
    'dates': '3/14',
    'show': True,
    'future': False,
    'image': '/static/images/events/opening-0414/album/slides/IMG_8963.jpg',
    'images': [
'/static/images/events/opening-0414/album/slides/IMG_8932.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8933.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8934.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8935.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8936.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8937.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8938.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8939.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8940.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8941.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8942.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8943.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8944.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8945.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8946.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8947.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8948.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8949.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8950.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8951.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8952.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8953.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8954.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8955.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8956.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8957.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8959.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8960.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8961.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8962.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8963.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8964.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8965.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8966.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8967.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8968.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8969.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8970.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8971.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8972.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8973.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8974.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8975.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8976.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8977.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8978.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8979.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8980.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8981.jpg',
'/static/images/events/opening-0414/album/slides/IMG_8982.jpg',
],
   },
  'art-exchange': {
    'title': u'台中教育大學藝術交流',
    'description': u'感謝台中教育大學林欽賢教授的邀請，執行長王月琴小姐赴台中與美術系的同學們進行了一場別開生面的藝術交流，相信美學的種子，將在每個角落開花結果。',
    'dates': '12/25',
    'show': True,
    'future': False,
    'image': '/static/images/events/art-exchange.jpg',
    'images': [
'/static/images/events/art-exchange/album/slides/IMG_0579.JPG',
],
   },  'NTNU-professor': {
    'title': u'師大國文系教授來訪',
    'description': u'洪天宇老師的精彩作品即將與師大國文系合作，帶給各位同學們空白的美學！謝謝師大國文系的教授們來訪，2013年在師大的一系列活動精彩可期，請勿錯過。',
    'dates': '12/15',
    'show': False,
    'future': False,
    'image': '/static/images/events/professor.jpg',
    'images': [
'/static/images/events/NTNU-professor/album/slides/IMG_8591.JPG',
'/static/images/events/NTNU-professor/album/slides/IMG_8592.JPG',
'/static/images/events/NTNU-professor/album/slides/IMG_8593.JPG',
'/static/images/events/NTNU-professor/album/slides/IMG_8594.JPG',
'/static/images/events/NTNU-professor/album/slides/IMG_8595.JPG',
'/static/images/events/NTNU-professor/album/slides/IMG_8596.JPG',
'/static/images/events/NTNU-professor/album/slides/IMG_8597.JPG',
'/static/images/events/NTNU-professor/album/slides/IMG_8598.JPG',
'/static/images/events/NTNU-professor/album/slides/IMG_8599.JPG',
'/static/images/events/NTNU-professor/album/slides/IMG_8600.JPG',
'/static/images/events/NTNU-professor/album/slides/IMG_8601.JPG',
'/static/images/events/NTNU-professor/album/slides/IMG_8602.JPG',
'/static/images/events/NTNU-professor/album/slides/IMG_8603.JPG',
'/static/images/events/NTNU-professor/album/slides/IMG_8604.JPG',
'/static/images/events/NTNU-professor/album/slides/IMG_8605.JPG',
'/static/images/events/NTNU-professor/album/slides/IMG_8606.JPG',
'/static/images/events/NTNU-professor/album/slides/IMG_8607.JPG',
'/static/images/events/NTNU-professor/album/slides/IMG_8608.JPG',
'/static/images/events/NTNU-professor/album/slides/IMG_8609.JPG',
'/static/images/events/NTNU-professor/album/slides/IMG_8610.JPG',
'/static/images/events/NTNU-professor/album/slides/IMG_8611.JPG',
'/static/images/events/NTNU-professor/album/slides/IMG_8612.JPG',
'/static/images/events/NTNU-professor/album/slides/IMG_8613.JPG',
'/static/images/events/NTNU-professor/album/slides/IMG_8614.JPG',
'/static/images/events/NTNU-professor/album/slides/IMG_8615.JPG',
],
   },
  'soap-making': {
    'title': u'手工皂講座',
    'description': u'為了實踐讓藝術走入生活的承諾，夢12美學空間特別邀請山月桂工藝坊講師，帶給各位朋友們全新的環保體驗。手工皂不僅是愛自然的清潔方式，同時，透過手工皂的製作，不同色彩、紋理與質感的表現，更是特別的美感經驗。感謝每位參與的朋友們，環保美學--手工皂講座大成功！',
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
    'description': u'經過許多人的支持與努力，夢12美學空間終於誕生了！座落於安和路二段的夢12美學空間，位在遠企購物中心對面的靜巷之中，她不只是一間畫廊，她更將是帶給社區活力、充滿藝術文化的美學重鎮。相信在不久的未來，她將帶給每個喜愛藝術的朋友們美麗的夢想。',
    'dates': '10/27',
    'image': '/static/images/events/opening.jpg',
    'future': False,
    'images': [
'/static/images/events/opening.jpg',
    ],
    'images': [
'/static/images/events/opening/album/slides/2012-10-31-14.53.08.JPG',
'/static/images/events/opening/album/slides/2012-10-31-14.53.11.JPG',
'/static/images/events/opening/album/slides/2012-10-31-14.53.19.JPG',
'/static/images/events/opening/album/slides/2012-10-31-14.54.16.JPG',
'/static/images/events/opening/album/slides/DSC02229.JPG',
'/static/images/events/opening/album/slides/DSC02230.JPG',
'/static/images/events/opening/album/slides/DSC02231.JPG',
'/static/images/events/opening/album/slides/DSC02232.JPG',
'/static/images/events/opening/album/slides/DSC02233.JPG',
'/static/images/events/opening/album/slides/DSC02234.JPG',
'/static/images/events/opening/album/slides/DSC02235.JPG',
'/static/images/events/opening/album/slides/DSC02236.JPG',
'/static/images/events/opening/album/slides/DSC02237.JPG',
'/static/images/events/opening/album/slides/DSC02238.JPG',
'/static/images/events/opening/album/slides/DSC02239.JPG',
'/static/images/events/opening/album/slides/DSC02240.JPG',
'/static/images/events/opening/album/slides/DSC02241.JPG',
'/static/images/events/opening/album/slides/DSC_0773.JPG',
'/static/images/events/opening/album/slides/DSC_0774.JPG',
'/static/images/events/opening/album/slides/DSC_0776.JPG',
'/static/images/events/opening/album/slides/DSC_0779.JPG',
'/static/images/events/opening/album/slides/DSC_0781.JPG',
'/static/images/events/opening/album/slides/DSC_0783.JPG',
'/static/images/events/opening/album/slides/DSC_0784.JPG',
'/static/images/events/opening/album/slides/DSC_0786.JPG',
'/static/images/events/opening/album/slides/DSC_0787.JPG',
'/static/images/events/opening/album/slides/DSC_0790.JPG',
'/static/images/events/opening/album/slides/DSC_0791.JPG',
'/static/images/events/opening/album/slides/DSC_0797.JPG',
'/static/images/events/opening/album/slides/DSC_0798.JPG',
'/static/images/events/opening/album/slides/DSC_0803.JPG',
'/static/images/events/opening/album/slides/DSC_0805.JPG',
'/static/images/events/opening/album/slides/DSC_0807.JPG',
'/static/images/events/opening/album/slides/DSC_0824.JPG',
'/static/images/events/opening/album/slides/DSC_0829.JPG',
'/static/images/events/opening/album/slides/DSC_0830.JPG',
'/static/images/events/opening/album/slides/DSC_0831.JPG',
'/static/images/events/opening/album/slides/DSC_0834.JPG',
'/static/images/events/opening/album/slides/DSC_0835.JPG',
'/static/images/events/opening/album/slides/DSC_0836.JPG',
'/static/images/events/opening/album/slides/DSC_0840.JPG',
'/static/images/events/opening/album/slides/DSC_0843.JPG',
'/static/images/events/opening/album/slides/DSC_0845.JPG',
'/static/images/events/opening/album/slides/DSC_0847.JPG',
'/static/images/events/opening/album/slides/DSC_0856.JPG',
'/static/images/events/opening/album/slides/DSC_0857.JPG',
'/static/images/events/opening/album/slides/DSC_0858.JPG',
'/static/images/events/opening/album/slides/DSC_0860.JPG',
'/static/images/events/opening/album/slides/DSC_0862.JPG',
'/static/images/events/opening/album/slides/DSC_0866.JPG',
'/static/images/events/opening/album/slides/DSC_0869.JPG',
'/static/images/events/opening/album/slides/DSC_0871.JPG',
'/static/images/events/opening/album/slides/DSC_0876.JPG',
'/static/images/events/opening/album/slides/DSC_0877.JPG',
'/static/images/events/opening/album/slides/DSC_0879.JPG',
'/static/images/events/opening/album/slides/DSC_0884.JPG',
'/static/images/events/opening/album/slides/DSC_0886.JPG',
'/static/images/events/opening/album/slides/DSC_0888.JPG',
'/static/images/events/opening/album/slides/DSC_0892.JPG',
'/static/images/events/opening/album/slides/DSC_0893.JPG',
'/static/images/events/opening/album/slides/DSC_0896.JPG',
'/static/images/events/opening/album/slides/DSC_0898.JPG',
'/static/images/events/opening/album/slides/DSC_0901.JPG',
'/static/images/events/opening/album/slides/DSC_0904.JPG',
'/static/images/events/opening/album/slides/DSC_0906.JPG',
'/static/images/events/opening/album/slides/DSC_0907.JPG',
'/static/images/events/opening/album/slides/DSC_0908.JPG',
'/static/images/events/opening/album/slides/DSC_0909.JPG',
'/static/images/events/opening/album/slides/DSC_0913.JPG',
'/static/images/events/opening/album/slides/DSC_0917.JPG',
'/static/images/events/opening/album/slides/DSC_0920.JPG',
'/static/images/events/opening/album/slides/DSC_0922.JPG',
'/static/images/events/opening/album/slides/DSC_0923.JPG',
'/static/images/events/opening/album/slides/DSC_0935.JPG',
'/static/images/events/opening/album/slides/DSC_0936.JPG',
'/static/images/events/opening/album/slides/DSC_0937.JPG',
'/static/images/events/opening/album/slides/DSC_0939.JPG',
'/static/images/events/opening/album/slides/DSC_0940.JPG',
'/static/images/events/opening/album/slides/DSC_0942.JPG',
'/static/images/events/opening/album/slides/DSC_0943.JPG',
'/static/images/events/opening/album/slides/DSC_0947.JPG',
'/static/images/events/opening/album/slides/DSC_0949.JPG',
'/static/images/events/opening/album/slides/DSC_0956.JPG',
'/static/images/events/opening/album/slides/DSC_0957.JPG',
'/static/images/events/opening/album/slides/DSC_0959.JPG',
'/static/images/events/opening/album/slides/DSC_0960.JPG',
'/static/images/events/opening/album/slides/DSC_0962.JPG',
'/static/images/events/opening/album/slides/DSC_0967.JPG',
'/static/images/events/opening/album/slides/DSC_0972.JPG',
'/static/images/events/opening/album/slides/DSC_0974.JPG',
'/static/images/events/opening/album/slides/DSC_0978.JPG',
'/static/images/events/opening/album/slides/DSC_0979.JPG',
'/static/images/events/opening/album/slides/DSC_0981.JPG',
'/static/images/events/opening/album/slides/DSC_0985.JPG',
'/static/images/events/opening/album/slides/DSC_0987.JPG',
'/static/images/events/opening/album/slides/DSC_0991.JPG',
'/static/images/events/opening/album/slides/DSC_0993.JPG',
'/static/images/events/opening/album/slides/DSC_0994.JPG',
'/static/images/events/opening/album/slides/DSC_0996.JPG',
'/static/images/events/opening/album/slides/DSC_0997.JPG',
'/static/images/events/opening/album/slides/DSC_0998.JPG',
'/static/images/events/opening/album/slides/DSC_1003.JPG',
'/static/images/events/opening/album/slides/DSC_1004.JPG',
'/static/images/events/opening/album/slides/DSC_1006.JPG',
'/static/images/events/opening/album/slides/DSC_1008.JPG',
'/static/images/events/opening/album/slides/DSC_1011.JPG',
'/static/images/events/opening/album/slides/DSC_1017.JPG',
'/static/images/events/opening/album/slides/DSC_1019.JPG',
'/static/images/events/opening/album/slides/DSC_1020.JPG',
'/static/images/events/opening/album/slides/DSC_1023.JPG',
'/static/images/events/opening/album/slides/DSC_1027.JPG',
'/static/images/events/opening/album/slides/DSC_1029.JPG',
'/static/images/events/opening/album/slides/DSC_1033.JPG',
'/static/images/events/opening/album/slides/DSC_1035.JPG',
'/static/images/events/opening/album/slides/DSC_1038.JPG',
'/static/images/events/opening/album/slides/DSC_1049.JPG',
'/static/images/events/opening/album/slides/DSC_1050.JPG',
'/static/images/events/opening/album/slides/DSC_1063.JPG',
'/static/images/events/opening/album/slides/DSC_1066.JPG',
'/static/images/events/opening/album/slides/DSC_1067.JPG',
'/static/images/events/opening/album/slides/DSC_1070.JPG',
'/static/images/events/opening/album/slides/DSC_1073.JPG',
'/static/images/events/opening/album/slides/DSC_1076.JPG',
'/static/images/events/opening/album/slides/DSC_1077.JPG',
'/static/images/events/opening/album/slides/DSC_1085.JPG',
'/static/images/events/opening/album/slides/DSC_1086.JPG',
'/static/images/events/opening/album/slides/DSC_1087.JPG',
'/static/images/events/opening/album/slides/DSC_1098.JPG',
'/static/images/events/opening/album/slides/DSC_1103.JPG',
],
  },
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
