import json

import requests
from msal import ConfidentialClientApplication

client_id = "1fake745-fake-4215-a270-aab4fake00e0"
client_secret = "gxI8Q~fakexv~FSJ.FjSVKdfakeoVmzklquFaKeR"
tenant_id = "ceFakec7-fd13-fake-b5d0-2fakeb6dad9b"

msal_authority = f"https://login.microsoftonline.com/{tenant_id}"

msal_scope = ["https://graph.microsoft.com/.default"]

msal_app = ConfidentialClientApplication(
    client_id=client_id,
    client_credential=client_secret,
    authority=msal_authority,
)

result = msal_app.acquire_token_silent(
    scopes=msal_scope,
    account=None,
)

if not result:
    result = msal_app.acquire_token_for_client(scopes=msal_scope)

if "access_token" in result:
    access_token = result["access_token"]
else:
    raise Exception("No Access Token found")

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
}

response = requests.get(
    url="https://graph.microsoft.com/v1.0/auditLogs/signIns", #Get Logs. Need P1 or P2 license
    headers=headers,
)

print(json.dumps(response.json(), indent=4))
