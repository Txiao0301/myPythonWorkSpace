from pyquery import PyQuery as pq

html = '''
<div>
    <ul>
        <li class="item-0">first item</li>
        <li class="item-1"><a href="lin2.html">second item</a></li>
        <li class="item-0 active"><a href="lin3.html"><span class="bold">third item</span></a></li>
        <li class="item-1 active"><a href="lin4.html">fourth item</a></li>
        <li class="item-0"><a href="lin5.html">fifth item</a></li>
    </ul>
</div>
'''

doc = pq(html)
# print(doc('li'))

list_data = doc('li').items()
for li in list_data:
    print(li)
    print(li.attr('class'))
    print(li.text())
    print(li.html())

# print(doc('.item-1.active').text())

# print(doc('.item-0.active a').attr('href'))
