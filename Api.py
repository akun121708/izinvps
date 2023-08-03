import os,json,requests
from pydo import Client
from requests import post,get
API_DROPLET = 'dop_v1_a6f72e9dee9ebec0931e76bab41d9b9b40137bec181a2160adbd6766e0881433'  #Paste the api code here
headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {API_DROPLET}'}  # Header information that will be sent to the digitalocean in order to authenticate user

def Get_Droplet_info():
    api_customers_balance = 'https://api.digitalocean.com/v2/droplets' #Url that will be used to call API request
    response = requests.get(api_customers_balance, headers=headers) #Get the response from API after sending request
    Database = requests.get(api_customers_balance, headers=headers).json() #Get the response from API after sending request
    NameDict =  json.loads(response.content.decode('utf-8'))
    if response.status_code == 200: #If response is success, show the response. Otherwise return nothing
        print(NameDict['droplets'][0]['id'])
        print(NameDict['droplets'][0]['name'])
        print('------------')
        print(NameDict['droplets'][1]['id'])
        print(NameDict['droplets'][1]['name'])
        print('------------')
        print(NameDict['droplets'][3]['id'])
        print(NameDict['droplets'][3]['name'])
        print('------------')
        print(NameDict['droplets'][4]['id'])
        print(NameDict['droplets'][4]['name'])
        print('------------')
    else:
        print(response.status_code)
        return None
Get_Droplet_info();
