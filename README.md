# Microsoft-Forms-Fill-Bot
Automate your form submissions effortlessly! This bot fills out forms for you, saves time, and ensures accuracy—perfect for surveys, registrations, and more. Try it now and let the bot do the work!

# Form Automation Bot

This bot automates form submissions, making it perfect for repetitive tasks like filling out surveys, registrations, or feedback forms. It uses Selenium to interact with web forms, dynamically detects fields, and fills them with random or predefined data. Whether you're testing a form or need to submit multiple entries, this bot saves time and ensures accuracy.

---

## Features

- **Dynamic Form Detection:** Automatically detects and fills text fields, dropdowns, radio buttons, checkboxes, and more.
- **Customizable Data:** Randomly generates names, ages, phone types, brands, and other data, or allows you to customize the inputs.
- **Headless Mode:** Runs in the background without opening a browser window.
- **Error Handling:** Skips problematic fields and continues filling the form.
- **Multiple Submissions:** Submits the form multiple times as specified by the user.
- **Form Reset:** Clears cookies and refreshes the page after each submission to ensure a clean slate.

---

## Requirements
##You Need to CHange Stuff to fit With Your Form##
Before running the bot, ensure you have the following installed:

1. **Python 3.x**
2. **Selenium**
3. **Geckodriver**
4. **Firefox Browser**

---

## Setup

### Step 1: Install Python

1. **Install Python 3.x**
   - On Windows/macOS/Linux, download Python from [python.org](https://www.python.org/downloads/).
   - During installation, ensure you check the box to **Add Python to PATH**.

2. **Verify Installation**
   - Open a terminal or command prompt and run:
     ```bash
     python --version
     ```
   - You should see something like `Python 3.x.x`.

---

### Step 2: Set Up a Virtual Environment (Optional/ If you got enviroment error)

1. **Create a Virtual Environment**
   - Navigate to your project folder and run:
     ```bash
     python -m venv venv
     ```

2. **Activate the Virtual Environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate

---

### Step 3: Install Dependencies

1. **Install Selenium**
   - Run the following command:
     ```bash
     pip install selenium
     pip install selenium webdriver-manager
     pip install webdriver-manager     


     ```

2. **Download Geckodriver**
   - Download Geckodriver for your operating system:
     - **Windows:** [geckodriver.exe](https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-win64.zip)
     - **macOS:** [geckodriver](https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-macos.tar.gz)
     - **Linux:** [geckodriver](https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-linux64.tar.gz)
   - Extract the downloaded file and note the path to the `geckodriver` executable.

3. **Install Firefox**
   - On Windows/macOS/Linux, download and install Firefox from [mozilla.org](https://www.mozilla.org/firefox/).

---

### Step 4: Set Up the Bot

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Adam-ZS/Microsoft-Forms-Fill-Bot.git
   cd Microsoft-Forms-Fill-Bot
   
Update the Script

Open the script (Form.py) in a text editor.

Update the geckodriver_path variable with the path to your Geckodriver executable.

       geckodriver_path = "/path/to/geckodriver"  # Update this path to yours
       
To find yours

      sudo find / -name "geckodriver"

