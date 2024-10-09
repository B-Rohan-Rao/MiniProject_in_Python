from pprint import pprint
import requests
from requests.auth import HTTPBasicAuth


# Uncomment the following lines and add your details.-->
# SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/90383c42299726f435a4729f32d694c4/flightDeals/prices"
# SHEETY_USRERNAME = "YOUR_SHEETY_USER_NAME"
# SHEETY_PASSWORD = "YOUR_SHEETY_PASSWORD"
# AUTORIZATION_HEADER = "YOUR_SHEETY_AUTORIZATION_HEADER"


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
