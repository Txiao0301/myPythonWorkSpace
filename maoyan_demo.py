import requests
from lxml import etree
import csv


class maoyan(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
        }
        self.start_url = 'https://maoyan.com/board/4'
        csv_fp = open('maoyan.csv', 'w')
        self.writer = csv.writer(csv_fp)
        self.writer.writerow(['index', 'title', 'actor', 'time', 'score'])

    def get_top_list(self, params):
        response = requests.get(url=self.start_url, headers=self.headers, params=params)
        if response.status_code == 200:
            print('请求成功：' + str(params))
            self.parse_list(response)
        else:
            print('请求列表失败')

    def parse_list(self, response):
        xpath_data = etree.HTML(response.text)
        index = xpath_data.xpath('//dd/i/text()')
        title = xpath_data.xpath('//dd/div//a/text()')
        actor = xpath_data.xpath('//dd/div//p[@class="star"]/text()')
        time = xpath_data.xpath('//dd/div//p[@class="releasetime"]/text()')
        integer = xpath_data.xpath('//dd//p[@class="score"]/i[@class="integer"]/text()')
        fraction = xpath_data.xpath('//dd//p[@class="score"]/i[@class="fraction"]/text()')
        for i in range(0, len(index)):
            data = []
            data.append(index[i])
            data.append(title[i])
            data.append(actor[i].strip())
            data.append(time[i])
            data.append(integer[i] + fraction[i])
            self.write_into_csv(data)

    def write_into_csv(self, data):
        self.writer.writerow(data)

    def start(self):
        for i in range(0, 10):
            num = i * 10
            data = {
                'offset': num
            }
            self.get_top_list(data)


maoyan().start()
