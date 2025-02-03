import sys
import apigee_operations


def automate_apigee_operations (apigeeUrl, apigeeDeveloper, appName, consumerKey, apiProduct, token):
    apigee_operations.check_product_exists(apigeeUrl, apiProduct, token)
    appExists = apigee_operations.check_app_exists(apigeeUrl, apigeeDeveloper, appName, token)

    if (appExists.lower() != "true"):
        apigee_operations.create_new_app(apigeeUrl, apigeeDeveloper, appName, token)
    
    apigee_operations.subscribe_new_product(apigeeUrl, apigeeDeveloper, appName, consumerKey, apiProduct, token)

if __name__ == "__main__":
    APIGEE_URL = sys.argv[1]
    APIGEE_DEVELOPER = sys.argv[2]
    APP_NAME = sys.argv[3]
    CONSUMER_KEY = sys.argv[4]
    API_PRODUCT = sys.argv[5]
    TOKEN = sys.argv[6]
    
    automate_apigee_operations (APIGEE_URL, APIGEE_DEVELOPER, APP_NAME, CONSUMER_KEY, API_PRODUCT, TOKEN)