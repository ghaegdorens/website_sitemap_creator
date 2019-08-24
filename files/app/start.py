import requests
from bs4 import BeautifulSoup



def main():
    page = requests.get('https://web.archive.org/')

    # Create a BeautifulSoup object
    soup = BeautifulSoup(page.text, 'html.parser')

    print(soup)
 


if __name__ == '__main__':
    main()