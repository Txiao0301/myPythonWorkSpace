import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}


def write_video(mp4_url, mp4_title):
    response = requests.get(mp4_url, headers=headers)
    response.encoding = response.apparent_encoding
    # f = open(mp4_title+'.mp4', mode='wb')
    # f.write(response.content)
    # f.close()
    with open(f'{mp4_title}.mp4', mode='wb') as f:
        f.write(response.content)


url = 'https://www.pearvideo.com/video_1651975'
res = requests.get(url, headers=headers)
mp4_url = re.findall('srcUrl="(.*?)"', res.text)[0]
mp4_title = re.findall('<title>(.*?)</title>', res.text)[0]
write_video(mp4_url, mp4_title)
