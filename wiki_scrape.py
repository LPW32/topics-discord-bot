import bs4
import requests

def getWiki(article_name):
    url = 'http://en.wikipedia.org/wiki/'+str(article_name)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    elems = soup.select('p')
    return elems[0].getText()+"\n"+"<"+url+">"

def citeStrip(string):
    ret = ''
    skipc = 0
    for i in string:
        if i == '[':
            skipc += 1
        elif i == ']' and skipc > 0:
            skipc -= 1
        elif skipc == 0:
            ret +=i
    return ret
