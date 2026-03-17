from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

URL = "https://test.hgn.com.np/sales-company"

# ----------------------------
# Sample travellers data
# ----------------------------
travellers = [
    {
        "first_name": "Ram",
        "last_name": "Sharma",
        "email": "ram@example.com",
        "phone": "9800000001",
        "passport": "P1234567"
    },
    {
        "first_name": "Sita",
        "last_name": "Thapa",
        "email": "sita@example.com",
        "phone": "9800000002",
        "passport": "P7654321"
    }
]

# ----------------------------
# Setup browser
# ----------------------------
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 20)

driver.get(URL)

# ----------------------------
# LOGIN STEP
# ----------------------------
# Replace these selectors after inspecting the real page

username = input("hgnnsales@hgn.com.np")
password = input("HgnSales@1234")

# Example login fields
wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)

# Example login button
driver.find_element(By.XPATH, "//button[contains(., 'Login') or contains(., 'Log in')]").click()

print("Logged in attempt done...")
time.sleep(3)

# ----------------------------
# FUNCTION: fill traveller form
# ----------------------------
def fill_traveller_form(traveller):
    # Replace these locators with actual ones from your site
    wait.until(EC.presence_of_element_located((By.NAME, "firstName"))).clear()
    driver.find_element(By.NAME, "firstName").send_keys(traveller["first_name"])

    driver.find_element(By.NAME, "lastName").clear()
    driver.find_element(By.NAME, "lastName").send_keys(traveller["last_name"])

    driver.find_element(By.NAME, "email").clear()
    driver.find_element(By.NAME, "email").send_keys(traveller["email"])

    driver.find_element(By.NAME, "phone").clear()
    driver.find_element(By.NAME, "phone").send_keys(traveller["phone"])

    driver.find_element(By.NAME, "passportNumber").clear()
    driver.find_element(By.NAME, "passportNumber").send_keys(traveller["passport"])

# ----------------------------
# ADD TRAVELLERS
# ----------------------------
for i, traveller in enumerate(travellers):
    # Click Add Traveller for first and additional travellers
    add_traveller_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add Traveller')]"))
    )
    add_traveller_btn.click()

    time.sleep(1)
    fill_traveller_form(traveller)

    print(f"Traveller {i + 1} added")

    time.sleep(1)

# ----------------------------
# CLICK CONTINUE
# ----------------------------
continue_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Continue')]"))
)
continue_btn.click()

print("Moved to Trip & Coverage Setup")

# ----------------------------
# FILL TRIP & COVERAGE
# ----------------------------
# Replace with actual locators from the page
# Example:
# wait.until(EC.presence_of_element_located((By.NAME, "destination"))).send_keys("Nepal")
# driver.find_element(By.NAME, "startDate").send_keys("2026-03-20")
# driver.find_element(By.NAME, "endDate").send_keys("2026-03-25")
# driver.find_element(By.XPATH, "//button[contains(., 'Next') or contains(., 'Proceed')]").click()

print("Now inspect Trip & Coverage fields and add the correct selectors.")

# Keep browser open for checking
input("Press Enter to close browser...")
driver.quit()