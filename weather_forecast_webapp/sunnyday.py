import requests



class Weather:
    """
    Creates a Weather object getting an apikey as input and
    either a city name or lat and lon coordinates
    """
    def __init__(self, apikey, city, lat=None, lon=None):
        if city or (city and lat and lon):
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apikey}&units=metric"
            r = requests.get(url)
            self.data = r.json()
        elif lat and lon:
            url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={apikey}&units=metric"
            r = requests.get(url)
            self.data = r.json()
        else:
            raise TypeError("provide either a city or lat and arguments")
        if self.data["cod"] == 200: #checks if a valid city has been inputted
            print("INVALID CITY")
            raise ValueError(self.data["message"])

    def next_12h(self):
        return self.data['list'][:4]  # provides the details we need for the next 12hrs

    def next_12h_simplified(self):  # simplifies the details from the next_12h function
        simpledata = []
        for dicty in self.data['list'][:4]:
            simpledata.append((dicty['dt_txt'],
            dicty['main']['temp'], dicty['weather'][0]['description']))
        return simpledata

    def getweathericon(self):
        simpledata = []
        for item in self.data["list"][:4]:
            icon_value = item["weather"][0]["icon"]
            simpledata.append(icon_value)
        return simpledata

