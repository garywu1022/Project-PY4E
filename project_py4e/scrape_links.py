import requests
from bs4 import BeautifulSoup
import re

def get_links(url):
    r = requests.get(url)
    sp = BeautifulSoup(r.text, 'html.parser')
    links = sp.select('td.cellinside a')
    #print(links)
    return [link.attrs['href'] for link in links]

links = get_links('https://vincentarelbundock.github.io/Rdatasets/datasets.html')

csv_lst = []
ct = 0
for link in links:
    link = re.findall('^https://\S+csv', link)
    #print(link)
    if len(link) < 1:
        continue
    else:
        csv_lst.append(link[0])
        ct = ct + 1
#print(csv_lst)
print('retrieved', ct, 'links')

with open('csv_to_download.txt', 'w') as f:
    for d_link in csv_lst:
        d_link = d_link + '\n'
        f.write(d_link)
print('txt file downloaded')