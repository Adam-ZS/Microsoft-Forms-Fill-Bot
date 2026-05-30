
# Microsoft Forms Auto Filler

Automate Microsoft Forms submissions effortlessly using Selenium.  
This tool fills forms automatically, handles multiple question types, and runs fully headless for fast and efficient automation.

---

## Overview

This project is a Python-based automation bot built with Selenium.  
It detects Microsoft Forms questions dynamically and answers them automatically using randomized logic.

It supports:
- Radio buttons
- Checkboxes
- Text inputs
- Multi-page forms (Next button handling)
- Auto submission
- Headless browser execution

---

## Features

- **Smart Question Detection**  
  Automatically detects Microsoft Forms question containers.

- **Radio Button Automation**  
  Randomly selects available options.

- **Checkbox Automation**  
  Selects multiple valid options while avoiding excluded values.

- **Text Input Filling**  
  Automatically fills text fields and text areas with random responses.

- **Multi-page Navigation**  
  Automatically clicks "Next" when available.

- **Auto Submit Handling**  
  Detects and clicks "Submit" when reached.

- **Headless Mode Support**  
  Runs without opening a visible browser window.

- **Stability Handling**  
  Handles stale elements and skips broken fields safely.

- **Multiple Submissions Support**  
  Runs automation multiple times based on user input.

---

## Requirements

Before running the bot, ensure:

- You have a working Microsoft Form URL
- The form structure is compatible with Microsoft Forms layout
- Firefox is installed
- Internet connection is active

---

## Installation

### 1. Install Python

Download Python:
https://www.python.org/downloads/

Enable:
- Add Python to PATH

Verify:
```bash
python --version
````

---

### 2. Install Dependencies

Install required packages:

```bash
pip install selenium webdriver-manager
```

---

### 3. Install Firefox

Download Firefox:
[https://www.mozilla.org/firefox/](https://www.mozilla.org/firefox/)

---

## How It Works

The bot uses:

* `webdriver_manager` → Automatically installs GeckoDriver
* `Firefox WebDriver` → Controls browser
* `Selenium selectors` → Detects form elements
* `Random generator` → Fills responses dynamically

---

## Configuration

### Excluded Options

These values will NOT be selected in checkboxes:

```python
GLOBAL_EXCLUSIONS = [
    "other",
    "medical",
    "__other_option__",
    "اخرى",
    "أخرى"
]
```

---

### Text Responses Pool

Used for text fields:

```python
TEXT_RESPONSES = [
    "Good", "Excellent", "Yes", "No", "N/A",
    "Perfect", "Okay", "Agree", "Strongly agree",
    "Everything is fine", "Very good", "Satisfied",
    "Nice", "Thank you"
]
```

---

## Run the Bot

Run the script:

```bash
python Form.py
```

---

## Usage

When running:

1. Enter Microsoft Form URL
2. Enter number of submissions
3. Bot starts automatically

Example:

```
Enter Microsoft Form URL: https://forms.office.com/...
Number of submissions: 10
```

---

## Output Example

```
Submission 1/10
Success

Submission 2/10
Submitted

Successful: 9/10
Time: 32.14 seconds
Average: 3.21 sec
```

---

## Notes

* Works only with Microsoft Forms structure
* Some forms may block automation or require adjustments
* Headless mode is enabled by default
* Use responsibly for testing purposes only

---

## Troubleshooting

If errors occur:

* Ensure Firefox is installed
* Update Selenium:

  ```bash
  pip install --upgrade selenium
  ```
* Check form layout compatibility
* Disable extra form restrictions if needed

---

## Author

Adam-ZS

---

## License

For educational and testing purposes only

