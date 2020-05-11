# import urllib.robotparser
#
# rp = urllib.robotparser.RobotFileParser()
# rp.set_url("http://www.musi-cal.com/robots.txt")
# rp.read()
# rrate = rp.request_rate("*")
# rrate.requests
# rrate.seconds
# rp.crawl_delay("*")
# rp.can_fetch("*", "http://www.musi-cal.com/cgi-bin/search?city=San+Francisco")
# rp.can_fetch("*", "http://www.musi-cal.com/")

import requests
res = requests.head('http://www.baidu.com')
print(res.headers)