import requests
from bs4 import BeautifulSoup


pagecount = 17
baseurl = "https://www.firmenabc.at/firmen/wolkersdorf-im-weinviertel_Lkn/"
hrefs = []
i = 1
while i < pagecount:
    url = baseurl + str(i) 
    print("requesting " + url)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    elements = soup.find_all(class_="btn-round bg-light-blue")
    hrefs += [element['href'] for element in elements if 'href' in element.attrs]
    i = i + 1

with open("output.txt", 'w') as file:
    for href in hrefs:
        file.write(href+ '\n')
        print(href)
    
input()