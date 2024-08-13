from os import environ
from orctane.utils.request import post

# Config vars
api_key = environ.get("ORCTANE_API_KEY", "orc_kVwozhpC0tQRLoC6t9XQNfReMtivku4Pb5")
api_url = environ.get("ORCTANE_API_URL", "http://localhost:5662")

def main():
    payload = {
        "version": "latest",
        "preview_text": "Dear Cmion, we noticed a login from Zurich",
        "variables": {
            "login_device": "Firefox on macOs",
            "login_time": "Sat, 22 Jun 2024, 00:01:10 AM"
        }
    }
    post('/templates/get/q2pf4b-BJUUA3cT4W99CyOqxDRc/godaddythankyou', payload)


if __name__ == "__main__":
    main()
