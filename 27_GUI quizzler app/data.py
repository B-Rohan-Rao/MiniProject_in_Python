import requests

parameters = {
    "amount": 20,
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php?", params=parameters)
question_list = response.json()
# print(question_list["results"])
question_data = question_list["results"]

