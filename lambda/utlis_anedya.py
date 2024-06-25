"""
Anedya utils
"""
import time
import json
import requests

node_id = ""
api_key = ""

def anedya_config(NODE_ID:str, API_KEY:str) -> None :
    """function to configure the anedya api key and node id"""
    global node_id, api_key
    node_id = NODE_ID
    api_key = API_KEY
    return None

def anedya_sendCommand(COMMAND_NAME:str, COMMAND_DATA:str):

    url = "https://api.anedya.io/v1/commands/send"
    api_key_in_formate = "Bearer " + api_key

    command_expiry_time = int(time.time() + 518400) * 1000

    payload = json.dumps(
        {
            "nodeid": node_id,
            "command": COMMAND_NAME,
            "data": COMMAND_DATA,
            "type": "string",
            "expiry": command_expiry_time,
        }
    )
    headers = {"Content-Type": "application/json", "Authorization": api_key_in_formate}

    requests.request("POST", url, headers=headers, data=payload,timeout=(5,10))

    # print(response.text)
    # st.write(response.text)

def anedya_setValue(KEY:str, VALUE:str):
    """function to set the data in the value storage """
    url = "https://api.anedya.io/v1/valuestore/setValue"
    api_key_in_formate = "Bearer " + api_key

    payload = json.dumps({
        "namespace": {
            "scope": "node",
            "id": node_id
        },
        "key": KEY,
        "value": VALUE,
        "type": "boolean"
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        "Authorization": api_key_in_formate
    }
    response = requests.request("POST", url, headers=headers, data=payload,timeout=(5,10))

    # print(response.status_code)
    # print(payload)
    print(response.text)
    return response

def anedya_getValue(KEY:str):
    """Function to stored data from the anedya value storage"""
    url = "https://api.anedya.io/v1/valuestore/getValue"
    api_key_in_formate = "Bearer " + api_key

    payload = json.dumps({
        "namespace": {
            "scope": "node",
            "id": node_id
        },
        "key": KEY
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        "Authorization": api_key_in_formate
    }

    response = requests.request("POST", url, headers=headers, data=payload,timeout=(5,10))
    response_message = response.text
    print(response_message)
    error_code = json.loads(response_message).get("errorcode")
    if error_code == 0:
        data = json.loads(response_message).get("value")
        value = [data, 1]
    else:
        print(response_message)
        # st.write("No previous value!!")
        value = [False, -1]

    return value

