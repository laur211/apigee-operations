import requests
import json
import sys

def create_app(apigee_url, apigee_developer, app_name, token):
    url = f"{apigee_url}/developers/{apigee_developer}/apps"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = json.dumps({"name": app_name})
    response = requests.post(url, headers=headers, data=payload)
    
    if response.status_code != 201:
        print(f"Error: Failed to create app (HTTP {response.status_code})\nResponse: {response.text}")
        sys.exit(1)

    return response.json() if response.text else None

def create_customer_key(apigee_url, apigee_developer, app_name, consumer_key, token):
    url = f"{apigee_url}/developers/{apigee_developer}/apps/{app_name}/keys/create"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = json.dumps({
        "consumerKey": consumer_key,
        "consumerSecret": consumer_key,
        "status": "Approved"
    })
    response = requests.post(url, headers=headers, data=payload)

    if response.status_code == 201:
        print(f"Consumer key created successfully: {consumer_key}")
        return response.json() if response.text else None
    
    elif response.status_code == 409:
        print(f"Warning: Consumer key '{consumer_key}' already exists. Skipping creation.")
        return None  # Return None to indicate the key already exists

    else:
        print(f"Error: Failed to create consumer key (HTTP {response.status_code})\nResponse: {response.text}")
        sys.exit(1)

    

def associate_product(apigee_url, apigee_developer, app_name, consumer_key, api_product, token):
    url = f"{apigee_url}/developers/{apigee_developer}/apps/{app_name}/keys/{consumer_key}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = json.dumps({
        "apiProducts": [api_product]
    })
    response = requests.post(url, headers=headers, data=payload)

    if response.status_code not in [200, 201]:
        print(f"Error: Failed to create associate product. (HTTP {response.status_code})\nResponse: {response.text}")
        sys.exit(1)

    return response.json() if response.text else None

def delete_consumer_key(apigee_url, apigee_developer, app_name, consumer_key, token):
    url = f"{apigee_url}/developers/{apigee_developer}/apps/{app_name}/keys/{consumer_key}"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    response = requests.delete(url, headers=headers)

    if response.status_code not in [200, 204]:
        print(f"Error: Failed to delete consumer key (HTTP {response.status_code})\nResponse: {response.text}")
        sys.exit(1)


    return response.json() if response.text else None
