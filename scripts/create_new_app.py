import sys
import gcp_operations

def create_new_app(apigee_url, apigee_developer, app_name, token):

    create_app_response = gcp_operations.create_app(apigee_url, apigee_developer, app_name, token)
    consumer_key_auto_generated = create_app_response['credentials'][0]['consumerKey']

    delete_response = gcp_operations.delete_consumer_key(apigee_url, apigee_developer, app_name, consumer_key_auto_generated, token)

if __name__ == "__main__":
    APIGEE_URL = sys.argv[1]
    APIGEE_DEVELOPER = sys.argv[2]
    APP_NAME = sys.argv[3]
    TOKEN = sys.argv[4]

    create_new_app(APIGEE_URL, APIGEE_DEVELOPER, APP_NAME, TOKEN)
