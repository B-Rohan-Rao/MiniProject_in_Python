from pprint import pprint
import requests
from requests.auth import HTTPBasicAuth

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/90383c42299726f435a4729f32d694c4/flightDeals/prices"
SHEETY_USRERNAME = "Rohan"
SHEETY_PASSWORD = "2003@Rohan"
AUTORIZATION_HEADER = "Basic Um9oYW46MjAwM0BSb2hhbg=="


class DataManager:

    def __init__(self):
        self._user = SHEETY_USRERNAME
        self._password = SHEETY_PASSWORD
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.header = {
            "Authorization": AUTORIZATION_HEADER
        }
        self.destination_data = {}

    def get_destination_data(self):
        """
        # Use the Sheety API to GET all the data in the Google sheet.
        """
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.header)
        data = response.json()
        self.destination_data = data["prices"]
        # pprint(data)
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.header
            )
            print(response.text)
