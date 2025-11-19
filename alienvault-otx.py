import requests
import json

def otx_lookup(api_key, indicator):
    url = f"https://otx.alienvault.com/api/v1/indicators/{indicator}"
    headers = {"X-OTX-API-KEY": api_key}
    return requests.get(url, headers=headers).json()
