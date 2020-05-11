import requests
from bs4 import BeautifulSoup
import json
import time


class BtcSpider(object):
    def __init__(self):
        self.url = 'https://www.8btc.com/author?page={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
        }
        self.data_list = []
        self.data_desc = []

    def get_response(self, url):
        response = requests.get(url, headers=self.headers)
        data = response.content.decode(response.apparent_encoding)
        # data = response.content.decode('gbk')
        return data

    # 列表页数据解析
    def parse_data(self, data):
        soup = BeautifulSoup(data, 'lxml')
        url_list = soup.select('.author-item .author-item__info a')
        title_list = soup.select('.author-item .author-item__info .author-item__info-name')
        for index, info in enumerate(title_list):
            info_list = {}
            info_list['title'] = info.get_text().strip()
            info_list['url'] = url_list[index].get('href')
            self.data_list.append(info_list)

    # 详情页数据解析
    def parse_detail_data(self, data):
        soup = BeautifulSoup(data, 'lxml')
        info_desc = soup.select_one('.author-overview__info-desc')
        info_title = soup.select_one('.author-overview__info-name strong')
        info_item = soup.select('.author-overview__info-item span')
        desc = {'作者名字': info_title.get_text(),
                '简介': info_desc.get_text(),
                '浏览量': info_item[0].get_text(),
                '获赞数': info_item[1].get_text(),
                '粉丝数': info_item[2].get_text()}
        self.data_desc.append(desc)

    def save_data(self, data, file_name):
        print('save ' + file_name + ' begin')
        print(len(data))
        data_str = json.dumps(data)
        with open(file_name, 'w') as f:
            f.write(data_str)
        print('save ' + file_name + ' success')

    def start(self):
        for i in range(1, 4):
            time.sleep(1)
            url = self.url.format(1)
            data = self.get_response(url)
            self.parse_data(data)
        self.save_data(self.data_list, 'author_list.json')

        for data in self.data_list:
            time.sleep(1)
            detail_url = data['url']
            detail_data = self.get_response('https://www.8btc.com' + str(detail_url))
            self.parse_detail_data(detail_data)
        self.save_data(self.data_desc, 'author_detail.json')


BtcSpider().start()
