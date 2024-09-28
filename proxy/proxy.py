import logging
import requests

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    target_host = 'ipinfo.io'
    logging.info('Python HTTP trigger function processed a request.')
    method = req.method
    headers = {key: value for key, value in req.headers.items()}
    path = req.route_params.get('path', '')
    # path = complete_path[len('proxy/'):]
    logging.info(f"Path: {path}")
    logging.info(f"Headers: {headers}")
    # logging.info(headers)
    body = req.get_body()
    # Define the target host
    headers['host'] = target_host
    # Construct the target URL
    target_url = f"https://{target_host}/{path}"
    # Make the request to the target host
    response = requests.request(method, target_url, headers=headers, data=body)
    # Return the response from the target host
    return func.HttpResponse(
        response.content,
        status_code=response.status_code,
        headers=dict(response.headers)
    )