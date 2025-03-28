from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dashboard import Dashboard
from reporting import Reporting

driver=webdriver.Chrome()
driver.get("https://dev.quicflow.com/login")
# driver.maximize_window()
driver.set_window_size(2024, 768)
print(driver.title)
time.sleep(3)
username=driver.find_element(By.XPATH,'//input[@type="Email"]')
print(username.is_displayed())
print(username.is_enabled())
print(username.is_selected())
username.send_keys("rohan.k@mgtechsoft.com")
password=driver.find_element(By.XPATH,'//input[@type="password"]')
print(password.is_displayed())
print(password.is_enabled())
print(password.is_selected())
password.send_keys("Rohan@8008")
submit=driver.find_element(By.XPATH,'//button[@type="submit"]')
submit.click()
time.sleep(5)
print("Username is correct")
print("Password is correct")
print("You have successfully logged in to the Quicflow page")


#------------------Dashboard---------------------------------------

dashboard = Dashboard(driver)

# Wait for the dashboard to load
dashboard.wait_for_dashboard()
dashboard.connection_statistics()
dashboard.connection_name()
# dashboard.get_svg_texts()
dashboard.extract_chart_data()


# -----------------Connections--------------------------------------

Connection=driver.find_element(By.XPATH,'//a[@href="/connections"]')
Connection.click()
print("Got into the connection")

addconnection=driver.find_element(By.XPATH,'//button[@type="button"]')
time.sleep(2)
addconnection.click()
time.sleep(3)
print("Got into the add connection")

connection_name=driver.find_element(By.NAME,"connectionName")
connection_name.send_keys("Test ")
print("Connection name is Test")
time.sleep(3)

region=WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CLASS_NAME,"select__control")))
region.click()
print("Opened dropdown")

dropdown_options=WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,'//div[contains(@class,"select__option")]')))
for option in dropdown_options:
    print("Option found:",option.text)
dropdown_options=WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,'//div[contains(@class,"select__option")]')))

dropdown_options=WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,'//div[contains(@class,"select__option")]')))
for option in dropdown_options:
    if "US East" in option.text:
        selected_text = option.text  
        option.click()
        print("Region is selected:", selected_text)
        time.sleep(3)
        break


# source connection
wait = WebDriverWait(driver, 5)
source_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'select__input-container')]//input")))
source_input.click()
print("Source is clicked")
wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'select__option')]")))

options = driver.find_elements(By.XPATH, "//div[contains(@class, 'select__option')]")

for option in options:
    print("Selecting option:", option.text) 

options = driver.find_elements(By.XPATH, "//div[contains(@class, 'select__option')]")
for option in options:
    if "Jira (83)" in option.text:
        selected_text=option.text
        option.click()
        print("Source option is selected:", selected_text)
        time.sleep(3)
        break

#Source Jira URL
wait = WebDriverWait(driver, 5)
jira_url = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='url']")))
jira_url.send_keys("https://varshacs2029.atlassian.net")
print("Source Jira url is filled")
time.sleep(3)

#Source Jira email
wait = WebDriverWait(driver, 5)
jira_email = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
jira_email.send_keys("varshacs2029@gmail.com")
print("Source Jira email is filled")
time.sleep(3)

#Source Jira api token
wait = WebDriverWait(driver, 5)
jira_api_token = wait.until(EC.visibility_of_element_located((By.NAME, "token")))
jira_api_token.send_keys("ATATT3xFfGF0wFC-BiY-VR-LSALHf2AZegdwNj6XT9l1O5t3Gx90ohcpcG8PllJR4Atri858cmG-js6fhl271sI8fjWBOdCPM8eIzP0_hjmJMqZV11XgynR3KLUcD0OADh2SB5HtkyPj880y-Ru3cJxneoAWyV59yNz0FFIdLT1dhczRQc3Qrzo=8328A1A1")
print("Source Jira api token is filled")
time.sleep(3)

#Source Test Button
source_test_button=WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Test Connection']")))
source_test_button.click()
print("Source connection successful")
time.sleep(3)


#Destination Input
wait = WebDriverWait(driver, 5)
dest_input = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='react-select-8-input']")))
dest_input.click()
print("Destination is clicked")
wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'select__option')]")))

options = driver.find_elements(By.XPATH, "//div[contains(@class, 'select__option')]")

for option in options:
    print("Selecting option:", option.text) 

options = driver.find_elements(By.XPATH, "//div[contains(@class, 'select__option')]")
for option in options:
    if "Jira (84)" in option.text:
        selected_text=option.text
        option.click()
        print("Destination option is selected:", selected_text)
        time.sleep(3)
        break

#Destination jira url
wait = WebDriverWait(driver, 5)
dest_jira_url = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@name='url' and @placeholder='Enter Jira URL'])[2]")))
dest_jira_url.click()
dest_jira_url.send_keys("https://varshacs2029.atlassian.net")
print("Destination Jira url is filled")
time.sleep(3)

#Destination Jira email
wait = WebDriverWait(driver, 5)
jira_email = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='email' and @placeholder='Enter your email'])[2]")))
dest_jira_url.click()
jira_email.send_keys("varshacs2029@gmail.com")
print("Destination Jira email is filled")
time.sleep(3)

#Source Jira api token
wait = WebDriverWait(driver, 5)
jira_api_token = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='password' and @placeholder='Enter API token'])[2]")))
jira_api_token.send_keys("ATATT3xFfGF0wFC-BiY-VR-LSALHf2AZegdwNj6XT9l1O5t3Gx90ohcpcG8PllJR4Atri858cmG-js6fhl271sI8fjWBOdCPM8eIzP0_hjmJMqZV11XgynR3KLUcD0OADh2SB5HtkyPj880y-Ru3cJxneoAWyV59yNz0FFIdLT1dhczRQc3Qrzo=8328A1A1")
print("Destination Jira api token is filled")
time.sleep(3)

#Source Test Button
dest_test_button=WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "(//button[text()='Test Connection'])[2]")))
dest_test_button.click()
print("Destination connection successful")
time.sleep(3)

#Save connection button
save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Save Connection']")))

save_button.click()
print("Connection Saved successfully")




#------------------------------------------------------------------------------------------------------------------------

#Reporting
reporting=Reporting(driver)
reporting.wait_for_reporting()
reporting.click_reporting_option()
reporting.report_conn_name()
reporting.source_record_id()


time.sleep(7)
driver.quit()

