import requests
import bs4

# GRABBING PAGE TITLE:
result = requests.get("https://example.com/")
soup = bs4.BeautifulSoup(result.text, "lxml")
page_title = soup.select('title')[0].getText()

# GRABBING All ELEMENTS OF A CLASS:
res = requests.get("https://en.wikipedia.org/wiki/FC_Nasaf")
soup2 = bs4.BeautifulSoup(res.text, "lxml")

players_list = [player.getText() for player in soup2.select('.fn')]

# GRABBING AN IMAGE:
response = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup3 = bs4.BeautifulSoup(response.text, "lxml")

computer_img = soup3.select(".thumbimage")[0]
image_link = requests.get(f"https:{computer_img['src']}")

f = open('/Users/jakhongir/desktop/computer.jpg', 'wb')
f.write(image_link.content)
f.close()

