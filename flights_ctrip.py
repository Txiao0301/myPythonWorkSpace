import requests
import json
import csv
import time


class flightsSpider(object):
    def __init__(self):
        self.header = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
        self.city_list = []
        self.lowestPrice_url = 'https://flights.ctrip.com/itinerary/api/12808/lowestPrice'
        self.csv_fp = open('flights.csv', 'w')
        self.writer = csv.writer(self.csv_fp)
        sheet_title = ['flight', 'date', 'lowestPrice']
        self.writer.writerow(sheet_title)

    def get_request_by_post(self, data, city_name_s, city_name_e):
        time.sleep(5)
        requests.adapters.DEFAULT_RETRIES = 5
        s = requests.session()
        s.keep_alive = False
        try:
            print(city_name_s + '-' + city_name_e)
            response = s.post(url=self.lowestPrice_url, data=data, headers=self.header, timeout=30)
            if response.status_code == 200:
                result = json.loads(response.text).get('data').get('oneWayPrice')
                if result:
                    flight_name = ''
                    rows = []
                    for key, value in zip(result[0].keys(), result[0].values()):
                        flight = city_name_s + '-' + city_name_e
                        if flight_name == flight:
                            flight = ''
                        else:
                            flight_name = flight
                        # print(flight, key, value)
                        rows.append([flight, key, value])
                    self.writer.writerows(rows)
        except TimeoutError:
            print('TimeoutError:', data)

    def set_data(self):
        if len(self.city_list) > 0:
            for city_s in self.city_list:
                for key_s, value_s in zip(city_s.keys(), city_s.values()):
                    for city_e in self.city_list:
                        for key_e, value_e in zip(city_e.keys(), city_e.values()):
                            data = {'flightWay': 'Oneway',
                                    'dcity': value_s,
                                    'acity': value_e,
                                    'army': False}
                            self.get_request_by_post(data, key_s, key_e)
            self.csv_fp.close()

    def get_city_list(self):
        city_list = requests.get('https://flights.ctrip.com/itinerary/api/poi/get')
        data_list = json.loads(city_list.text).get('data')
        if data_list:
            for data in data_list:
                if data != '热门':
                    city_map = data_list.get(data)
                    if city_map:
                        for c_map in city_map:
                            city = city_map.get(c_map)
                            list_num = len(city)
                            for i in range(list_num):
                                c = city[i].get('data')
                                c_list = c.split('|')[-1]
                                if c_list.find(',') < 0:
                                    self.city_list.append({city[i].get('display'): c_list})
            self.set_data()

    def start(self):
        self.get_city_list()
        # data = {'flightWay': 'Oneway',
        #         'dcity': 'CHG',
        #         'acity': 'dnh',
        #         'army': False}
        # self.get_request_by_post(data, 'key_s', 'key_e')


flightsSpider().start()
