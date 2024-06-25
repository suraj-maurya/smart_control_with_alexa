# smart_control_with_alexa


## Set-Up

1. Download this repo and unzip it.
2. Open the `en-IN.json` and `en-US.json` files and enter your invocation name:
   ```
   "invocationName": "YOUR-ALEXA-INVOCATION-NAME"
   ```
3. Fill in your Node ID and API key in the lambda_function.py file
```
node_id = "YOUR-NODE_ID"  # Get it from the anedya node description 
api_key = "YOUR-API-KEY"  # Get it from the anedya project dashboard
```
4. Save the file and create a zip file of it.
5. Go to the Alexa Developer Console -> Code section. Click on "Import Code"