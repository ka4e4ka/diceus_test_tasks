import base_api

# Test Cases
if __name__ == "__main__":
    # TEST CASE 1: Positive scenario for creating a pet
    new_pet_data = {
        "id": 12345,
        "name": "Fluffy",
        "status": "available"
    }
    rp = base_api.create_pet(new_pet_data)
    print("Test Case 1 (Create Pet) - Passed") if rp.status_code == 200 else print("Test Case 1 (Create Pet) - Failed")

    # TEST CASE 2: Positive scenario for retrieving a pet by its ID
    pet_id_to_get = 12345
    rp = base_api.get_pet_by_id(pet_id_to_get)
    print("Test Case 2 (Get Pet by ID) - Passed") if rp.status_code == 200 else print("Test Case 2 (Get Pet by ID) - Failed")

    # TEST CASE 3: Positive scenario for updating a pet
    updated_pet_data = {
        "id": 12345,
        "name": "Fluffy",
        "status": "sold"
    }
    rp = base_api.update_pet(pet_id_to_get, updated_pet_data)
    print("Test Case 3 (Update Pet) - Passed") if rp.status_code == 200 else print("Test Case 3 (Update Pet) - Failed")

    # TEST CASE 4: Negative scenario for retrieving a non-existent pet
    non_existent_pet_id = 99999
    rp = base_api.get_pet_by_id(non_existent_pet_id)
    print("Test Case 4 (Get Non-Existent Pet by ID) - Passed") if rp.status_code == 400 else print("Test Case 4 (Get Non-Existent Pet by ID) - Failed")

    # TEST CASE 5: Negative scenario for deleting a non-existent pet
    rp = base_api.delete_pet(non_existent_pet_id)
    print("Test Case 5 (Delete Non-Existent Pet) - Passed") if rp.status_code == 404 else print("Test Case 5 (Delete Non-Existent Pet) - Failed")

    # TEST CASE 6: Positive scenario for creating a user
    new_user_data = {
        "id": 12345,
        "username": "john_doe",
        "email": "john.doe@example.com",
        "phone": "123-456-7890"
    }
    rp = base_api.create_user(new_user_data)
    print("Test Case 6 (Create User) - Passed") if rp.status_code == 200 else print("Test Case 6 (Create User) - Failed")

    # TEST CASE 7: Positive scenario for retrieving a user by their username
    username_to_get = "john_doe"
    rp = base_api.get_user_by_username(username_to_get)
    print("Test Case 7 (Get User by Username) - Passed") if rp.status_code == 200 else print("Test Case 7 (Get User by Username) - Failed")

    # TEST CASE 8: Positive scenario for updating a user
    updated_user_data = {
        "id": 12345,
        "username": "john_doe",
        "email": "john.doe.updated@example.com",
        "phone": "987-654-3210"
    }
    rp = base_api.update_user(username_to_get, updated_user_data)
    print("Test Case 8 (Update User) - Passed") if rp.status_code == 200 else print("Test Case 8 (Update User) - Failed")

    # TEST CASE 9: Negative scenario for retrieving a non-existent user
    non_existent_username = "non_existent_user"
    rp = base_api.get_user_by_username(non_existent_username)
    print("Test Case 9 (Get Non-Existent User by Username) - Passed") if rp.status_code == 404 else print("Test Case 9 (Get Non-Existent User by Username) - Failed")

    # TEST CASE 10: Negative scenario for deleting a non-existent user
    rp = base_api.delete_user(non_existent_username)
    print("Test Case 10 (Delete Non-Existent User) - Passed") if rp.status_code == 404 else print("Test Case 10 (Delete Non-Existent User) - Failed")

    # TEST CASE 11: Positive scenario for placing a new order
    new_order_data = {
        "id": 12345,
        "petId": 54321,
        "quantity": 1,
        "shipDate": "2023-07-18T12:00:00.000Z",
        "status": "placed"
    }
    rp = base_api.place_order(new_order_data)
    print("Test Case 11 (Place Order) - Passed") if rp.status_code == 200 else print("Test Case 11 (Place Order) - Failed")

    # TEST CASE 12: Positive scenario for retrieving an order by its ID
    order_id_to_get = 12345
    rp = base_api.get_order_by_id(order_id_to_get)
    print("Test Case 12 (Get Order by ID) - Passed") if rp.status_code == 200 else print("Test Case 12 (Get Order by ID) - Failed")

    # TEST CASE 13: Negative scenario for deleting a non-existent order
    non_existent_order_id = 99999
    rp = base_api.delete_order(non_existent_order_id)
    print("Test Case 13 (Delete Non-Existent Order) - Passed") if rp.status_code == 404 else print("Test Case 13 (Delete Non-Existent Order) - Failed")
