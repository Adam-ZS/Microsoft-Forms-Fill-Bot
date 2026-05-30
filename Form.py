from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import StaleElementReferenceException
import random
import time

parrot = r"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                 MICROSOFT FORMS AUTO FILLER v1.0                   ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

 █████╗ ██████╗  █████╗ ███╗   ███╗      ███████╗███████╗
██╔══██╗██╔══██╗██╔══██╗████╗ ████║      ╚══███╔╝██╔════╝
███████║██║  ██║███████║██╔████╔██║        ███╔╝ ███████╗
██╔══██║██║  ██║██╔══██║██║╚██╔╝██║       ███╔╝  ╚════██║
██║  ██║██████╔╝██║  ██║██║ ╚═╝ ██║      ███████╗███████║
╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝      ╚══════╝╚══════╝


     __  __ _                     __            __
    /  |/  (_)___________  ______/ /_____  ____/ /_
   / /|_/ / / ___/ ___/ / / / __  / __ \/ __  / /
  / /  / / / /__/ /  / /_/ / /_/ / /_/ / /_/ / /
 /_/  /_/_/\___/_/   \__,_/\__,_/\____/\__,_/_/

                Forms Automation Suite
                   by Adam-ZS
"""

# ============================================
# CONFIG
# ============================================

GLOBAL_EXCLUSIONS = [
    "other",
    "medical",
    "__other_option__",
    "اخرى",
    "أخرى"
]

TEXT_RESPONSES = [
    "Good",
    "Excellent",
    "Yes",
    "No",
    "N/A",
    "Perfect",
    "Okay",
    "Agree",
    "Strongly agree",
    "Everything is fine",
    "Very good",
    "Satisfied",
    "Nice",
    "Thank you"
]

# ============================================
# RANDOM TEXT
# ============================================

def random_text():
    return random.choice(TEXT_RESPONSES)

# ============================================
# FILL MICROSOFT FORM
# ============================================

def fill_microsoft_form(driver, form_url):

    try:
        driver.get(form_url)

        time.sleep(3)

        while True:

            questions = driver.find_elements(
                By.CSS_SELECTOR,
                "div[data-automation-id='questionItem']"
            )

            for q in questions:

                try:

                    # ====================================
                    # RADIO BUTTONS
                    # ====================================

                    radios = q.find_elements(
                        By.CSS_SELECTOR,
                        "input[type='radio']"
                    )

                    if radios:

                        unchecked = [
                            r for r in radios
                            if not r.is_selected()
                        ]

                        if unchecked:

                            selected = random.choice(unchecked)

                            driver.execute_script(
                                "arguments[0].click();",
                                selected
                            )

                            time.sleep(0.1)

                    # ====================================
                    # CHECKBOXES
                    # ====================================

                    checkboxes = q.find_elements(
                        By.CSS_SELECTOR,
                        "input[type='checkbox']"
                    )

                    if checkboxes:

                        valid = []

                        for cb in checkboxes:

                            value = (
                                cb.get_attribute("value") or ""
                            ).lower()

                            if not any(
                                ex in value
                                for ex in GLOBAL_EXCLUSIONS
                            ):
                                valid.append(cb)

                        if valid:

                            count = random.randint(
                                1,
                                min(3, len(valid))
                            )

                            picks = random.sample(valid, count)

                            for cb in picks:

                                driver.execute_script(
                                    "arguments[0].click();",
                                    cb
                                )

                                time.sleep(0.1)

                    # ====================================
                    # TEXT INPUTS
                    # ====================================

                    text_inputs = q.find_elements(
                        By.CSS_SELECTOR,
                        "textarea, input[type='text']"
                    )

                    for txt in text_inputs:

                        current = txt.get_attribute("value")

                        if not current:

                            txt.send_keys(random_text())

                            time.sleep(0.05)

                except StaleElementReferenceException:
                    continue

                except Exception:
                    continue

            # ====================================
            # NEXT BUTTON
            # ====================================

            try:

                next_buttons = driver.find_elements(
                    By.XPATH,
                    "//button[contains(., 'Next')]"
                )

                if next_buttons:

                    next_btn = next_buttons[0]

                    if next_btn.is_displayed():

                        driver.execute_script(
                            "arguments[0].click();",
                            next_btn
                        )

                        time.sleep(2)

                        continue

            except:
                pass

            # ====================================
            # SUBMIT BUTTON
            # ====================================

            try:

                submit_buttons = driver.find_elements(
                    By.XPATH,
                    "//button[contains(., 'Submit')]"
                )

                if submit_buttons:

                    submit_btn = submit_buttons[0]

                    if submit_btn.is_displayed():

                        driver.execute_script(
                            "arguments[0].click();",
                            submit_btn
                        )

                        return True

            except:
                pass

            break

        return False

    except Exception as e:

        print(f"❌ Error: {e}")

        return False

# ============================================
# MAIN
# ============================================

def run_automation():

    print(parrot)

    print("=" * 50)
    print("Microsoft Forms Auto Filler")
    print("=" * 50)

    form_url = input("\n📋 Enter Microsoft Form URL: ").strip()

    num_submissions = int(
        input("🔢 Number of submissions: ")
    )

    # ====================================
    # FIREFOX OPTIONS
    # ====================================

    options = Options()

    options.add_argument("--headless")

    options.add_argument("--width=1200")

    options.add_argument("--height=1000")

    options.add_argument("--disable-gpu")

    options.add_argument("--no-sandbox")

    # ====================================
    # DRIVER
    # ====================================

    driver = webdriver.Firefox(
        service=Service(
            GeckoDriverManager().install()
        ),
        options=options
    )

    total = 0

    start_time = time.time()

    print("\n🚀 Starting...\n")

    for i in range(num_submissions):

        print(
            f"📝 Submission {i+1}/{num_submissions}"
        )

        success = fill_microsoft_form(
            driver,
            form_url
        )

        if success:

            try:

                WebDriverWait(driver, 5).until(
                    EC.url_contains("ResponsePage")
                )

                total += 1

                print("✅ Success")

            except:

                print("⚠️ Submitted")

        else:

            print("❌ Failed")

        driver.delete_all_cookies()

    elapsed = time.time() - start_time

    driver.quit()

    print("\n" + "=" * 50)

    print(
        f"✅ Successful: {total}/{num_submissions}"
    )

    print(
        f"⏱️ Time: {elapsed:.2f} seconds"
    )

    if num_submissions > 0:

        print(
            f"⚡ Average: {elapsed / num_submissions:.2f} sec"
        )

    print("=" * 50)

# ============================================
# START
# ============================================

if __name__ == "__main__":

    run_automation()
