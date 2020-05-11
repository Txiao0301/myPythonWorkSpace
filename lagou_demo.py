import requests
import time


class lagouSpider(object):

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
            'Host': 'www.lagou.com',
            'Origin': 'https://www.lagou.com',
            'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
        }
        self.start_url = 'https://www.lagou.com/jobs/positionAjax.json?px=new&needAddtionalResult=false'

    def get_cookie(self):
        url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
        response = requests.get(url=url, headers=self.headers)
        return response.cookies

    def start_requests(self, page_num):
        data = {'first': True,
                'pn': page_num,
                'kd': 'python'
                }
        response = requests.post(url=self.start_url, data=data, headers=self.headers, cookies=self.get_cookie())
        self.parse_response(response, page_num)

    def parse_response(self, response, page_num):
        result = response.json()
        if result['msg'] is None:
            print('第' + str(page_num) + '页，请求成功')
            data_list = result['content']['positionResult']['result']
            if len(data_list) > 0:
                for data in data_list:
                    d = {
                        'positionId': str(data['positionId']),
                        'positionName': data['positionName'],
                        'companyFullName': data['companyFullName'],
                        'companySize': data['companySize'],
                        'industryField': data['industryField'].replace(',', ' '),
                        'financeStage': data['financeStage'],
                        'createTime': data['createTime'],
                        'city': data['city'],
                        'salary': data['salary'],
                        'workYear': data['workYear'],
                        'jobNature': data['jobNature'],
                        'education': data['education'],
                    }
                    print(d)
                    with open('lagou.csv', mode='a', encoding='utf-8')as f:
                        values = d.values()
                        f.write(','.join(values))
                        f.write('\n')
        else:
            print(result['msg'])
            time.sleep(10)
            self.start_requests(page_num)

    def start(self):
        for n in range(1, 31):
            self.start_requests(n)


lagouSpider().start()
