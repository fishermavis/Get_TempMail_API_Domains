from http.client import responses
import requests
import json

url = "https://privatix-temp-mail-v1.p.rapidapi.com/request/domains/"

headers = {
	"X-RapidAPI-Key": "######",
	"X-RapidAPI-Host": "privatix-temp-mail-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

domain_list = response.text


print("The current tmp-mail domains are:\n")
print(domain_list)

