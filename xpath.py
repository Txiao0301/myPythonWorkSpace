import requests
from lxml import etree

url = 'http://news.baidu.com/'
# url = 'https://www.8btc.com/author?page=1'
response = requests.get(url)
xpath_data = etree.HTML(response.text)
result = etree.tostring(xpath_data, encoding='utf-8')
print(result)
# 节点 /
result = xpath_data.xpath('/html/head/title/text()')
# 跨节点 //
result = xpath_data.xpath('//a/text()')
# 标签包裹的内容 text()
result = xpath_data.xpath('//a[@mon="ct=1&a=2&c=top&pn=2"]/text()')
# 标签的属性 @属性名
result = xpath_data.xpath('//a[@mon="ct=1&a=2&c=top&pn=2"]/@href')
print(result)
