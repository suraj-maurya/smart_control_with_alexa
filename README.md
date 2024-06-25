# smart_control_with_alexa


## Set-Up

- Download this repo and unzip.
- Open en-IN.json and en-US.json files and enter your Invocation name.
```
      "invocationName": "YOUR-ALEXA-INVOCATION-NAME"
```
- Fill your Node Id and Api key. In lambda_function.py file.
```
node_id = "YOUR-NODE_ID"  # Get it from the anedya node description 
api_key = "YOUR-API-KEY"  # Get it from the anedya project dashboard
```
- Save the file and Make its zip file
- Go to alexa developer console -> code section. Click on import code.