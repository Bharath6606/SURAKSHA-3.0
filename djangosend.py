



import RPi.GPIO as GPIO
import requests
import time

# Set the GPIO pin for the switch
SWITCH_PIN = 17  # Change this to your GPIO pin number

# Set up GPIO
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Set pin as input with pull-up resistor

def get_contact_details(device_id):
    print("enterd function");
    # Replace with your Django server URL
    url = f'http://192.168.105.245:8000/api/get_contact_details/{device_id}/'
    
    print(url)
    try:
        print("entered try..")
        response = requests.get(url)
        print(response)
        if response.status_code == 200:
            print("entered 1st if..")
            print("Contact details:", response.json())
        else:
            print("entered 1st else")
            print("Failed to retrieve contact details:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error:", e)

try:
    while True:
       # time.sl#eep() 
        print("entered whlie..")
        input_state = GPIO.input(SWITCH_PIN)
        if input_state == GPIO.LOW:  # Button is pressed
            print("Switch pressed!")
            device_id = 3  # Example device ID, replace with actual device ID
            get_contact_details(device_id)
            time.sleep(1)  # Delay to debounce the button press
        time.sleep(5)  # Small delay to prevent high CPU usage
except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up GPIO on CTRL+C exit
