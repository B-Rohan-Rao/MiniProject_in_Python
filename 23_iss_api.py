import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")  # <--The string is the url of the api
# ".get()" is the method used to get the request from the api endpoint
print(response)
# print(response.status_code)
"""Depending on the starting number of the response code, we can determine the v we got from the request.
1XX :- The request is being processed or the result you are seeing is not final.
2XX :- You have got the result.
3XX :- The site is redirecting.
4XX :- The thing you are looking for doesn't exist.( Most common that can be seen is `404 error`)
5XX :-  There is a problem with the server and is not able to process the request.
"""

response.raise_for_status()  # This is going to raise the exact error for us if the request is unsuccessful.

data = response.json()  # This data is in the form of dic. So we can treat this as the dictionary.

latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]
iss_position = (latitude, longitude)

print(iss_position)
