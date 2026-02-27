
import RPi.GPIO as GPIO
import time
from twilio.rest import Client
import smtplib
from email.mime.text import MIMEText

# GPIO Setup
BUTTON_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Twilio credentials
account_sid = 'AC87c2a7f0187439b6c1e08ee06c74025f'
auth_token = 'a771922a4ceff468d85871853f052242'

# Email credentials
email_address = 'octatanglecare3s@gmail.com'
email_password = 'nvxz bzjd ypqa crkk'

# Static receiver information
receiver_email = 'akulashivaakulashiva@gmail.com'
receiver_phone = '+919390370155'

# Function to send email
def send_email():
    subject = "Emergency Alert"
    body = "This is an emergency alert. Please check in with the sender as soon as possible."
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = email_address
    msg['To'] = receiver_email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(email_address, email_password)
        server.sendmail(email_address, receiver_email, msg.as_string())
    print(f"Email sent to {receiver_email}")

# Function to send SMS using Twilio API
#def send_sms():
 #   client = Client(account_sid, auth_token)
  ###print(f"SMS sent to {receiver_phone}")

# Function to handle button press
def on_button_press():
    print("Button pressed!")
    #send_sms()
    send_email()

# Main loop
try:
    while True:
        input_state = GPIO.input(BUTTON_PIN)
        if input_state == False:
            on_button_press()
            time.sleep(5)  # Debounce
finally:
    GPIO.cleanup()
