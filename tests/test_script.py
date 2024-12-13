from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # This is optional if you want automatic driver management
import time

# Set up WebDriver using the Service class
service = Service(executable_path='D:\\chromedriver_win32\\chromedriver.exe')  # Path to your chromedriver
driver = webdriver.Chrome(service=service)

try:
    # Open the homepage (ensure your Django app is running)
    driver.get("http://127.0.0.1:8000/")  # Local server URL

    # Test: Check if homepage title is correct
    print("Page title is:", driver.title)
    assert "Home" in driver.title, "Test Failed! Title doesn't match."

    # Example Test: Check if the header exists on the homepage
    header = driver.find_element(By.TAG_NAME, 'h1')
    assert header.text == "Welcome to Our Pet Adoption Website", "Test Failed! Header text doesn't match."

    # Test: Check if there are adoption posts
    adoption_posts_section = driver.find_element(By.ID, 'adoption-posts')
    assert "Latest Adoption Posts" in adoption_posts_section.text, "Test Failed! Adoption posts section not found."

    # Test: Click on the 'Login' link from homepage
    login_button = driver.find_element(By.LINK_TEXT, "Login")  # Since the login button isn't a button, using a link
    login_button.click()

    time.sleep(2)  # Wait for the login page to load

    # Test: Login functionality (using test credentials)
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    # Input login credentials (update with valid test credentials)
    username_field.send_keys("Jahid")
    password_field.send_keys("Jahid")
    password_field.send_keys(Keys.RETURN)  # Submit the form

    time.sleep(3)  # Wait for login response

    # Test: Check if login was successful (check if logout text appears)
    if "Logout" in driver.page_source:
        print("Login Test Passed!")
    else:
        print("Login Test Failed!")

    # Test: Add a new pet by navigating to the pet creation page
    add_pet_button = driver.find_element(By.LINK_TEXT, "Create Pet")  # Using the link text in pet_create.html
    add_pet_button.click()

    time.sleep(2)  # Wait for the create pet page to load

    # Fill out the "Create Pet" form (based on pet_create.html)
    pet_name_field = driver.find_element(By.NAME, "name")  # Assuming 'name' is the form field for pet's name
    pet_type_field = driver.find_element(By.NAME, "type")  # Assuming 'type' is the form field for pet's type
    pet_age_field = driver.find_element(By.NAME, "age")  # Assuming 'age' is the form field for pet's age

    # Example pet details to fill out
    pet_name_field.send_keys("Fluffy")
    pet_type_field.send_keys("Cat")
    pet_age_field.send_keys("2")

    # Submit the form to create a new pet
    pet_age_field.send_keys(Keys.RETURN)

    time.sleep(3)  # Wait for the form to be processed

    # Check if pet is added (since no success message appears, we will check if the pet exists in the list)
    driver.get("http://127.0.0.1:8000/pets/all")  # Go to the pet listing page
    time.sleep(2)

    pet_found = False
    pets = driver.find_elements(By.CLASS_NAME, 'adoption-card')
    for pet in pets:
        if "Fluffy" in pet.text and "Cat" in pet.text:
            pet_found = True
            break

    if pet_found:
        print("Add Pet Test Passed!")
    else:
        print("Add Pet Test Failed!")

finally:
    # Close the browser after the tests
    driver.quit()
