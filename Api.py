import os,json
from pydo import Client
from requests import post,get
api_token = 'dop_v1_65bc0f003d5e31ad9c3ab7c2fc6c5306c265ede0ae538a1c5b5f6c1104984240'  #Paste the api code here
headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {api_token}'}  # Header information that will be sent to the digitalocean in order to authenticate user

def get_balance_info():
    api_customers_balance = 'https://api.digitalocean.com/v2/customers/my/balance'  #Url that will be used to call API request
    response = requests.get(api_customers_balance, headers=headers)     #Get the response from API after sending request
    if response.status_code == 200:                       #If response is success, show the response. Otherwise return nothing
        print(json.loads(response.content.decode('utf-8')))
    else:
        return None
get_balance_info();
