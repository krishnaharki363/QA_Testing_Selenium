from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import traceback


def login(driver, wait):
    driver.get("Your_URL")
    print("Login page opened")

    email = "Your_Email"
    password = "Your_Password"

    login_email = wait.until(
        EC.visibility_of_element_located((By.XPATH, "(//input[@placeholder='Email'])[2]"))
    )
    login_password = wait.until(
        EC.visibility_of_element_located((By.XPATH, "(//input[@placeholder='Password'])[2]"))
    )

    login_email.clear()
    login_email.send_keys(email)

    login_password.clear()
    login_password.send_keys(password)

    buttons = wait.until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "button"))
    )

    sign_in_button = None
    for btn in buttons:
        if btn.text.strip().upper() == "SIGN IN":
            sign_in_button = btn
            break

    if sign_in_button is None:
        raise Exception("SIGN IN button not found")

    driver.execute_script("arguments[0].click();", sign_in_button)
    print("Logged in successfully")


def open_create_order(driver, wait):
    create_order_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Create Order')]"))
    )
    driver.execute_script("arguments[0].click();", create_order_btn)
    print("Clicked Create Order")


def debug_page(driver):
    print("\nCurrent URL:", driver.current_url)
    print("Page title:", driver.title)

    inputs = driver.find_elements(By.TAG_NAME, "input")
    print(f"\nFound {len(inputs)} input fields:\n")

    for i, inp in enumerate(inputs, start=1):
        try:
            print(
                f"{i}. placeholder={inp.get_attribute('placeholder')!r}, "
                f"name={inp.get_attribute('name')!r}, "
                f"type={inp.get_attribute('type')!r}, "
                f"value={inp.get_attribute('value')!r}"
            )
        except Exception:
            print(f"{i}. Could not inspect input")

    buttons = driver.find_elements(By.TAG_NAME, "button")
    print(f"\nFound {len(buttons)} buttons:\n")

    for i, btn in enumerate(buttons, start=1):
        try:
            print(f"{i}. text={btn.text.strip()!r}")
        except Exception:
            print(f"{i}. Could not inspect button")


def main():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 30)

    try:
        login(driver, wait)

        wait.until(EC.url_contains("/sales-company"))
        print("Current URL after login:", driver.current_url)

        open_create_order(driver, wait)

        wait.until(EC.url_contains("/travelers/new"))
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(3)

        print("Traveller page opened successfully")
        debug_page(driver)

        input("\nPress Enter to close browser...")
    except Exception as e:
        print("Error occurred:", e)
        traceback.print_exc()
        input("Press Enter to close browser...")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
