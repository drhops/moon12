# This Python file uses the following encoding: utf-8
'''
Models for Moon12.

Created on Oct 30, 2012
@author: Daniel Hopkins (drhops@gmail.com)
'''
from django.db import models

EMAIL_MAX_LENGTH = 25

D_EVENTS = {
  'soap-making': {
    'description': u'山月桂工作坊將在11/24於夢12美學空間舉辦手工皂講座，屆時有興趣的朋友都將可以免費參加，先來一睹為快，看看這些彷彿藝術品一般的手工皂吧！',
    'image': '/static/images/events/soap.jpg',
  },
  'opening': {
    'description': u'十月二十七日下午三點夢12開幕了，當天超過百位好朋友從紐澤西、成都、台中、新竹趕來，帶來一場溫馨的聚會，各個角落散發著濃郁的友情。在這一刻，我們的夢想慢慢開始藴釀...',
    'image': '/static/images/events/opening.jpg',
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

D_ARTISTS = {
  'wong-ming-zhe': {
    'full_name': u'翁明哲',
    'email': 'dbchang@gmail.com',
    'description': u'窗子是穿透的，隔開自我的內與外，是連接過去與現在的出口；深井則是折射 的，映照出心理的慾望與身體的衝動，有水面上的浮光與水面下的掠影。--翁 明哲',
    'home_image': '/static/images/artists/blue_sky.jpg',
    'images': [
      {
        'title': u'壓力',  
        'description': 'DESCRIPTION',
        'medium': u'油彩畫布',
        'dimensions': '120x120cm',
        'year': '2007',
        'source': u'翁明哲_壓力.jpg',
      },
      {
        'title': u'屁股',  
        'description': 'DESCRIPTION',
        'medium': u'油彩畫布',
        'dimensions': '91.5x116.5cm',
        'year': '2012',
        'source': u'翁明哲_屁股.jpg',
      },
      {
        'title': u'睡覺',  
        'description': 'DESCRIPTION',
        'medium': u'油彩畫布',
        'dimensions': '91.5x116.5cm',
        'year': '2012',
        'source': u'翁明哲_睡覺.jpg',
      },
      {
        'title': u'蓮花池',  
        'description': 'DESCRIPTION',
        'medium': u'油彩畫布',
        'dimensions': '25x45cm',
        'year': '2012',
        'source': u'翁明哲_蓮花池.jpg',
      },
      {
        'title': u'石門水庫',  
        'description': 'DESCRIPTION',
        'medium': u'油彩畫布',
        'dimensions': '25x45cm',
        'year': '2012',
        'source': u'翁明哲_石門水庫.jpg',
      },
      {
        'title': u'三顆橘子',  
        'description': 'DESCRIPTION',
        'medium': u'油彩畫布',
        'dimensions': '25x45cm',
        'year': '2012',
        'source': u'翁明哲_三顆橘子.jpg',
      },
      {
        'title': u'礁溪魚塭',  
        'description': 'DESCRIPTION',
        'medium': u'油彩畫布',
        'dimensions': '25x45cm',
        'year': '2012',
        'source': u'翁明哲_礁溪魚塭.jpg',
      },
      {
        'title': u'大溪夜街',  
        'description': 'DESCRIPTION',
        'medium': u'油彩畫布',
        'dimensions': '91.5x116.5cm',
        'year': '2012',
        'source': u'翁明哲_大溪夜街.jpg',
      },
      {
        'title': u'碧潭左岸',  
        'description': 'DESCRIPTION',
        'medium': u'油彩畫布',
        'dimensions': '91x116.5cm',
        'year': '2012',
        'source': u'翁明哲_碧潭左岸.jpg',
      },
      {
        'title': u'奔跑的櫟樹',  
        'description': 'DESCRIPTION',
        'medium': u'油彩畫布',
        'dimensions': '120x120cm',
        'year': '2012',
        'source': u'翁明哲_奔跑的櫟樹.jpg',
      },
      {
        'title': u'伊比利之戀',  
        'description': 'DESCRIPTION',
        'medium': u'油彩畫布',
        'dimensions': '120F',
        'year': '2012',
        'source': u'翁明哲_伊比利之戀.jpg',
      },
      {
        'title': u'直潭的早晨',  
        'description': 'DESCRIPTION',
        'medium': u'油彩畫布',
        'dimensions': '72x41cm',
        'year': '2012',
        'source': u'翁明哲_直潭的早晨.jpg',
      },
      {
        'title': u'碧潭吊僑向晚',  
        'description': 'DESCRIPTION',
        'medium': u'油彩畫布',
        'dimensions': '25x45cm',
        'year': '2012',
        'source': u'翁明哲_碧潭吊僑向晚.jpg',
      },
      {
        'title': u'三條魚兩片檸檬',  
        'description': 'DESCRIPTION',
        'medium': u'油彩畫布',
        'dimensions': '25x45cm',
        'year': '2012',
        'source': u'翁明哲_三條魚兩片檸檬.jpg',
      },
      {
        'title': u'看著窗外的夏漱',  
        'description': 'DESCRIPTION',
        'medium': u'油彩畫布',
        'dimensions': '270x178cm',
        'year': '2012',
        'source': u'翁明哲_看著窗外的夏漱.jpg',
      },
      {
        'title': u'和風吹拂的九份',  
        'description': 'DESCRIPTION',
        'medium': u'油彩畫布',
        'dimensions': '91.5x116.5cm',
        'year': '2012',
        'source': u'翁明哲_和風吹拂的九份.jpg',
      },
      {
        'title': u'由土地公廟看直潭',  
        'description': 'DESCRIPTION',
        'medium': u'油彩畫布',
        'dimensions': '25x45cm',
        'year': '2012',
        'source': u'翁明哲_由土地公廟看直潭.jpg',
      },
      {
        'title': u'金瓜石的慵懶午後',  
        'description': 'DESCRIPTION',
        'medium': u'油彩畫布',
        'dimensions': '91x116.5cm',
        'year': '2012',
        'source': u'翁明哲_金瓜石的慵懶午後.jpg',
      },
      {
        'title': u'陽光普照的水湳洞',  
        'description': 'DESCRIPTION',
        'medium': u'油彩畫布',
        'dimensions': '91x116.5cm',
        'year': '2012',
        'source': u'翁明哲_陽光普照的水湳洞.jpg',
      },
    ],
  },
  'wong-ming-ya': {
    'full_name': u'翁明崖',
    'email': 'drhops@gmail.com',
    'description': u'我見著了這海洋與大氣相接的海象，卻見不著海洋這物質的內在，我知其為 水，可這物質裡的世界為何，不可見。因其不可見而神祕，而可想像，有如人 這肉體的可見，而不可見其內在的精神性。--翁明崖',
    'home_image': '/static/images/artists/beach.jpg',
    'images': [
      {
        'title': u'旅．形 - 石梯坪',
        'description': 'DESCRIPTION',
        'medium': u'油彩、畫布',
        'dimensions': '30x30cm',
        'year': '2009',
        'source': '1-2.jpg'
      },
      {
        'title': u'旅．形 - 鼻頭角',
        'description': 'DESCRIPTION',
        'medium': u'油彩、畫布',
        'dimensions': '30x30cm',
        'year': '2009',
        'source': '1-3.jpg'
      },
      {
        'title': u'石蓮花',
        'description': 'DESCRIPTION',
        'medium': u'油彩、畫布',
        'dimensions': '25x25cm',
        'year': '2012',
        'source': '2.jpg',
      },
      {
        'title': u'美麗與哀愁Ⅲ',
        'description': 'DESCRIPTION',
        'medium': u'油彩、畫布',
        'dimensions': '50x100cm',
        'year': '2010',
        'source': '3.jpg',
      },
      {
        'title': u'美麗與哀愁-Flora',
        'description': 'DESCRIPTION',
        'medium': u'油彩、畫布',
        'dimensions': '50x100cm',
        'year': '2011',
        'source': '7.jpg',
      },
      {
        'title': u'紅石榴',
        'description': 'DESCRIPTION',
        'medium': u'畫布、油彩',
        'dimensions': '50x25cm',
        'year': '2010',
        'source': '8.jpg',
      },
    ],
  },
  'hong-tian-yu': {
    'full_name': u'洪天宇',
    'description': u'熱帶雨林這把大火從1964 年開始燃起，即便是在2012 年的今天，依然餘烟裊 裊。在地表蔓生的牧場和油棕園逐漸吞噬雨林的天空，在灰燼單調劃一的大地 裏，我們撐起一座座名牌的祭壇。--洪天宇',
    'home_image': '/static/images/artists/mcdonalds.jpg',
  },
  'zhang-zheng-yu': {
    'full_name': u'張正裕',
    'description': u'國內知名的陶藝家，其作品融合傳統與現代，在精湛的陶藝與花藝調和之下， 交織出溫暖而樸實的藝術樣貌。',
    'home_image': '/static/images/artists/chang.jpg',
    'images': [
      {
        'title': '#0810',  
        'description': 'DESCRIPTION',
        'medium': u'',
        'dimensions': '495×195×h215mm',
        'year': '',
        'source': u'張正裕_0810_1.jpg',
      },
      {
        'title': '#1715 (view 1)',  
        'description': 'DESCRIPTION',
        'medium': u'',
        'dimensions': '242×150×h368mm',
        'year': '',
        'source': u'張正裕_1715_1.jpg',
      },
      {
        'title': '#1715 (view 2)',  
        'description': 'DESCRIPTION',
        'medium': u'',
        'dimensions': '242×150×h368mm',
        'year': '',
        'source': u'張正裕_1715_2.jpg',
      },
      {
        'title': '#1715 (view 3)',  
        'description': 'DESCRIPTION',
        'medium': u'',
        'dimensions': '242×150×h368mm',
        'year': '',
        'source': u'張正裕_1715_3.jpg',
      },
      {
        'title': '#1807 (view 1)',
        'description': 'DESCRIPTION',
        'medium': u'',
        'dimensions': '238×140×h370mm',
        'year': '',
        'source': u'張正裕_1807_1.jpg',
      },
      {
        'title': '#1807 (view 2)',  
        'description': 'DESCRIPTION',
        'medium': u'',
        'dimensions': '238×140×h370mm',
        'year': '',
        'source': u'張正裕_1807_2.jpg',
      },
      {
        'title': '#1807 (view 3)',  
        'description': 'DESCRIPTION',
        'medium': u'',
        'dimensions': '238×140×h370mm',
        'year': '',
        'source': u'張正裕_1807_3.jpg',
      },
      {
        'title': '#1807 (view 4)',  
        'description': 'DESCRIPTION',
        'medium': u'',
        'dimensions': '238×140×h370mm',
        'year': '',
        'source': u'張正裕_1807_4.jpg',
      },
      {
        'title': '#1814',  
        'description': 'DESCRIPTION',
        'medium': u'',
        'dimensions': '156×156×h215mm',
        'year': '',
        'source': u'張正裕_1814_1.jpg',
      },
      {
        'title': '#1824 (view 1)',  
        'description': 'DESCRIPTION',
        'medium': u'',
        'dimensions': '200×92×h235mm',
        'year': '',
        'source': u'張正裕_1824_1.jpg',
      },
      {
        'title': '#1824 (view 2)',  
        'description': 'DESCRIPTION',
        'medium': u'',
        'dimensions': '200×92×h235mm',
        'year': '',
        'source': u'張正裕_1824_2.jpg',
      },
      {
        'title': '#1919 (view 1)',  
        'description': 'DESCRIPTION',
        'medium': u'',
        'dimensions': '272×105×h283mm',
        'year': '',
        'source': u'張正裕_1919_1.jpg',
      },
      {
        'title': '#1919 (view 2)',  
        'description': 'DESCRIPTION',
        'medium': u'',
        'dimensions': '272×105×h283mm',
        'year': '',
        'source': u'張正裕_1919_2.jpg',
      },
      {
        'title': '#2004 (view 1)',  
        'description': 'DESCRIPTION',
        'medium': u'',
        'dimensions': '328×170×h280mm',
        'year': '',
        'source': u'張正裕_2004_1.jpg',
      },
      {
        'title': '#2004 (view 2)',  
        'description': 'DESCRIPTION',
        'medium': u'',
        'dimensions': '328×170×h280mm',
        'year': '',
        'source': u'張正裕_2004_2.jpg',
      },
      {
        'title': '#2004 (view 3)',  
        'description': 'DESCRIPTION',
        'medium': u'',
        'dimensions': '328×170×h280mm',
        'year': '',
        'source': u'張正裕_2004_3.jpg',
      },
      {
        'title': '#2004 (view 4)',  
        'description': 'DESCRIPTION',
        'medium': u'',
        'dimensions': '328×170×h280mm',
        'year': '',
        'source': u'張正裕_2004_4.jpg',
      },
      {
        'title': '#2005 (view 1)',  
        'description': 'DESCRIPTION',
        'medium': u'',
        'dimensions': '272×98×h283mm',
        'year': '',
        'source': u'張正裕_2005_1.jpg',
      },
      {
        'title': '#2005 (view 2)',  
        'description': 'DESCRIPTION',
        'medium': u'',
        'dimensions': '272×98×h283mm',
        'year': '',
        'source': u'張正裕_2005_2.jpg',
      },
      {
        'title': '#2005 (view 3)',  
        'description': 'DESCRIPTION',
        'medium': u'',
        'dimensions': '272×98×h283mm',
        'year': '',
        'source': u'張正裕_2005_3.jpg',
      },
      {
        'title': '#2005 (view 4)',  
        'description': 'DESCRIPTION',
        'medium': u'',
        'dimensions': '272×98×h283mm',
        'year': '',
        'source': u'張正裕_2005_4.jpg',
      },
    ],
  },
  'broustet': {
    'full_name': u'Vincent Broustet',
    'description': u'Vincent 擅長以簡單線條勾勒形體，表現極簡風格。他的創作媒材包括炭筆、水 彩、油畫、織錦，各地風情人文交織在他的藝術創作之中，作品在法國、摩洛 哥、柬埔寨重要畫廊與公共空間展出。 在夢12開幕現場，Vincent 以獨特的絨布 “Velvet” 系列作為台灣首次展出，他把 絨布的柔順細緻融合在抽象、意象的造型中，呈現華麗而內斂的底蘊。',
    'home_image': '/static/images/artists/broustet.jpg',
    'images': [
      {
        'title': 'broustet 1',
        'description': 'description',
        'source': '1.jpg',
      },
      {
        'title': 'broustet 2',
        'description': 'description',
        'source': '2.jpg',
      },
      {
        'title': 'broustet 3',
        'description': 'description',
        'source': '3.jpg',
      },
      {
        'title': 'broustet 4',
        'description': 'description',
        'source': '4.jpg',
      },
      {
        'title': 'broustet 5',
        'description': 'description',
        'source': '5.jpg',
      },
      {
        'title': 'broustet 6',
        'description': 'description',
        'source': '6.jpg',
      },
    ],  },
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
