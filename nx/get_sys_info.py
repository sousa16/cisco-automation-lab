import requests, urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

session = requests.Session()

URL = "https://sbx-nxos-mgmt.cisco.com/api/aaaLogin.json"
PAYLOAD = {
    "aaaUser": {
        "attributes": {
            "name": "joasousa",
            "pwd": "9--Gcb4OUtn9PQh"
        }
    }
}

# Make the POST request to get the authentication token
response = session.post(URL, json=PAYLOAD, verify=False)

# Define SYS_URL variable to get system information
SYS_URL = "https://sbx-nxos-mgmt.cisco.com/api/mo/sys.json"

sys_info = session.get(SYS_URL, verify=False).json()["imdata"][0]["topSystem"]["attributes"]

print("Hostname:", sys_info["name"])
print("Serial Number:", sys_info["serial"])
print("Uptime:", sys_info["systemUpTime"])