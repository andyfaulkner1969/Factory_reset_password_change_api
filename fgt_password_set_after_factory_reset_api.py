#!/usr/bin/env python3

import json
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

###########################################################################################
# This script will set a password for a newly factory reset FGT via API
###########################################################################################

host = "10.20.20.11"
passwd = "Danni1993!"

payload = {
	"username" : "admin",
}

# Note: On a non-licensed FGT-VM HTTPS is not supported until a license is applied.
#  you have to use http. 

try:
	url = "http://" + host +"/api/v2/authentication" 
	x = requests.post(url, json= payload,verify=False)
	parsed_json = json.loads(x.text)
	print(parsed_json['status_message'])
	
except:
	print("Didn't work")

payload = {
	"username" : "admin",
	"new_password1" : passwd,
	"new_password2" : passwd,
}

try:
	y = requests.post(url, json= payload,verify=False)
	parsed_json = json.loads(y.text)
	print(parsed_json['status_message'])
except:
	print("Didn't work")


	

