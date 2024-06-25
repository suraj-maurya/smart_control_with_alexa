# smart_control_with_alexa


## Set-Up

1. Download this repo and unzip.
2. Open en-IN.json and en-US.json files and enter your Invocation name.
```
      "invocationName": "YOUR-ALEXA-INVOCATION-NAME"
```
3. Fill your Node Id and Api key. In lambda_function.py file.
```
node_id = "YOUR-NODE_ID"  # Get it from the anedya node description 
api_key = "YOUR-API-KEY"  # Get it from the anedya project dashboard
```
4. Save the file and Make its zip file
5. Go to alexa developer console -> code section. Click on import code.