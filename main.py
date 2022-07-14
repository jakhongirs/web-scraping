import requests
import bs4

# GRABING PAGE TITLE:
result = requests.get("https://example.com/")
soup = bs4.BeautifulSoup(result.text, "lxml")
page_title = soup.select('title')[0].getText()

print(page_title)
