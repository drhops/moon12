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
  'event-0430': {
    'title': u'執行長赴台中教育大學演講',
    'description': u"""夢12 美學空間王月琴執行長於四月三十日，受邀於台中教育大學美術系專題講座。
講座主題：別讓夢想等太久，討論創意的動機、來源、過程、典範，
並與同學們一起透視藝術世界的奧祕""",
    'dates': '4/30',
    'show': True,
    'future': False,
    'image': 'images/events/event-0430/album/slides/DSC_0530.jpg',
    'images': [
'images/events/event-0430/album/slides/DSC_0516.jpg',
'images/events/event-0430/album/slides/DSC_0519.jpg',
'images/events/event-0430/album/slides/DSC_0521.jpg',
'images/events/event-0430/album/slides/DSC_0522.jpg',
'images/events/event-0430/album/slides/DSC_0525.jpg',
'images/events/event-0430/album/slides/DSC_0526.jpg',
'images/events/event-0430/album/slides/DSC_0527.jpg',
'images/events/event-0430/album/slides/DSC_0528.jpg',
'images/events/event-0430/album/slides/DSC_0529.jpg',
'images/events/event-0430/album/slides/DSC_0530.jpg',
],
  },
  'event-0421': {
    'title': u'吳怡蒨老師與龍安國小資優班學生相約',
    'description': u"""吳怡蒨老師與龍安國小資優班學生相約在夢12。
在美好的藝術空間，經歷了難得的美感洗禮。
結合社區藝術與機會教育，推廣城市新美學。""",
    'dates': '4/21',
    'show': True,
    'future': False,
    'image': 'images/events/event-0421/album/slides/IMG_8988.jpg',
    'images': [
'images/events/event-0421/album/slides/IMG_8984.jpg',
'images/events/event-0421/album/slides/IMG_8985.jpg',
'images/events/event-0421/album/slides/IMG_8986.jpg',
'images/events/event-0421/album/slides/IMG_8987.jpg',
'images/events/event-0421/album/slides/IMG_8988.jpg',
'images/events/event-0421/album/slides/IMG_8989.jpg',
'images/events/event-0421/album/slides/IMG_8990.jpg',
'images/events/event-0421/album/slides/IMG_8991.jpg',
'images/events/event-0421/album/slides/IMG_8992.jpg',
'images/events/event-0421/album/slides/IMG_8993.jpg',
'images/events/event-0421/album/slides/IMG_8994.jpg',
'images/events/event-0421/album/slides/IMG_8995.jpg',
'images/events/event-0421/album/slides/IMG_8996.jpg',
'images/events/event-0421/album/slides/IMG_8997.jpg',
'images/events/event-0421/album/slides/IMG_8998.jpg',
'images/events/event-0421/album/slides/IMG_8999.jpg',
'images/events/event-0421/album/slides/IMG_9000.jpg',
'images/events/event-0421/album/slides/IMG_9001.jpg',
'images/events/event-0421/album/slides/IMG_9002.jpg',
'images/events/event-0421/album/slides/IMG_9003.jpg',
'images/events/event-0421/album/slides/IMG_9004.jpg',
'images/events/event-0421/album/slides/IMG_9005.jpg',
],
  },
  'opening-0414': {
    'title': u'吳怡蒨個展開幕',
    'description': u"""感謝各界愛好藝文的親朋好友大力支持，
吳怡蒨老師的個展「城市拼圖」開幕圓滿順利。
在都會裡透過對藝術熱絡的交流，添加一片美好。""",
    'dates': '4/14',
    'show': False,
    'future': False,
    'image': 'images/events/opening-0414/album/slides/IMG_8963.jpg',
    'images': [
'images/events/opening-0414/album/slides/IMG_8932.jpg',
'images/events/opening-0414/album/slides/IMG_8933.jpg',
'images/events/opening-0414/album/slides/IMG_8934.jpg',
'images/events/opening-0414/album/slides/IMG_8935.jpg',
'images/events/opening-0414/album/slides/IMG_8936.jpg',
'images/events/opening-0414/album/slides/IMG_8937.jpg',
'images/events/opening-0414/album/slides/IMG_8938.jpg',
'images/events/opening-0414/album/slides/IMG_8939.jpg',
'images/events/opening-0414/album/slides/IMG_8940.jpg',
'images/events/opening-0414/album/slides/IMG_8941.jpg',
'images/events/opening-0414/album/slides/IMG_8942.jpg',
'images/events/opening-0414/album/slides/IMG_8943.jpg',
'images/events/opening-0414/album/slides/IMG_8944.jpg',
'images/events/opening-0414/album/slides/IMG_8945.jpg',
'images/events/opening-0414/album/slides/IMG_8946.jpg',
'images/events/opening-0414/album/slides/IMG_8947.jpg',
'images/events/opening-0414/album/slides/IMG_8948.jpg',
'images/events/opening-0414/album/slides/IMG_8949.jpg',
'images/events/opening-0414/album/slides/IMG_8950.jpg',
'images/events/opening-0414/album/slides/IMG_8951.jpg',
'images/events/opening-0414/album/slides/IMG_8952.jpg',
'images/events/opening-0414/album/slides/IMG_8953.jpg',
'images/events/opening-0414/album/slides/IMG_8954.jpg',
'images/events/opening-0414/album/slides/IMG_8955.jpg',
'images/events/opening-0414/album/slides/IMG_8956.jpg',
'images/events/opening-0414/album/slides/IMG_8957.jpg',
'images/events/opening-0414/album/slides/IMG_8959.jpg',
'images/events/opening-0414/album/slides/IMG_8960.jpg',
'images/events/opening-0414/album/slides/IMG_8961.jpg',
'images/events/opening-0414/album/slides/IMG_8962.jpg',
'images/events/opening-0414/album/slides/IMG_8963.jpg',
'images/events/opening-0414/album/slides/IMG_8964.jpg',
'images/events/opening-0414/album/slides/IMG_8965.jpg',
'images/events/opening-0414/album/slides/IMG_8966.jpg',
'images/events/opening-0414/album/slides/IMG_8967.jpg',
'images/events/opening-0414/album/slides/IMG_8968.jpg',
'images/events/opening-0414/album/slides/IMG_8969.jpg',
'images/events/opening-0414/album/slides/IMG_8970.jpg',
'images/events/opening-0414/album/slides/IMG_8971.jpg',
'images/events/opening-0414/album/slides/IMG_8972.jpg',
'images/events/opening-0414/album/slides/IMG_8973.jpg',
'images/events/opening-0414/album/slides/IMG_8974.jpg',
'images/events/opening-0414/album/slides/IMG_8975.jpg',
'images/events/opening-0414/album/slides/IMG_8976.jpg',
'images/events/opening-0414/album/slides/IMG_8977.jpg',
'images/events/opening-0414/album/slides/IMG_8978.jpg',
'images/events/opening-0414/album/slides/IMG_8979.jpg',
'images/events/opening-0414/album/slides/IMG_8980.jpg',
'images/events/opening-0414/album/slides/IMG_8981.jpg',
'images/events/opening-0414/album/slides/IMG_8982.jpg',
],
   },
  'art-exchange': {
    'title': u'台中教育大學藝術交流',
    'description': u'感謝台中教育大學林欽賢教授的邀請，執行長王月琴小姐赴台中與美術系的同學們進行了一場別開生面的藝術交流，相信美學的種子，將在每個角落開花結果。',
    'dates': '12/25',
    'show': False,
    'future': False,
    'image': 'images/events/art-exchange.jpg',
    'images': [
'images/events/art-exchange/album/slides/IMG_0579.JPG',
],
   },  'NTNU-professor': {
    'title': u'師大國文系教授來訪',
    'description': u'洪天宇老師的精彩作品即將與師大國文系合作，帶給各位同學們空白的美學！謝謝師大國文系的教授們來訪，2013年在師大的一系列活動精彩可期，請勿錯過。',
    'dates': '12/15',
    'show': False,
    'future': False,
    'image': 'images/events/professor.jpg',
    'images': [
'images/events/NTNU-professor/album/slides/IMG_8591.JPG',
'images/events/NTNU-professor/album/slides/IMG_8592.JPG',
'images/events/NTNU-professor/album/slides/IMG_8593.JPG',
'images/events/NTNU-professor/album/slides/IMG_8594.JPG',
'images/events/NTNU-professor/album/slides/IMG_8595.JPG',
'images/events/NTNU-professor/album/slides/IMG_8596.JPG',
'images/events/NTNU-professor/album/slides/IMG_8597.JPG',
'images/events/NTNU-professor/album/slides/IMG_8598.JPG',
'images/events/NTNU-professor/album/slides/IMG_8599.JPG',
'images/events/NTNU-professor/album/slides/IMG_8600.JPG',
'images/events/NTNU-professor/album/slides/IMG_8601.JPG',
'images/events/NTNU-professor/album/slides/IMG_8602.JPG',
'images/events/NTNU-professor/album/slides/IMG_8603.JPG',
'images/events/NTNU-professor/album/slides/IMG_8604.JPG',
'images/events/NTNU-professor/album/slides/IMG_8605.JPG',
'images/events/NTNU-professor/album/slides/IMG_8606.JPG',
'images/events/NTNU-professor/album/slides/IMG_8607.JPG',
'images/events/NTNU-professor/album/slides/IMG_8608.JPG',
'images/events/NTNU-professor/album/slides/IMG_8609.JPG',
'images/events/NTNU-professor/album/slides/IMG_8610.JPG',
'images/events/NTNU-professor/album/slides/IMG_8611.JPG',
'images/events/NTNU-professor/album/slides/IMG_8612.JPG',
'images/events/NTNU-professor/album/slides/IMG_8613.JPG',
'images/events/NTNU-professor/album/slides/IMG_8614.JPG',
'images/events/NTNU-professor/album/slides/IMG_8615.JPG',
],
   },
  'soap-making': {
    'title': u'手工皂講座',
    'description': u'為了實踐讓藝術走入生活的承諾，夢12美學空間特別邀請山月桂工藝坊講師，帶給各位朋友們全新的環保體驗。手工皂不僅是愛自然的清潔方式，同時，透過手工皂的製作，不同色彩、紋理與質感的表現，更是特別的美感經驗。感謝每位參與的朋友們，環保美學--手工皂講座大成功！',
    'dates': '11/24',
    'image': 'images/events/soap.jpg',
    'future': False,
    'images': [
'images/events/soap-making/album/slides/IMG_8326.JPG',
'images/events/soap-making/album/slides/IMG_8327.JPG',
'images/events/soap-making/album/slides/IMG_8328.JPG',
'images/events/soap-making/album/slides/IMG_8329.JPG',
'images/events/soap-making/album/slides/IMG_8330.JPG',
'images/events/soap-making/album/slides/IMG_8331.JPG',
'images/events/soap-making/album/slides/IMG_8332.JPG',
'images/events/soap-making/album/slides/IMG_8333.JPG',
'images/events/soap-making/album/slides/IMG_8334.JPG',
'images/events/soap-making/album/slides/IMG_8335.JPG',
'images/events/soap-making/album/slides/IMG_8336.JPG',
'images/events/soap-making/album/slides/IMG_8337.JPG',
'images/events/soap-making/album/slides/IMG_8338.JPG',
'images/events/soap-making/album/slides/IMG_8339.JPG',
'images/events/soap-making/album/slides/IMG_8340.JPG',
'images/events/soap-making/album/slides/IMG_8341.JPG',
'images/events/soap-making/album/slides/IMG_8342.JPG',
'images/events/soap-making/album/slides/IMG_8343.JPG',
'images/events/soap-making/album/slides/IMG_8344.JPG',
'images/events/soap-making/album/slides/IMG_8345.JPG',
'images/events/soap-making/album/slides/IMG_8346.JPG',
'images/events/soap-making/album/slides/IMG_8347.JPG',
'images/events/soap-making/album/slides/IMG_8348.JPG',
'images/events/soap-making/album/slides/IMG_8349.JPG',
'images/events/soap-making/album/slides/IMG_8350.JPG',
'images/events/soap-making/album/slides/IMG_8351.JPG',
'images/events/soap-making/album/slides/IMG_8352.JPG',
'images/events/soap-making/album/slides/IMG_8353.JPG',
'images/events/soap-making/album/slides/IMG_8354.JPG',
'images/events/soap-making/album/slides/IMG_8355.JPG',
'images/events/soap-making/album/slides/IMG_8356.JPG',
'images/events/soap-making/album/slides/IMG_8357.JPG',
'images/events/soap-making/album/slides/IMG_8358.JPG',
'images/events/soap-making/album/slides/IMG_8359.JPG',
'images/events/soap-making/album/slides/IMG_8360.JPG',
'images/events/soap-making/album/slides/IMG_8361.JPG',
'images/events/soap-making/album/slides/IMG_8362.JPG',
'images/events/soap-making/album/slides/IMG_8363.JPG',
'images/events/soap-making/album/slides/IMG_8364.JPG',
'images/events/soap-making/album/slides/IMG_8365.JPG',
'images/events/soap-making/album/slides/IMG_8366.JPG',
'images/events/soap-making/album/slides/IMG_8367.JPG',
'images/events/soap-making/album/slides/IMG_8368.JPG',
'images/events/soap-making/album/slides/IMG_8369.JPG',
'images/events/soap-making/album/slides/IMG_8370.JPG',
'images/events/soap-making/album/slides/IMG_8371.JPG',
'images/events/soap-making/album/slides/IMG_8372.JPG',
'images/events/soap-making/album/slides/IMG_8373.JPG',
'images/events/soap-making/album/slides/IMG_8374.JPG',
'images/events/soap-making/album/slides/IMG_8375.JPG',
'images/events/soap-making/album/slides/IMG_8378.JPG',
'images/events/soap-making/album/slides/IMG_8379.JPG',
'images/events/soap-making/album/slides/IMG_8380.JPG',
'images/events/soap-making/album/slides/IMG_8381.JPG',
'images/events/soap-making/album/slides/IMG_8382.JPG',
'images/events/soap-making/album/slides/IMG_8383.JPG',
'images/events/soap-making/album/slides/IMG_8384.JPG',
'images/events/soap-making/album/slides/IMG_8385.JPG',
  ],
  },
  'opening': {
    'title': u'夢12開幕',
    'description': u'經過許多人的支持與努力，夢12美學空間終於誕生了！座落於安和路二段的夢12美學空間，位在遠企購物中心對面的靜巷之中，她不只是一間畫廊，她更將是帶給社區活力、充滿藝術文化的美學重鎮。相信在不久的未來，她將帶給每個喜愛藝術的朋友們美麗的夢想。',
    'dates': '10/27',
    'image': 'images/events/opening.jpg',
    'future': False,
    'images': [
'images/events/opening.jpg',
    ],
    'images': [
'images/events/opening/album/slides/2012-10-31-14.53.08.JPG',
'images/events/opening/album/slides/2012-10-31-14.53.11.JPG',
'images/events/opening/album/slides/2012-10-31-14.53.19.JPG',
'images/events/opening/album/slides/2012-10-31-14.54.16.JPG',
'images/events/opening/album/slides/DSC02229.JPG',
'images/events/opening/album/slides/DSC02230.JPG',
'images/events/opening/album/slides/DSC02231.JPG',
'images/events/opening/album/slides/DSC02232.JPG',
'images/events/opening/album/slides/DSC02233.JPG',
'images/events/opening/album/slides/DSC02234.JPG',
'images/events/opening/album/slides/DSC02235.JPG',
'images/events/opening/album/slides/DSC02236.JPG',
'images/events/opening/album/slides/DSC02237.JPG',
'images/events/opening/album/slides/DSC02238.JPG',
'images/events/opening/album/slides/DSC02239.JPG',
'images/events/opening/album/slides/DSC02240.JPG',
'images/events/opening/album/slides/DSC02241.JPG',
'images/events/opening/album/slides/DSC_0773.JPG',
'images/events/opening/album/slides/DSC_0774.JPG',
'images/events/opening/album/slides/DSC_0776.JPG',
'images/events/opening/album/slides/DSC_0779.JPG',
'images/events/opening/album/slides/DSC_0781.JPG',
'images/events/opening/album/slides/DSC_0783.JPG',
'images/events/opening/album/slides/DSC_0784.JPG',
'images/events/opening/album/slides/DSC_0786.JPG',
'images/events/opening/album/slides/DSC_0787.JPG',
'images/events/opening/album/slides/DSC_0790.JPG',
'images/events/opening/album/slides/DSC_0791.JPG',
'images/events/opening/album/slides/DSC_0797.JPG',
'images/events/opening/album/slides/DSC_0798.JPG',
'images/events/opening/album/slides/DSC_0803.JPG',
'images/events/opening/album/slides/DSC_0805.JPG',
'images/events/opening/album/slides/DSC_0807.JPG',
'images/events/opening/album/slides/DSC_0824.JPG',
'images/events/opening/album/slides/DSC_0829.JPG',
'images/events/opening/album/slides/DSC_0830.JPG',
'images/events/opening/album/slides/DSC_0831.JPG',
'images/events/opening/album/slides/DSC_0834.JPG',
'images/events/opening/album/slides/DSC_0835.JPG',
'images/events/opening/album/slides/DSC_0836.JPG',
'images/events/opening/album/slides/DSC_0840.JPG',
'images/events/opening/album/slides/DSC_0843.JPG',
'images/events/opening/album/slides/DSC_0845.JPG',
'images/events/opening/album/slides/DSC_0847.JPG',
'images/events/opening/album/slides/DSC_0856.JPG',
'images/events/opening/album/slides/DSC_0857.JPG',
'images/events/opening/album/slides/DSC_0858.JPG',
'images/events/opening/album/slides/DSC_0860.JPG',
'images/events/opening/album/slides/DSC_0862.JPG',
'images/events/opening/album/slides/DSC_0866.JPG',
'images/events/opening/album/slides/DSC_0869.JPG',
'images/events/opening/album/slides/DSC_0871.JPG',
'images/events/opening/album/slides/DSC_0876.JPG',
'images/events/opening/album/slides/DSC_0877.JPG',
'images/events/opening/album/slides/DSC_0879.JPG',
'images/events/opening/album/slides/DSC_0884.JPG',
'images/events/opening/album/slides/DSC_0886.JPG',
'images/events/opening/album/slides/DSC_0888.JPG',
'images/events/opening/album/slides/DSC_0892.JPG',
'images/events/opening/album/slides/DSC_0893.JPG',
'images/events/opening/album/slides/DSC_0896.JPG',
'images/events/opening/album/slides/DSC_0898.JPG',
'images/events/opening/album/slides/DSC_0901.JPG',
'images/events/opening/album/slides/DSC_0904.JPG',
'images/events/opening/album/slides/DSC_0906.JPG',
'images/events/opening/album/slides/DSC_0907.JPG',
'images/events/opening/album/slides/DSC_0908.JPG',
'images/events/opening/album/slides/DSC_0909.JPG',
'images/events/opening/album/slides/DSC_0913.JPG',
'images/events/opening/album/slides/DSC_0917.JPG',
'images/events/opening/album/slides/DSC_0920.JPG',
'images/events/opening/album/slides/DSC_0922.JPG',
'images/events/opening/album/slides/DSC_0923.JPG',
'images/events/opening/album/slides/DSC_0935.JPG',
'images/events/opening/album/slides/DSC_0936.JPG',
'images/events/opening/album/slides/DSC_0937.JPG',
'images/events/opening/album/slides/DSC_0939.JPG',
'images/events/opening/album/slides/DSC_0940.JPG',
'images/events/opening/album/slides/DSC_0942.JPG',
'images/events/opening/album/slides/DSC_0943.JPG',
'images/events/opening/album/slides/DSC_0947.JPG',
'images/events/opening/album/slides/DSC_0949.JPG',
'images/events/opening/album/slides/DSC_0956.JPG',
'images/events/opening/album/slides/DSC_0957.JPG',
'images/events/opening/album/slides/DSC_0959.JPG',
'images/events/opening/album/slides/DSC_0960.JPG',
'images/events/opening/album/slides/DSC_0962.JPG',
'images/events/opening/album/slides/DSC_0967.JPG',
'images/events/opening/album/slides/DSC_0972.JPG',
'images/events/opening/album/slides/DSC_0974.JPG',
'images/events/opening/album/slides/DSC_0978.JPG',
'images/events/opening/album/slides/DSC_0979.JPG',
'images/events/opening/album/slides/DSC_0981.JPG',
'images/events/opening/album/slides/DSC_0985.JPG',
'images/events/opening/album/slides/DSC_0987.JPG',
'images/events/opening/album/slides/DSC_0991.JPG',
'images/events/opening/album/slides/DSC_0993.JPG',
'images/events/opening/album/slides/DSC_0994.JPG',
'images/events/opening/album/slides/DSC_0996.JPG',
'images/events/opening/album/slides/DSC_0997.JPG',
'images/events/opening/album/slides/DSC_0998.JPG',
'images/events/opening/album/slides/DSC_1003.JPG',
'images/events/opening/album/slides/DSC_1004.JPG',
'images/events/opening/album/slides/DSC_1006.JPG',
'images/events/opening/album/slides/DSC_1008.JPG',
'images/events/opening/album/slides/DSC_1011.JPG',
'images/events/opening/album/slides/DSC_1017.JPG',
'images/events/opening/album/slides/DSC_1019.JPG',
'images/events/opening/album/slides/DSC_1020.JPG',
'images/events/opening/album/slides/DSC_1023.JPG',
'images/events/opening/album/slides/DSC_1027.JPG',
'images/events/opening/album/slides/DSC_1029.JPG',
'images/events/opening/album/slides/DSC_1033.JPG',
'images/events/opening/album/slides/DSC_1035.JPG',
'images/events/opening/album/slides/DSC_1038.JPG',
'images/events/opening/album/slides/DSC_1049.JPG',
'images/events/opening/album/slides/DSC_1050.JPG',
'images/events/opening/album/slides/DSC_1063.JPG',
'images/events/opening/album/slides/DSC_1066.JPG',
'images/events/opening/album/slides/DSC_1067.JPG',
'images/events/opening/album/slides/DSC_1070.JPG',
'images/events/opening/album/slides/DSC_1073.JPG',
'images/events/opening/album/slides/DSC_1076.JPG',
'images/events/opening/album/slides/DSC_1077.JPG',
'images/events/opening/album/slides/DSC_1085.JPG',
'images/events/opening/album/slides/DSC_1086.JPG',
'images/events/opening/album/slides/DSC_1087.JPG',
'images/events/opening/album/slides/DSC_1098.JPG',
'images/events/opening/album/slides/DSC_1103.JPG',
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
