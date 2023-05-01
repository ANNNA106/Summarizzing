import requests
from bs4 import BeautifulSoup

LIMIT = True
limit = 2


def get_links(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    urls = []
    for link in soup.find_all('a'):
        s = link.get('href')
        if s != None:
            if s.startswith('/wiki'):
                s = 'https://en.wikipedia.org/' + s
            if s.startswith('#'):
                continue
            if s.startswith("//en"):
                s = "https:" + s
            if s.startswith("/w"):
                s = "https://en.wikipedia.org/" + s
            urls.append(s)
    return urls[1:]

def digger(links, n, N):
    limC = 0
    for i in links:
        if LIMIT:
            if limC == limit:
                break
            limC += 1
        _links = get_links(i)
        if len(_links) == 0 or n == 0:
            break
        print("\t"*(N-n),i,"->")
        digger(_links, n-1, N)


def main():

    links = get_links('https://en.wikipedia.org/wiki/Narendra_Modi')
    n = int(input("Enter depth: "))
    #n = 5

    digger(links, n, n)

main()