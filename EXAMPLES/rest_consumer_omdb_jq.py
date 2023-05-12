import requests
from pprint import pprint

API_KEY = 'b87452b6'

OMDB_URL = "http://www.omdbapi.com"

def main():
    requests_params = {'t': 'Black Panther', "apikey": API_KEY}
    response = requests.get(OMDB_URL, params=requests_params, timeout=5)
    if response.status_code == requests.codes.OK:  # 200
        pass
    else:
        print(f"response.status_code: {response.status_code}")

if __name__ == '__main__':
    main()


