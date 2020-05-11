import requests
import json
import re
import os


class pvpSpider(object):
    def __init__(self):
        self.header = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }
        self.start_url = 'https://pvp.qq.com/web201605/js/herolist.json'
        self.dir_name = '王者荣耀皮肤'

    def get_list(self, start_url):
        response = requests.get(start_url, headers=self.header)
        if response.status_code == 200:
            self.parse_list_data(response)

    def parse_list_data(self, resopnse):
        data = resopnse.text
        data_list = json.loads(data)
        for info in data_list:
            self.get_detail(info.get('ename'))

    def get_detail(self, index):
        url = 'https://pvp.qq.com/web201605/herodetail/' + str(index) + '.shtml'
        response = requests.get(url, headers=self.header)
        if response.status_code == 200:
            self.parse_detail(index, response)

    def parse_detail(self, index, response):
        response.encoding = response.apparent_encoding
        data = re.findall('<ul class="pic-pf-list pic-pf-list3" data-imgname="(.*?)">', response.text)[-1]
        if data:
            img_list = str(data).split('|')
            if img_list:
                for i in range(len(img_list)):
                    img_url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(index) + '/' + str(
                        index) + '-bigskin-' + str(i + 1) + '.jpg'
                    img_name = img_list[i]
                    self.down_img(img_url, img_name)

    def down_img(self, url, img_name):
        img = requests.get(url, headers=self.header, timeout=30)
        if img_name:
            img_name = img_name.split('&')[0]

        if not os.path.exists(self.dir_name):
            os.mkdir(self.dir_name)

        with open(self.dir_name + '/' + img_name + '.jpg', 'wb')as f:
            f.write(img.content)

    def start(self):
        self.get_list(self.start_url)


pvpSpider().start()
