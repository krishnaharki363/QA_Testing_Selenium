from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("Platform URL")

wait = WebDriverWait(driver, 20)

# Login form fields (2nd Email and 2nd Password on the page)
login_email = wait.until(
    EC.visibility_of_element_located((By.XPATH, "(//input[@placeholder='Email'])[2]"))
)

login_password = wait.until(
    EC.visibility_of_element_located((By.XPATH, "(//input[@placeholder='Password'])[2]"))
)

login_email.clear()
login_email.send_keys("xyz@gmail.com")

login_password.clear()
login_password.send_keys("Password")

# Find all buttons and pick the SIGN IN one
buttons = wait.until(
    EC.presence_of_all_elements_located((By.TAG_NAME, "button"))
)

sign_in_button = None
for btn in buttons:
    text = btn.text.strip().upper()
    if text == "SIGN IN":
        sign_in_button = btn
        break

if sign_in_button is None:
    raise Exception("SIGN IN button not found")

# Scroll into view, then click
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", sign_in_button)
driver.execute_script("arguments[0].click();", sign_in_button)

print("SIGN IN button clicked successfully.")

input("Press Enter to close browser...")
driver.quit()