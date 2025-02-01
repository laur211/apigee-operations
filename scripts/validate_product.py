import requests
import sys

def check_product_exists(apigee_url, product, token):
    url = f"{apigee_url}/apiproducts"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{url}/{product}", headers=headers)
    print(response)

    print(f"Response Code: {response.status_code}")  # Print status code

    if response.status_code != 200:
      print(f"Request failed with http status code: {response.status_code}")
      sys.exit(1)

if __name__ == "__main__":
    APIGEE_URL = sys.argv[1]
    PRODUCT = sys.argv[2]
    TOKEN = sys.argv[3]
    
    check_product_exists(APIGEE_URL, PRODUCT, TOKEN)
