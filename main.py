import requests
from bs4 import BeautifulSoup

URL = "https://www.rentacar-rhodes.com/search-car-hire-rhodes?location_from=5&date_from=27-08-2022&time_from=07%3A00&location_to=5&date_to=06-09-2022&time_to=23%3A00&coupon_code=&age=age2#results-alerts"
website = requests.get(URL)
results = BeautifulSoup(website.content, 'html.parser')

prices = results.find_all('span', id='10-base')
for price in prices:
    print (price.text)