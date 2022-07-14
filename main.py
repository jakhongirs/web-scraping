import requests
import bs4

# GRABING PAGE TITLE:
result = requests.get("https://example.com/")
soup = bs4.BeautifulSoup(result.text, "lxml")
page_title = soup.select('title')[0].getText()

# GRABING All ELEMENTS OF A CLASS:
res = requests.get("https://en.wikipedia.org/wiki/FC_Nasaf")
soup2 = bs4.BeautifulSoup(res.text, "lxml")

players_list = [player.getText() for player in soup2.select('.fn')]


