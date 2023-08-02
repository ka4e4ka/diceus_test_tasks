import requests

# Base URL for the API
BASE_URL = "https://petstore.swagger.io/v2"


# Function to send a POST request to create a new pet
def create_pet(pet_data):
    return requests.post(f"{BASE_URL}/pet", json=pet_data)


# Function to send a GET request to retrieve a pet by its ID
def get_pet_by_id(pet_id):
    return requests.get(f"{BASE_URL}/pet/{pet_id}")


# Function to send a PUT request to update a pet by its ID
def update_pet(pet_id, pet_data):
    return requests.put(f"{BASE_URL}/pet/{pet_id}", json=pet_data)


# Function to send a DELETE request to delete a pet by its ID
def delete_pet(pet_id):
    return requests.delete(f"{BASE_URL}/pet/{pet_id}")


# Function to send a POST request to create a new user
def create_user(user_data):
    return requests.post(f"{BASE_URL}/user", json=user_data)


# Function to send a GET request to retrieve a user by their username
def get_user_by_username(username):
    return requests.get(f"{BASE_URL}/user/{username}")


# Function to send a PUT request to update a user by their username
def update_user(username, user_data):
    return requests.put(f"{BASE_URL}/user/{username}", json=user_data)


# Function to send a DELETE request to delete a user by their username
def delete_user(username):
    return requests.delete(f"{BASE_URL}/user/{username}")


# Function to send a POST request to place a new order in the store
def place_order(order_data):
    return requests.post(f"{BASE_URL}/store/order", json=order_data)


# Function to send a GET request to retrieve an order by its ID
def get_order_by_id(order_id):
    return requests.get(f"{BASE_URL}/store/order/{order_id}")


# Function to send a DELETE request to delete an order by its ID
def delete_order(order_id):
    return requests.delete(f"{BASE_URL}/store/order/{order_id}")
