from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time
import random

# ====================================================================================
# HOW TO USE THIS SCRIPT:
# 1. Install Selenium: Run `pip install selenium` in your terminal.
# 2. Download Geckodriver: Get it from https://github.com/mozilla/geckodriver/releases.
# 3. Update the code below to match your form:
#    - Change the XPath for the "Submit" button if needed.
#    - Add or modify fields in the `auto_fill_form` function.
#    - Update the lists of names, brands, etc., if necessary.
# 4. Run the script: `python Form.py`
# ====================================================================================

# Message for users about the "Start Now" button
print("Important: If your form has a 'Start Now' button, remove it by going to the form >")
print("1. Open the form in edit mode.")
print("2. Click on the 'Style' tab.")
print("3. Select the 'Top Left' layout option.")
print("4. Save your changes.\n")

# Lists of names for random selection
male_names = ["Ahmed", "Mohamed", "Ali", "Omar", "Youssef", "Abdul", "Hassan", "Hussein", "Ibrahim", "Khalid"]
female_names = ["Fatima", "Aisha", "Layla", "Zainab", "Mariam", "Nadia", "Leila", "Rania", "Yara", "Ananya"]

# Function to randomly select a name based on gender
def get_random_name(gender):
    if gender == "Male":
        return random.choice(male_names)
    else:
        return random.choice(female_names)

# Function to randomly select a gender
def get_random_gender():
    return random.choice(["Male", "Female"])

# Function to randomly select an age between 15 and 25
def get_random_age():
    return random.randint(15, 25)

# Function to randomly select a phone type
def get_random_phone_type():
    return random.choice(["iPhone", "Android", "Feature Phone"])

# Function to randomly select a favorite smartphone brand
def get_random_favorite_brand():
    return random.choice(["Apple", "Samsung", "Huawei", "Xiaomi", "Oppo"])

# Function to randomly select a primary reason for using a phone
def get_random_reason():
    return random.choice(["Communication", "Entertainment", "Work", "Social Media"])

# Function to randomly select a place where the phone is used the most
def get_random_place():
    return random.choice(["Home", "Work", "Public Places", "School"])

# Function to randomly select a frequently used mobile application
def get_random_app():
    return random.choice(["WhatsApp", "Instagram", "TikTok", "Facebook", "Snapchat"])

# Function to randomly select the number of social media apps installed
def get_random_social_media_apps():
    return random.randint(1, 10)

# Function to randomly select the number of phones owned
def get_random_phones_owned():
    return random.randint(1, 3)

# Function to randomly select the number of times the phone is checked per day
def get_random_phone_checks():
    return random.randint(10, 100)

# Function to randomly select the storage used on the phone (realistic sizes)
def get_random_storage_used():
    return random.choice([16, 32, 64, 128, 256, 512, 1024])

# Function to randomly select the number of years using a smartphone
def get_random_years_using_smartphone():
    return random.randint(1, 10)

# Function to automatically fill out the form
def auto_fill_form(driver):
    time.sleep(3)  # Wait for the form to load
    fields = driver.find_elements(By.XPATH, "//input | //textarea | //select")  # Find all form fields

    for field in fields:
        try:
            field_type = field.get_attribute("type")  # Get the type of the field (text, number, etc.)
            field_name = field.get_attribute("name") or field.get_attribute("aria-label") or "Unknown Field"  # Get the field name

            # Handle text fields
            if field_type == "text" or field_type is None:
                field.clear()  # Clear the field before filling it
                if "name" in field_name.lower():
                    field.send_keys(get_random_name(get_random_gender()))  # Fill with a random name
                elif "age" in field_name.lower():
                    field.send_keys(str(get_random_age()))  # Fill with a random age
                elif "phone" in field_name.lower():
                    field.send_keys(get_random_phone_type())  # Fill with a random phone type
                elif "brand" in field_name.lower():
                    field.send_keys(get_random_favorite_brand())  # Fill with a random brand
                elif "reason" in field_name.lower():
                    field.send_keys(get_random_reason())  # Fill with a random reason
                elif "place" in field_name.lower():
                    field.send_keys(get_random_place())  # Fill with a random place
                elif "app" in field_name.lower():
                    field.send_keys(get_random_app())  # Fill with a random app
                elif "storage" in field_name.lower():
                    field.send_keys(str(get_random_storage_used()))  # Fill with a random storage size
                elif "years" in field_name.lower():
                    field.send_keys(str(get_random_years_using_smartphone()))  # Fill with random years
                else:
                    field.send_keys("Random Text")  # Default text for unknown fields

            # Handle number fields
            elif field_type == "number":
                field.clear()
                field.send_keys(str(random.randint(1, 100)))  # Fill with a random number

            # Handle radio buttons
            elif field_type == "radio":
                if not field.is_selected():
                    field.click()  # Select the radio button if not already selected

            # Handle checkboxes
            elif field_type == "checkbox":
                if random.choice([True, False]):
                    field.click()  # Randomly check or uncheck the checkbox

            # Handle date fields
            elif field_type == "date":
                field.clear()
                field.send_keys("2023-10-15")  # Fill with a fixed date (adjust as needed)

            # Handle dropdowns
            elif field.tag_name == "select":
                options = field.find_elements(By.TAG_NAME, "option")
                if options:
                    random.choice(options).click()  # Select a random option from the dropdown
        except Exception as e:
            print(f"Error filling field {field_name}: {e}")

# Configure Firefox options (run in headless mode)
firefox_options = Options()
firefox_options.headless = True  # Run without opening a browser window
firefox_options.add_argument("--disable-gpu")  # Disable GPU for headless mode

# Path to Geckodriver (update this to your Geckodriver path)
geckodriver_path = "/usr/local/bin/geckodriver"  # Replace with the actual path

# Initialize the Firefox WebDriver
try:
    driver = webdriver.Firefox(service=Service(geckodriver_path), options=firefox_options)
except Exception as e:
    print(f"Error initializing WebDriver: {e}")
    exit(1)

# Ask the user for the form URL and number of submissions
form_url = input("Enter the form URL: ")
num_submissions = int(input("How many times do you want to fill the form? "))

# Start filling the form
for i in range(num_submissions):
    try:
        driver.get(form_url)  # Open the form URL
        time.sleep(5)  # Wait for the form to load
        auto_fill_form(driver)  # Fill out the form

        # Submit the form
        try:
            submit_button = driver.find_element(By.XPATH, "//button[text()='Submit']")  # Find the submit button
            submit_button.click()  # Click the submit button
            print(f"Form submitted successfully! ({i + 1}/{num_submissions})")
        except Exception as e:
            print(f"Error submitting form: {e}")

        # Clear cookies and refresh the page to reset the form
        driver.delete_all_cookies()
        driver.refresh()
    except Exception as e:
        print(f"Error during submission {i + 1}: {e}")
        driver.refresh()
        continue

# Close the browser
driver.quit()
