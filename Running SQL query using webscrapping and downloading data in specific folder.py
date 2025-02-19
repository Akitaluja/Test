from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import subprocess
import json

# Define the script and the site name as arguments
script = "C:/Users/Ankit/Documents/cred.py"
site_name = "supersql-site"
# Run the script and capture the output
result = subprocess.run(["python", script, site_name], capture_output=True, text=True)
# Parse the output (assuming it is in JSON format)
creds = json.loads(result.stdout)
# Extract the userid and password
userid = creds['userid']
password = creds['password']

# Step 3: Enter SQL query
sql_query = "select count(*) from OR;"

# Initialize WebDriver
driver = webdriver.Chrome()

# Step 1: Log in to the website
driver.get("https://superset.xxxx.org/")
driver.find_element(By.NAME, "username").send_keys(userid)
driver.find_element(By.NAME, "password").send_keys(password)
driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)

time.sleep(3)  # Wait for login to complete

# Step 2: Navigate to the SQL page
driver.get("https://superset.xxxx.org/sqllab")
time.sleep(3)  # Wait for page load

# Step 3: Click on Ace Editor to Activate It (Instead of Clicking `ace_text-input`)
editor_area = driver.find_element(By.CLASS_NAME, "ace_content")
editor_area.click()  # Click the visible editor to focus
time.sleep(1)

# Step 4: Locate the Ace Editor Hidden Input
sql_input = driver.find_element(By.CLASS_NAME, "ace_text-input")  # Hidden input field

# Step 6: Select the Newly Entered Query (Shift + Up Arrow)
# Step 6: Select the Newly Entered Query (Shift + Up Arrow)
sql_input.send_keys(Keys.SHIFT, Keys.ARROW_UP)
sql_input.send_keys(Keys.DELETE)
# Step 5: Move to the Next Line and Enter SQL Query
sql_input.send_keys(Keys.ENTER)  # Move to a new line
time.sleep(1)

custom_query = sql_query  # Replace with your query
sql_input.send_keys(custom_query)
time.sleep(1)

# Step 6: Select the Newly Entered Query (Shift + Up Arrow)
sql_input.send_keys(Keys.SHIFT, Keys.ARROW_UP)

time.sleep(3)

# Locate the button using its class name
button = driver.find_element(By.XPATH, "//button[contains(@class, 'ant-btn') and contains(@class, 'superset-button') and contains(@class, 'superset-button-primary')]")

# Click the button
button.click()
# Step 3: Wait for Execution and Close Browser
time.sleep(35)  # Wait for 35 seconds for execution

# Locate the "Download to CSV" button using its class name
download_button = driver.find_element(By.XPATH, "//a[contains(@class, 'ant-btn') and contains(@class, 'superset-button') and contains(@class, 'css-18echj3') and .//span[contains(text(), 'Download to CSV')]]")

# Click the button
download_button.click()

print("Download started!")

# Step 8: Wait for download and close browser
time.sleep(60)  # Wait for 1 minute for download to complete
driver.quit()
