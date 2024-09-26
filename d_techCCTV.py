import requests
import re
import os
import time
import sys

# Clear terminal based on the OS
def clear_terminal():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux / MacOS
        os.system('clear')

# Fancy typing effect for hacker-like text
def type_effect(text, speed=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()  # Move to the next line

# Loading animation with dots
def loading_animation(text, duration=1, dots=3):
    """Creates a dynamic loading animation for hacker-like effect."""
    for _ in range(dots):
        sys.stdout.write(f"\r{text}{'.' * (_ % 4)}")
        sys.stdout.flush()
        time.sleep(duration / dots)
    print()

# Futuristic entry animation
def futuristic_entry():
    clear_terminal()
    print("\033[1;32m")  # Green text for the hacker look
    type_effect("Initializing D-TECH Systems...\n", speed=0.03)  # Reduced speed
    loading_animation("Connecting...", 1, dots=2)  # Reduced duration
    time.sleep(0.5)  # Short pause
    clear_terminal()

# Fake system threat warning
def system_warning():
    print("\033[1;31m")  # Red text for warning
    type_effect("WARNING: Unauthorized access detected!\n", speed=0.05)
    time.sleep(1)
    type_effect("Possible system breach...\n", speed=0.05)
    print("\033[1;37m")  # Back to white text
    time.sleep(1)

# Function to check IP location
def check_ip_location(ip):
    response = requests.get(f"http://ip-api.com/json/{ip}")
    if response.status_code == 200:
        return response.json()
    return None

# List of country codes to fetch CCTV feeds from
country_codes = ['US', 'JP', 'IN', 'FR', 'DE', 'RU', 'CN', 'BR', 'ZA']  # Add more countries if needed

# Apply D-TECH theme and futuristic entry
futuristic_entry()

# Clear and start the main interface
clear_terminal()
print("\033[1;32m")  # Green text for hacker theme
print("""
##############################################
##                                          ##
##  Welcome to the D-TECH CCTV FOOTAGE     ##
##   ACCESS POINT TO SECURITY CAMERA        ##
##              WORLDWIDE                   ##
##                                          ##
##############################################
""")
loading_animation("Initializing D-TECH systems", 1.5)  # Reduced duration

# Restore system warning
system_warning()

# Add boot-up system process
print("\033[1;32m")
type_effect("Booting up core modules...", speed=0.05)
time.sleep(0.5)  # Reduced sleep
loading_animation("Connecting to D-TECH servers", 2)  # Duration kept for suspense

# Access CCTV cameras worldwide
clear_terminal()
print("\033[1;37m")  # White text

# Display PREASX24 and CCTV hack tool introduction
type_effect("--&--~%P~EASX24 -%----", speed=0.07)
time.sleep(0.5)  # Reduced sleep
type_effect("Welcome to the D-TECH CCTV FOOTAGE ACCESS POINT TO SECURITY CAMERA WORLDWIDE!", speed=0.06)
time.sleep(0.5)  # Reduced sleep
type_effect("Accessing CCTV networks in multiple countries...\n", speed=0.05)

# Simulate IP fetch with progress bar effect
try:
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}
    total_ips_fetched = 0

    for country_code in country_codes:
        print(f"\033[1;34mFetching CCTV feeds for country: {country_code}")
        time.sleep(1)  # Simulate loading per country

        for page in range(0, 5):  # Adjust the number of pages to scrape per country
            url = f"http://www.insecam.org/en/bycountry/{country_code}/?page={page}"
            res = requests.get(url, headers=headers)
            findip = re.findall('http://\d+\.\d+\.\d+\.\d+:\d+', res.text)
            
            for hasil in findip:
                ip = hasil.split("/")[2].split(":")[0]  # Extract IP from the result
                location_info = check_ip_location(ip)  # Check the IP location
                
                if location_info:
                    print(f"\033[1;37m{hasil} - Location: {location_info['city']}, {location_info['region']}, {location_info['country']}")
                    with open('logs.txt', 'a') as f:
                        f.write(f"{hasil} - Location: {location_info['city']}, {location_info['region']}, {location_info['country']}\n")

                    total_ips_fetched += 1

                    # Reboot system messages at intervals
                    if total_ips_fetched in [15, 50] or (total_ips_fetched > 50 and total_ips_fetched % 50 == 0):
                        clear_terminal()
                        type_effect("SYSTEM REBOOTING...\n", speed=0.05)
                        loading_animation("Reinitializing core systems", 2)
                        time.sleep(1)  # Short pause before continuing

    print("\n\033[1;32mDone! All logs saved to logs.txt")
except Exception as e:
    print(f"\033[1;31mError occurred. Unable to fetch data: {str(e)}\033[0m")

# Add more hacker-like final messages
type_effect("\n-- Thanks for using the D-TECH program --", speed=0.05)
print("\n\033[1;34mMODIFIED BY Preasx24")
print("\033[1;37m------ PREASX24 ------")

# Instructions to view the logs
print("\033[1;33m")
type_effect("\nTo view the results, copy and paste this command:\n", speed=0.04)
print("\033[1;32m")
print("nano logs.txt")
