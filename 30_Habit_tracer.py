import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "jgvdsdfvloijfs"  # any token of our choice in between 8 and 120 characters. Validation rule: [ -~]{8,128}
USERNAME = "brohanrao"  # any unique username that the pixela doesn't have or has been registered.[a-z][a-z0-9-]{1,32}
GRAPH_ID = "graph1"  # Validation rule: ^[a-z][a-z0-9-]{1,16}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Creating user in PIXELA -->
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# For creating the user for the first time with the given parameters.
"""
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)
"""

# Creating graph for the existing user -->
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"  # Make sure to use the color that hase been given in the api documentation.
}


#  required to do only once in order to create the graph.
"""
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)
"""

# Updating the data using datetime module for present date.

today = datetime.now()
post_pixel_endpoint = f"{graph_endpoint}/{graph_config['id']}"
quantity = "3"
date = today.strftime("%Y%m%d")
post_pixel_config = {
    "date": date,
    "quantity": quantity
}

"""
"strftime" function is used to formate the dates any any required formate. However,  We need to use the official 
documents inorder to get the code of getting the exact word of abbreviation to use. 
for eg:- %Y is used to get the year 
         %m is used to get the month in digit 
         %d is used to get the present date of the month.
         
`https://www.w3schools.com/python/python_datetime.asp`
visit the link for more codes.👆         
"""

"""
response = requests.post(url=post_pixel_endpoint, json=post_pixel_config, headers=headers)
print(response.text)
"""


# Updating a pixel with a new value -->
update = {
    "quantity": "9.034",
}
update_endpoint = f"{post_pixel_endpoint}/{date}"

"""
response = requests.put(url=update_endpoint, json=update, headers=headers)
print(response.text)
"""


# Deleting a pixel -->

delete_endpoint = f"{post_pixel_endpoint}/{date}"
"""
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
"""

#  At last, you can visit the link to look visually your daily tracker.👇
# https://pixe.la/v1/users/<Your_Username>/graphs/<graph_id>.html
