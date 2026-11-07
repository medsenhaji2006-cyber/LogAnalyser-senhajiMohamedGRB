import requests
import concurrent
from requests import Response

def get_location(ip):
    response=requests.get("https://ipinfo.io/"+ip+"/json")
    if response.status_code==200:

        print(response.json()) 

if __name__ == "__main__":
    print(get_location("196.65.181.117"))   
    