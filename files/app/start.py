import requests
from bs4 import BeautifulSoup



def main():
    page = requests.get('https://web.archive.org/')

    # Create a BeautifulSoup object
    soup = BeautifulSoup(page.text, 'html.parser')
    for href in soup.find_all(href=True):
        print(href.attrs)
        #print("Found the URL: {0}, TEXT: {1}".format(href['href'], href['text']))

    #links = [a['href'] for a in soup.find_all('a', href=True)]
    #print(links)
    #links = [a['href'] for a in soup.select('a[href]')]
    #print(links)
    #anchor = data.xpath('//a[@class="title"]/text()')
    #anchors = soup.find_all('a', {'class': 'Unique_Class_Name', 'href': True})
    #if anchor.has_attr('href'):
    #    print (anchor['href'])
    # for link in soup.findAll('a', href=True, text='TEXT'):
   

if __name__ == '__main__':
    main()