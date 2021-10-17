from bs4 import BeautifulSoup
import urllib.request


req = urllib.request.urlopen('https://www.ua-football.com/')
html = req.read()
soup = BeautifulSoup(html,"html.parser")
news = soup.find_all('li', class_= 'mb-3' )

result = []
for item in news:
     title = item.find('span', class_='fz-16 fw-500 heading').get_text(strip=True)
     desc = item.find('span', class_='d-block').get_text(strip=True)
     href = item.find('href')
     result.append({
          'title': title,
          'desc': desc,
          'href': href
     })
     print(result)
