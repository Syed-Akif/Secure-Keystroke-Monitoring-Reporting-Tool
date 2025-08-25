#Secure-Keystroke-Monitoring-Reporting-Tool

This is a simple keylogger written in Python that captures keyboard inputs and sends a report to a specified email address at regular intervals.

**Disclaimer:** This tool is for educational purposes only. Unauthorized monitoring of a computer is illegal.

## Features
- Captures keystrokes.
- Logs special keys (e.g., Space, Enter, Shift).
- Sends log reports via email.
- Runs in the background.

## Setup
1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd keylogger
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure Email Settings:**
    - Open `keylogger.py`.
    - Set your `SENDER_EMAIL` and `SENDER_PASSWORD`.
    - **Important:** For Gmail, you will likely need to generate an "App Password". Go to your Google Account settings -> Security -> App passwords.

## Usage
Run the script from your terminal:
```bash
python keylogger.py
The keylogger will start capturing keystrokes and will send an email report every 60 seconds (or the interval you configure).

