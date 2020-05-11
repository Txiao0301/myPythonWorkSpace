import re
import time
import os

import requests

header = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}
response = requests.get('https://www.vmgirls.com/3903.html', headers=header)
html = response.text
dirName = re.findall('<h1 class="post-title h3">(.*?)</h1>', html)[-1]
if not os.path.exists(dirName):
    os.mkdir(dirName)
# urlList = re.findall(
#     '<img alt=".*?" src=".*?" width=".*?" height=".*?" class=".*?" data-src="(.*?)" data-nclazyload=".*?">', html)
urlList = re.findall(
    '<img alt=".*?" src=".*?" width=".*?" height=".*?" class=".*?" data-src="(.*?)" data-nclazyload=".*?" data-srcset=".*?" data-sizes=".*?">',
    html)
for url in urlList:
    time.sleep(1)
    fileName = url.split('/')[-1]
    if not os.path.exists(dirName + '/' + fileName):
        img = requests.get(url, headers=header, timeout=30)
        with open(dirName + '/' + fileName, 'wb') as f:
            f.write(img.content)
