import requests
import sys

def check_app_exists(apigee_url, apigee_developer, app_name, token):
    url =  f"{apigee_url}/developers/{apigee_developer}/apps/{app_name}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)

    print(f"Response Code: {response.status_code}")  # Print status code

    if response.status_code == 200:
        print("appExists=true")
        return "true"
    elif response.status_code == 404:
        print("appExists=false")
        return "false"
    else:
        print(f"Error: Unexpected response {response.status_code}")
        sys.exit(1)

if __name__ == "__main__":
    APIGEE_URL = sys.argv[1]
    APIGEE_DEVELOPER = sys.argv[2]
    APP_NAME = sys.argv[3]
    TOKEN = sys.argv[4]
    
    check_app_exists(APIGEE_URL, APIGEE_DEVELOPER, APP_NAME, TOKEN)
