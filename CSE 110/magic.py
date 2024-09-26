from selenium import webdriver
import time

# URL of the website from which you want to read text
source_url = "https://play.typeracer.com/?universe=dictionary"

# URL of the website where you want to write the text
destination_url = "https://play.typeracer.com/?universe=dictionary"

# Initialize WebDriver (specify the path to your browser driver)
driver = webdriver.Chrome("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk")

# Open the source website
driver.get(source_url)

# Wait for the page to load
time.sleep(3)  # Adjust the sleep time as needed

# Get the text from the source website (modify as needed depending on website structure)
source_text = driver.find_element_by_xpath("high seem govern mean part man and down school possible life also another need home very school few same you").text

# Open the destination website
driver.get(destination_url)

# Wait for the page to load
time.sleep(3)  # Adjust the sleep time as needed

# Find the input field on the destination website and write the text
input_field = driver.find_element_by_xpath("//input[@id='input-field']")  # Adjust the XPath to match the input field
input_field.send_keys(source_text)

# Close the browser
driver.quit()
