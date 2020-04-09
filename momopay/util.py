import os
from uuid import uuid4

import requests
from dotenv import load_dotenv

load_dotenv()


def create_api_user(key):
    """Create momo api user"""
    url = 'https://ericssonbasicapi2.azure-api.net/v1_0/apiuser'
    body = {'providerCallbackHost': os.getenv('CALLBACK_HOST')}
    id = str(uuid4())
    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'X-Reference-Id': id
    }
    x = requests.post(url, json=body, headers=headers)
    if x.status_code is not 201:
        return None
    return id


def get_api_user(id, key):
    url = f'https://ericssonbasicapi2.azure-api.net/v1_0/apiuser/{id}/apikey'
    headers = {
        'Ocp-Apim-Subscription-Key': key,
    }
    res = requests.post(url, headers=headers)

    if res.status_code is not 201:
        return None

    data = res.json()
    return {
        'id': id,
        'apiKey': data['apiKey']
    }
