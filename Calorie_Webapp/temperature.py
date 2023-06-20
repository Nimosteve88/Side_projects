from selectorlib import Extractor
import requests


class Temperature:
    headers = {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    base_url = 'https://www.timeanddate.com/weather/'
    yml_path = 'temperature.yaml'

    def __init__(self, country, city):
        #in case there's any spaces withon the country or/and city, the space will be replaced with '-'
        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")

    def _build_url(self): # constructs the url
        url = self.base_url + self.country + "/" + self.city
        return url

    def _scrape(self):
        #performs the web scraping in order to get the required temp
        url = self._build_url()
        extractor = Extractor.from_yaml_file(self.yml_path) #calls xml path from yaml file
        r = requests.get(url, headers=self.headers) #gains the contents
        full_content = r.text # converts the contents within the dictionary into strings
        raw_content = extractor.extract(full_content) #this should extract the info we're looking for but
        # it won't be in the correct form. This is sorted out later
        return raw_content

    def get(self):
        scraped_content = self._scrape()

        return float(scraped_content['temp'].replace("\xa0°C", "").strip()) # Reconstructs the raw_content in order to
        # to correctly view the kind of temp we want


if __name__ == "__main__":
    temperature = Temperature(country="usa", city="san francisco")
    print(temperature.get())
