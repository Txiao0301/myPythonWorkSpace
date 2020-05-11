html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.title)  # title 元素
# <title>The Dormouse's story</title>

print(soup.p)  # 第一个 p 元素
# <p class="title"><b>The Dormouse's story</b></p>

print(soup.p['class'])  # p 元素的 class 属性
# ['title']

print(soup.p.b)  # p 元素下的 b 元素
# <b>The Dormouse's story</b>

print(soup.p.parent.name)  # p 元素的父节点的标签
# body


print(soup.find_all('a'))  # 所有 a 元素
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

print(soup.find(id='link3'))  # id 为 link3 的元素
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a
print(soup.select('html head title'))
# [<title>The Dormouse's story</title>]
print(soup.select('p > #link1'))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]