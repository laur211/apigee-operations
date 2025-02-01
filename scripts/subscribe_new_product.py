import sys
import gcp_operations

def subscribe_new_product(apigee_url, apigee_developer, app_name, consumer_key, api_product, token):

    response_key = gcp_operations.create_customer_key(apigee_url, apigee_developer, app_name, consumer_key, token)

    response_product = gcp_operations.associate_product(apigee_url, apigee_developer, app_name, consumer_key, api_product, token)

if __name__ == "__main__":
    APIGEE_URL = sys.argv[1]
    APIGEE_DEVELOPER = sys.argv[2]
    APP_NAME = sys.argv[3]
    CONSUMER_KEY = sys.argv[4]
    API_PRODUCT = sys.argv[5]
    TOKEN = sys.argv[6]

    subscribe_new_product(APIGEE_URL, APIGEE_DEVELOPER, APP_NAME, CONSUMER_KEY, API_PRODUCT, TOKEN)
