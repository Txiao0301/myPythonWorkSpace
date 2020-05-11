import requests

movie_url = 'https://jx.618g.com/?url=https://v.qq.com/x/cover/mzc00200r2566h7.html'

text = requests.get(movie_url).text
print(text)
