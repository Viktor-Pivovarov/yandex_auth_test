import requests
import json
import os
import logging

# Define constants for data directory and the path to the users.json file
DATA_DIR = "data"
USERS_JSON_PATH = os.path.join(DATA_DIR, "users.json")
API_ENDPOINT = "https://jsonplaceholder.typicode.com/users"


logging.basicConfig(level=logging.INFO)

def save_data_to_json(data):
    try:
        with open(USERS_JSON_PATH, 'w') as file:
            json.dump(data, file)
    except Exception as e:
        logging.error(f"Error saving data to JSON: {e}")

def load_data_from_json()->dict:
    try:
        if os.path.exists(USERS_JSON_PATH):
            with open(USERS_JSON_PATH, 'r') as file:
                return json.load(file)
    except Exception as e:
        logging.error(f"Error loading data from JSON: {e}")
    return None

def fetch_user_data()->dict:
    """
    Fetch user data from the API. If the API call fails, it attempts to load data from a local JSON file.
    """
    try:
        response = requests.get(API_ENDPOINT)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        data = response.json()
        save_data_to_json(data) 
        logging.info("Fetched data from API and saved to local JSON.")
        return data
    except requests.RequestException as e:
        logging.error(f"Error fetching data from API: {e}")
        logging.info("Attempting to load data from local JSON.")
        return load_data_from_json()

def get_user_credentials():
    users = fetch_user_data()
    if users:
        user = users[0]
        return user["email"], user["username"], user["website"], user["phone"]
    return None, None, None, None
