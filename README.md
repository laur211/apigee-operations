![Diagram](https://raw.githubusercontent.com/laur211/apigee-operations/master/apigee_workflow_diagram.drawio.png)

# Apigee Operations GitHub Action

## Overview
This GitHub Action automates Apigee application management, including validating API products, checking for existing applications, creating new applications, and subscribing them to API products. It is triggered manually via `workflow_dispatch`.

## Features
- Validates the existence of an API product in Apigee.
- Checks if an application already exists.
- Creates a new application if it does not exist.
- Subscribes the application to the specified API product.

## Inputs
This workflow requires the following inputs:

| Name          | Description                                    | Required |
|---------------|------------------------------------------------|----------|
| `APP_NAME`    | The name of the application in Apigee.         | true |
| `CONSUMER_KEY`| The consumer key for the new application.      | true |
| `API_PRODUCT` | The API product to associate with the app.     | true |

## Secrets
The following GitHub secrets must be set for authentication:

| Secret Name  | Description |
|-------------|-------------|
| `TOKEN`      | The API token for authenticating with Apigee. |

## Environment Variables
The following environment variables are set during execution:

| Variable          | Description |
|------------------|-------------|
| `APIGEE_DEVELOPER` | The developer associated with the application (to be configured). |
| `APIGEE_URL`       | The base URL of the Apigee API (to be configured). |

## Usage
Trigger this workflow manually from the GitHub Actions tab by providing the required inputs.

## Steps
1. **Checkout Repository** - Clones the repository.
2. **Set up Python** - Installs Python 3.x.
3. **Install Dependencies** - Installs required Python packages.
4. **Set Environment Variables** - Configures required environment variables.
5. **Validate API Product** - Checks if the specified API product exists.
6. **Verify App Existence** - Checks if the application already exists.
7. **Create New App** - Creates a new application if it does not exist.
8. **Subscribe to API Product** - Subscribes the application to the given API product.

## Scripts Used
- `scripts/validate_product.py` - Validates the API product.
- `scripts/check_apigee_app.py` - Checks if an application exists.
- `scripts/create_new_app.py` - Creates a new application.
- `scripts/subscribe_new_product.py` - Subscribes an application to an API product.

## Notes
- Ensure that `APIGEE_URL` and `APIGEE_DEVELOPER` are correctly set before running this workflow.
- The workflow assumes the existence of the Python scripts mentioned above in the `scripts/` directory.

