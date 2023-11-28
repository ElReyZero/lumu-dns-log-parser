import requests

API_URL = "https://api.lumu.io"

def send_data_to_api(data, collector_id, client_key):
    for i in range(0, len(data), 500):
        requests.post(API_URL+f"/collectors/{collector_id}/dns/queries?key={client_key}", json=data[i:i+500])