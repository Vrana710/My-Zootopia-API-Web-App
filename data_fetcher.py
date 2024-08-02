import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv('API_KEY')
API_URL = 'https://api.api-ninjas.com/v1/animals'

def fetch_data(animal_name):
    headers = {
        'X-Api-Key': API_KEY
    }
    params = {
        'name': animal_name
    }
    response = requests.get(API_URL, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return []

if __name__ == "__main__":
    animal_name = input("Enter an animal name to fetch data: ")
    data = fetch_data(animal_name)
    print(data)
