import requests
from bs4 import BeautifulSoup



def main():
    page = requests.get('https://web.archive.org/')

    # Create a BeautifulSoup object
    soup = BeautifulSoup(page.text, 'html.parser')
    for href in soup.find_all(href=True):
        print("Found the URL:", href['href'])


if __name__ == '__main__':
    main()