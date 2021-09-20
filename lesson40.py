import bs4
import requests

# gets webpage
res = requests.get("https://en.wikipedia.org/wiki/Main_Page")
# checks to see if there are any issues grabbing page
res.raise_for_status()
# indicating what kind of webpage you are grabbing
soup = bs4.BeautifulSoup(res.text, "html.parser")
# grabbing specific element from page
elems = soup.select('#mp-tfa > p:nth-child(2) > b:nth-child(1) > a:nth-child(1)')
print(elems[0].text)

