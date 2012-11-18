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
    'images': [
      {
        'title': u'划得來嗎',  
        'description': u"""
「這是交換，不是賺到 ! 」朋友對我喜滋滋的表情潑了一盆冷水，「你用電
影票的加購價買到六折的飲料和爆米花，感覺上好像賺很大，但是坐在椅子上
兩小時不動，同時又吞進八、九百卡路里，這些熱量要走兩三個小時才能消耗
掉，你不覺得這是拿健康在做交換嗎？」「是喔!那妳幫我吃。」<br/>
<br/>
如果連買個爆米花都有利害交換，那買任何東西恐怕都避不開利害的糾纏。
例如到現代超市買牛肉帶給我們明顯的好處是：高效率物流帶來低價商品，購
物環境整潔舒適，肉品冷藏處理包裝美觀無腥味，價格種類排列有序，量化視
覺衝擊選擇多樣化，自助式取貨挑到滿意再買，有手推車方便一次購足甚至送
貨到家，購物兼娛樂休閒。然而，我們不容易察覺的是：成功超市形成的市場
壟斷，肉品產地破壞環境消費者無法感受，大財團支持下的跨國連鎖供應鍵讓
全球各地自營商無力抗衡，廉價肉品創造大量消費犧牲環境及個人健康，疏離
人與牛隻從成長到屠宰的過程，讓食肉者對生命冷漠自私。<br/>
<br/>
任何事物都有多重意義，而且常常相互矛盾，再好的藥物都有副作用。還是
老子比較睿智，他說;「禍兮福之所倚，福兮禍之所伏」。 禍福利害原本就是連
體嬰，不過人偏偏就愛美好、利益、良善。政客、商品、科技之所以令人徬徨
疏離，隔一陣子便會失望反感，主要就是大家都先把好處擺在亮處大聲嚷嚷，
壞處暫時隱藏消音，直到我們不得不面對天使臉上的魔鬼笑容。
""",
        'medium': u'壓克力鋁板',
        'dimensions': '244x122cm',
        'year': '2012',
        'source': u'洪天宇_划得來嗎.jpg',
      },
      {
        'title': u'文明的路徑',  
        'description': u"""
全球在為每秒消失兩個足球場大小的森林驚呼時，印尼、巴西卻一點
也沒有道德上的歉意，持續煽動經濟升級的烈火，將雨林改成棕櫚園、農
牧場。他們憑什麼可以如此理直氣壯？難道不是全世界公認經濟成長是眾
善之門，賺錢是唯一的美德，給了他們無比的勇氣？更何況厲聲指責的歐
美環保人士，如果回顧自己的土地，恐怕一句話都說不上來。<br/>
<br/>
在歐洲人踏上美國之前，整個北美東海岸全是連綿的森林，以至於有
句老話說：松鼠在樹梢上向前跳，可以從大西洋一路上跳到密西西比河而
不需著地。全球五大洲，被人類工事改造自然樣貌進行的最徹底的就屬歐
洲。例如：法國境內原本有百分之八十森林覆蓋，到十八世紀末只剩下百
分之十四。成為西方文明搖籃的邁錫尼首都Pylos四郊盡是巨松林，原本蓊
鬱的 Melos如今全成了不毛之地。歐洲無論神話傳說或童話故事大半以森
林為舞台，如今人工建物從海岸到高山遍佈全境。整個歐美文明的進步，
長久以來可說是建立在森林的灰燼上，而今有何道德立場指責別人砍樹
呢？<br/>
<br/>
當全世界最大的日用消費品公司聯合利華（Unilever）把大片雨林變成
棕櫚油行銷全球，只不過是在走一條歐美進步的老路罷了，更何況棕櫚油
最大的買家還是歐美跨國大企業呢。晶瑩剔透的棕櫚油會跟著食品、化妝
品到全球每個人手上，讓大家都能享受到雨林的遺澤。至於熱帶雨林，放
心吧它不會完全消失，遲早我們會像歐美那樣留幾塊保護區供人憑吊，讓
我們可以安慰自己說一切如常沒甚麼不對勁，所有的天候異常只是一場虛
驚，還是努力賺錢吧 !
""",
        'medium': u'壓克力鋁板',
        'dimensions': '244x122cm',
        'year': '2011',
        'source': u'洪天宇_文明的路徑.jpg',
      },
      {
        'title': u'雨林的輓歌',  
        'description': u"""
今天海空運的周延幾乎讓所有的人都涵蓋在全球供應鏈之下。像身上
穿的衣服，原料可能產於埃及、設計在西班牙、紡織製造在中國。開車出
門，汽油是來自奈及利亞、輪胎出自法國、鋼圈來自瑞典、橡膠取自馬來
西亞。光一片餅乾的成份就可以繞遍地球一圈：麵粉-澳洲、香料-印尼、
砂糖 -巴西、葵花油-美國、包裝紙-加拿大、奶油-奧地利、運輸用油-科威
特、製餅機器-日本。當餅乾在口中爆開香氣的剎那，我們已經用味蕾跟全
世界串在一起。<br/>
<br/>
全球大大小小的事務比神經網路更密切地集結在一起。隨著流行潮流
亦步亦趨的消費者，卻不知道「皮包永遠少一個，鞋子永遠少一雙』，會
造成遠在巴西的雨林一片片地被焚燒，牛群一隻一隻地倒在自己的血泊
中。明星、名人在螢幕上對大家諄諄告誡：人要追求夢想、努力實現自
我、滿足情感需求、追求有品味的事物，此外還要照顧自己、犒賞自己，
並經由消費奢侈品建立自尊心。<br/>
<br/>
他們沒說的是：樹葉將在火焰中哭泣，子孫會用憂傷的眼睛望著我們。
""",
        'medium': u'壓克力鋁板',
        'dimensions': '244x122cm',
        'year': '2011',
        'source': u'洪天宇_雨林的輓歌.jpg',
      },
      {
        'title': u'用腳趾思考',  
        'description': u"""
我以為世上最了解自己的腳要穿什麼鞋的人就是自己，直到售鞋專櫃小姐一
面幫我挑鞋一面說：「 一雙鞋除了給你腳部帶來舒適安全之外，也同時給你帶
來自信、身份認同、和地位。鞋子穿上身便彰顯了個人風采，它把個人品味，
美感修為，一覽無遺地呈現在眾人面前。每雙鞋的款式質料都有它最適當穿著
場合，不同的活動有不同的鞋款，不同的衣著也需配不同的鞋子，穿著得體令
人印象深刻，反之亦然。買到一雙好鞋也等於買到一個好心情，每次穿你都會
開心，如果再加上名牌的加持，那走路就像漫步在雲端，足以讓你睥睨眾生。
今天我們公司的黃金紀念鞋款正在做特價，你可以物超所值地擁有它，買到等
於賺到。先生，你穿幾號的？」<br/>
<br/>
哇 ! 太優的專櫃小姐了，她讓我見識到一雙鞋不僅要配合腳型，它還要
配合整個生活文化、流行品味、身分認同，鞋子不只是包住了腳，還包住
了整個人，甚至到後來還包住了全世界。一雙鞋如果能如此神通廣大，那
它一定也能包納更寬廣的生態正義，讓製鞋過程不毀滅環境資源，不將重
金屬傾倒河川，不讓有機溶劑污染地下水源，不用血汗勞力，不讓動物承
受不人道養殖及屠宰。如果消費者意識到購買是一種權力也是一種責任，
他想買的是對環境及生命較友善的產品，那麼企業便會迎頭趕上，正如
Nike與Timberland已於2009年7月宣布不再使用來自亞馬遜雨林的皮革，
adidas與Clarks隨後跟進。今天買到最有價值的不是鞋子，而是經由專櫃小
姐一番開示而來的瞥見－『買東西，救地球』。
""",
        'medium': u'壓克力鋁板',
        'dimensions': '244x122cm',
        'year': '2012',
        'source': u'洪天宇_用腳趾思考.jpg',
      },
      {
        'title': u'誰在乎呢？',  
        'description': u"""
2008年6月巴西總統盧拉（Luiz Inacio Lula da Silva）表示：「雨林遭濫墾
有八成可歸咎於蓄養牛隻」。巴西在過去廿年，有70萬平方公里已遭破壞，相
當於每10秒鐘就破壞一個足球場面積。財報分析：「愛迪達在 2008年度第4季
的營收，由原先24.2億歐元上升了6.2%至25.7億歐元，高於預估的24.7億歐
元。」這些數字湊在一起，發現整個世界最不可忽視的角色，就是在大街小巷
走來走去、在運動場上跑跳的消費者，他們根本等不及穿破一雙球鞋，只要新
款式一報到，流行風一刮，立刻熱情擁抱再買一雙。幾十億人口喜新厭舊造就
的非理性力量，正在一步一步地改變世界。<br/>
<br/>
企業大多對生態環境關懷、提高工資、改善工作環境等等興趣缺缺，因為提
高工資改善工作環境，只有工會關心，消費者根本不在乎。關懷生態環境只有
環保人士偶爾叫囂，消費者聽了都煩。只有給我更新的款式、更新的功能、更
漂亮的價格，其餘免談。即便品牌的蓬勃壯大是建立在廉價勞工的背脊上，企
業獲利來自環境生態的萬劫不復，消費者還是只管價錢，除了錢，其他都不重
要。污染、暖化、洪水、飢荒，這些如果剛好電視正在播放，我會看一下，但
只是表面的，無動於衷的，一切都會從眼前滑過去，對 ! 看世界就像看電視一
般，下一分鐘早已忘記上一分鐘演什麼，「 結果 」是什麼都無關緊要了。
""",
        'medium': u'壓克力鋁板',
        'dimensions': '244x122cm',
        'year': '2012',
        'source': u'洪天宇_誰在乎呢.jpg',
      },
      {
        'title': u'煉獄場的遊戲',  
        'description': u"""
自1972年開始，德士古石油公司便從厄瓜多爾的熱帶雨林中成功的汲出第一
滴石油。爾後持續東鑽西挖佈下大範圍的輸油管線，一路穿越印地斯山脈直達
海邊。德士古公司將叢林中的石油基地命名為「Lago Agrio」意即「酸湖 」。
如今看來酸湖這個名字用來形容當地辛酸的生活真是貼切，德士古石油公司留
下的土地、河流、地下水污染，讓當地居民籠罩在癌症、腹痛、皮膚起泡、頭
痛的死亡陰影中。這是部落史上族人的傷痛，第一次無法由巫師撫慰<br/>
<br/>
在資本主義體系鼓舞大家賺錢第一的價值觀裡，道德、環保、公益，都成了
沈重無比的包袱。企業競爭無比殘酷，若不把獲利擺第一轉而關心他人，很快
地就會落於人後，只能看著沒有道德包袱的人，踩著你的頭頂揚長高歌而去。
一旦加入這種賽局，企業要存活壯大，除了拼命擴張利潤，還有選擇餘地嗎？
因此高唱關心環保，捐點小錢做些慈善公益事業，已經是值得大書特書的高貴
企業情操了，面對這樣的世界不玩行嗎？金錢囚錮了一切，無人，無人能獲得
緩刑。
""",
        'medium': u'壓克力鋁板',
        'dimensions': '244x122cm',
        'year': '2012',
        'source': u'洪天宇_煉獄場的遊戲.jpg',
      },
      {
        'title': u'儘管去做吧！',  
        'description': u"""
一個男人從鏡頭的遠方跑來，縱身一跳，慢動作呈現彈起、空中漫
步、落地、沙土揚起，在這三十秒內聽到劉易士的聲音隨著腳步響起
：「我生平第一次跳遠很好笑，只跳了九英呎，但我對自己說：『別放
棄』。高中時我總是得第二名，當時我可以就此放棄跳遠，但我依然相信
一個人不可以輕易放棄，一旦這信念成為你的信仰，你的成就將難以估
量。」好美啊！真是振奮人心。<br/>
<br/>
耐吉總能推出一支又一支動人心弦的廣告，展現品牌的戰鬥力、決
心、成就、樂趣，和運動後的心靈飽足，推出 「just do it！」口號之後，
更是完全迎合青少年衝動叛逆自我超越的雄心。如今青少年的神不在教堂
寺廟裡，而在球場上奔馳；神不在古典經典裡而在螢幕轉播中。品牌在我
們的文化中創造了最鮮明的神祇，給了我們最強大的圖像，企業成功的造
神運動，掀起一波又一波的消費狂潮。走在全球各處大城小鎮，隨處可見
耐吉標誌聳立的祭壇。群眾淹沒在消費洪流中，被廣告催眠到早已沒剩多
少判斷思考能力。這時如果問：要燒墾多少雨林，要闢多少牧場，要殺多
少頭牛，要用多少皮革，才能滿足全球消費者購買新鞋的衝動？真的很不
上道。<br/>
<br/>
美國是否還信仰上帝，恐怕連美國人自已也說不清了。聖經十誡嚴禁
人們崇拜偶像，拜資本主義賺錢有理之賜，美國已是全球偶像最大產出與
輸出的國度，即便摩西在世，恐怕也不是喬丹的對手，更別說擊毀金牛
了。
""",
        'medium': u'壓克力鋁板',
        'dimensions': '244x122cm',
        'year': '2012',
        'source': u'洪天宇_儘管去做吧.jpg',
      },
      {
        'title': u'就用石油來解渴吧',  
        'description': u"""
美國雪佛蘭石油公司，多年來在亞馬遜河探勘石油、傾倒龐大的有毒廢料，
透過河流及地下水的擴散，將原本是世外桃源的天堂國度，變成了毒龍潭。當
地原住民持續受到不明病痛折磨，離最近的醫院要八小時，族人陸陸續續被癌
症帶走。隨著河裡魚群消失，只能仰賴少數家禽為生。不斷出生的畸形兒，更
是讓族群難以為繼。身為美國第二大的石油能源公司，始終不願對汙染負起任
何責任。以美國國力的優勢，加上法律的善解，冗長的官司應該可以順利打到
下個世紀。<br/>
<br/>
無論地下黑金藏在地球那個角落，只要沒被發掘佔領，都能提供各大石油公
司各顯神通，遊戲規則是趕在別人還沒榨乾之前趁早下手。反正被吸吮的土地
最後註定要淪為爛攤子，因此肆無忌憚地掠奪，不到盡頭絕不可罷休。何況普
世相信只要你有錢，法律、公理都比較容易站在你這一邊。我們羨慕富人，討
厭窮人，原始、貧窮、落後原本就該接受懲罰，不是嗎？
""",
        'medium': u'壓克力鋁板',
        'dimensions': '244x122cm',
        'year': '2012',
        'source': u'洪天宇_就用石油來解渴吧.jpg',
      },               
    ],
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
