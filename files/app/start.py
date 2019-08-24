import requests
from bs4 import BeautifulSoup



def main():
    page = requests.get('https://www.300solutions.com/')

    # Create a BeautifulSoup object
    soup = BeautifulSoup(page.text, 'html.parser')
    for href in soup.find_all(href=True):
        print(href.attrs)  

if __name__ == '__main__':
    main()