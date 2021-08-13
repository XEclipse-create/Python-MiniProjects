import urllib.request
from bs4 import BeautifulSoup

class Scrap:
    def __init__(self,site1):
        self.site=site
    
    def scrape(self):
        s = urllib.request.urlopen(self.site)
        html = s.read()
        parser = "html.parser"

        r = BeautifulSoup(html,parser)

        for t in r.find_all("a"):
            url = t.get("href")
            if url is None:
                continue
            if "articles" in url:
                print("\n" +url)

n = "https://news.google.com/"
Scrap(n).scrape()
    
