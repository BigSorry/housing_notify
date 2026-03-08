import os
import requests
import bookkeep
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from base64 import b64decode

def get_request():
    # Access the API key and private key from environment variables
    load_dotenv()
    API_KEY = os.getenv("ZYTE_KEY")
    api_response = requests.post(
        "https://api.zyte.com/v1/extract",
        auth=(API_KEY, ""),
        json={
            "url": "https://www.pararius.nl/huurwoningen/"
                   "amersfoort/500-1200/straal-50/25m2/sinds-1",
            "httpResponseBody": True,
            "device": "desktop",
            "followRedirect": True,
        },
    )
    http_response_body: bytes = b64decode(
        api_response.json()["httpResponseBody"])
    return http_response_body

def extract_listings(soup_html, base_url="www.pararius.nl"):
    listings_result = []
    extracted_listing = [li for li in soup_html.find_all('li', class_='search-list__item search-list__item--listing')]
    for list in extracted_listing:
        link = base_url + list.find('a', class_='listing-search-item__link--title')['href']
        price = soup.find('div', class_='listing-search-item__price').find('span').text
        # features such as  ['69 m²', '3 kamers', 'Kaal']
        div = list.find('div', class_='listing-search-item__features')
        room_features = [li.text.strip() for li in div.find_all('li')]

        listings_result.append({
            'link': link,
            'price': price,
            'features': room_features
        })

    return listings_result

if __name__ == '__main__':
    http_response_body = get_request()
    soup = BeautifulSoup(http_response_body, "html.parser")
    listings = extract_listings(soup)

    bookkeep.notify_new(listings)

