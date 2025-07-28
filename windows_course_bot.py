
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time, sys, uuid

# Change these to your DTU credentials
ROLL_NO = "LOGIN ID"
PASSWORD = "PASSWORD"

# DTU URLs
LOGIN_URL = "https://reg.exam.dtu.ac.in/student/login"
COURSE_URL = "https://reg.exam.dtu.ac.in/student/courseRegistration/64971609f608d957ec3b280e"//add your reg page url here.


# macOS chromedriver path
CHROMEDRIVER_PATH = "C:\\Path\\To\\chromedriver.exe"
CHROME_PROFILE = f"C:\\Windows\\Temp\\course-bot-{uuid.uuid4()}"

# Replace these with your subject names and form IDs
FORM_IDS = {
    "Consumer Behaviour": "64971609f608d957ec3b280e/686e5514d00bc35c8c12bdb3",
    "Creative Writing Skills": "64971609f608d957ec3b280e/686e5514d00bc35c8c12bd77",
    "Non-Verbal Communication": "64971609f608d957ec3b280e/686e5514d00bc35c8c12bda3",
    "Economic Growth": "64971609f608d957ec3b280e/686e5514d00bc35c8c12be37",
    "Macro": "64971609f608d957ec3b280e/686e5514d00bc35c8c12bd73",
    "Total Quality Management": "64971609f608d957ec3b280e/686e5514d00bc35c8c12bd83"
}

options = Options()
options.add_argument(f"--user-data-dir={CHROME_PROFILE}")
options.add_argument("--profile-directory=Default")
options.add_experimental_option("detach", True)
service = Service(CHROMEDRIVER_PATH)

def main():
    registered = False
    print("Launching Chrome")

    try:
        driver = webdriver.Chrome(service=service, options=options)
        driver.set_window_size(1200, 900)
        driver.get(LOGIN_URL)

        print("🔐 Logging in...")
        print("Loaded by original DTU bot creator - github.com/KunwarxSingh")
        driver.find_element(By.NAME, "roll_no").send_keys(ROLL_NO)
        driver.find_element(By.NAME, "password").send_keys(PASSWORD)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()

        while "/student/home" not in driver.current_url:
            time.sleep(0.2)

        print("⏳ Opening course registration page...")

        while not registered:
            driver.get(COURSE_URL)

            for name, form_id in FORM_IDS.items():
                try:
                    form_xpath = f"//form[contains(@action, '{form_id}')]"
                    form_elements = driver.find_elements(By.XPATH, form_xpath)
                    if not form_elements:
                        print(f"{name}: Form not found.")
                        continue

                    register_btn = form_elements[0].find_element(By.XPATH, ".//button[contains(text(), 'Register')]")
                    if register_btn.is_enabled():
                        print(f"👉 Registering for {name}...")
                        driver.execute_script("arguments[0].click();", register_btn)
                        time.sleep(2.5)
                        driver.get(COURSE_URL)
                        time.sleep(0.5)

                        if not driver.find_elements(By.XPATH, form_xpath):
                            print(f"Confirmed: {name} registered.")
                            registered = True
                            break
                        else:
                            print(f"⚠️ {name} still appears. Trying next...")
                    else:
                        print(f"⏳ {name}: Button not enabled yet.")
                except Exception as e:
                    print(f"⚠️ {name}: Error - {e}")

            if not registered:
                print("🔁 Retrying in 2s...\n")
                time.sleep(1.5)

    except Exception as e:
        print("Fatal error:", e)
        try:
            driver.save_screenshot("error.png")
            print("Screenshot saved as error.png")
        except:
            pass
        sys.exit(1)

    finally:
        if registered:
            driver.quit()

if __name__ == "__main__":
    main()
