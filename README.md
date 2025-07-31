#  DTU Course Auto Registration Bot

This bot automatically registers you for electives on the DTU registration portal as soon as the registration opens. It uses Selenium to log in, keep refreshing the page, and click the “Register” button the moment it’s enabled.

> Works on both macOS and Windows using Selenium and ChromeDriver.

---

##  Features

- Auto login to student portal
- Automatically detects when the “Register” button is enabled
- Registers for multiple subjects
- Screenshot on crash
- Works on both macOS and Windows (separate scripts)

---

## 📁 Folder Structure

```
course-auto-reg/
├── mac_course_bot.py         # Use this on macOS
├── windows_course_bot.py     # Use this on Windows
├── requirements.txt          # Python dependencies
└── README.md                 # complete guide
```

---

##  Full Setup Guide (DO THIS STEP BY STEP)

---

### 1.Install Python

Check if Python is already installed:

```bash
python --version
# or
python3 --version
```

If not, download and install Python from:  
-> https://www.python.org/downloads/

---

### 2. Install pip (Python package installer)

Usually comes with Python. If not:

```bash
python -m ensurepip --upgrade
```

---

### 3. Install Selenium

Run this command:

```bash
pip install selenium
```

Also add this line to `requirements.txt`:

```
selenium
```

---

### 4. Install Google Chrome

If you don’t have it:  
->https://www.google.com/chrome/

---

### 5.Install ChromeDriver (VERY IMPORTANT)

Selenium uses this to control Chrome.

#### Step 1: Check your Chrome version

Open Chrome → go to: `chrome://settings/help`  
Note the version (e.g. `114.0.5735.110`)

#### Step 2: Download the matching ChromeDriver

Go to:  
->https://sites.google.com/chromium.org/driver/  
Download the version that matches your Chrome version.

#### Step 3: Set ChromeDriver path

- **On macOS**:

```bash
mv chromedriver /usr/local/bin/
chmod +x /usr/local/bin/chromedriver
```

- **On Windows**:
  Place `chromedriver.exe` somewhere like `C:\chromedriver\`

Update this line in `windows_course_bot.py`:

```python
CHROMEDRIVER_PATH = "C:\chromedriver\chromedriver.exe"
```

---

## How to Get Subject Form IDs??

You need a subject’s unique **form ID** to register it with the bot.

### Steps:

1. Open course registration page on Chrome:
   ->`https://reg.exam.dtu.ac.in/student/courseRegistration/<your-session-id>`

2. Right-click on the **"Register"** button of the subject → using **Inspect** element

3. Look for a line like:

   ```html
   <form
     action="/student/courseRegistration/64971609f608d957ec3b280e/686e5514d00bc35c8c12bd83"
   ></form>
   ```

4. The full form ID = everything after `/courseRegistration/`  
   Example:

   ```
   64971609f608d957ec3b280e/686e5514d00bc35c8c12bd83
   ```

5. Add to the `FORM_IDS` dict in the script like:

   ```python
   FORM_IDS = {
       "Creative Writing Skills": "64971609f608d957ec3b280e/686e5514d00bc35c8c12bd83"
   }
   ```

Repeat for all the subjects you want to auto-register.

---

## "Edit Your DTU Login Credentials in the Script"

Open either `mac_course_bot.py` or `windows_course_bot.py` and update:

```python
ROLL_NO = "Your DTU Roll Number"
PASSWORD = "Your DTU Password"
```

---

## ▶️ How to Run the Bot

### On macOS:

```bash
python3 mac_course_bot.py
```

### On Windows:

```bash
python windows_course_bot.py
```

**Keep it running before registration opens**. It will detect when the "Register" button becomes clickable and click it instantly.

---

## Optional: Delete Temp Chrome Profile (if needed)

The script creates a temp Chrome profile each time. You can delete it:

- **macOS**:

  ```bash
  rm -rf /tmp/course-bot-*
  ```

- **Windows**:  
  Delete folder like: `C:\Windows\Temp\course-bot-*`

---

## Crash Debugging

If something goes wrong, the bot saves a screenshot as `error.png` in the project directory so you can see what happened.

---

---

## Built By

This script was made by KxS  
Use it wisely, and don’t get caught slacking during electives 😉.
