import requests

parameter={
    "amount":10,
    "type":"boolean"
}
requested_api = requests.get(url="https://opentdb.com/api.php", params=parameter)
requested_api.raise_for_status()
question_data = requested_api.json()["results"]
