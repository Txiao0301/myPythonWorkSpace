import requests

url = 'https://movie.douban.com/subject/26794435/comments'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Cache-Control': 'max-age=0',
    # 'Connection': 'keep-alive',
    'Cookie': 'll="118297"; bid=-1NOicrmqeM; __utmz=30149280.1583049519.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1583049519.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __yadk_uid=hqpFf8haOZzhwOTAxmqMDVAuCDprIUXk; __gads=ID=7fd885fb2a543381:T=1583049552:S=ALNI_MbWoXbOSSkXgTOL7TDGaiqwF-75Dw; _vwo_uuid_v2=DC15CC4FC61DDB97E73CCA6400B9BE3A8|c836ef8c89b984b37baa8ca9e82da7ae; ct=y; douban-fav-remind=1; ps=y; push_noty_num=0; push_doumail_num=0; __utmv=30149280.21245; douban-profile-remind=1; __utmc=30149280; __utmc=223695111; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1583115232%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DqfyKmqkRwMSqfTDrxJT4ScCquj8ySox4PN41d-6EMwpjN41CMAJZg5GWra520P01%26wd%3D%26eqid%3D805492130001290c000000035e5b6b2b%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.352464785.1583049519.1583073691.1583115233.4; __utma=223695111.2004760075.1583049519.1583073691.1583115232.4; dbcl2="212455195:LXP4XjWDLyQ"; ck=kpsR; __utmt=1; __utmb=30149280.8.5.1583120672613; _pk_id.100001.4cf6=7398fe9fc327e41d.1583049519.3.1583120772.1583078949.; __utmb=223695111.17.10.1583115233,',
    # 'Host': 'movie.douban.com',
    # 'Sec-Fetch-Dest': 'document',
    # 'Sec-Fetch-Mode': 'navigate',
    # 'Sec-Fetch-Site': 'none',
    # 'Sec-Fetch-User': '?1',
    # 'Upgrade-Insecure-Requests': '1'
}
params = {
    'start': '480',
    'limit': '20',
    'sort': 'new_score',
    'status': 'P'
}
response = requests.get(url=url, params=params, headers=headers)
print(response.status_code)
print(response.url)

