import json
import boto3
import requests

def lambda_handler(event, context):
    print(event)
    
    URL = "http://maps.googleapis.com/maps/api/geocode/json"
    location = event['landmark']
    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'address':location}
 
    # sending get request and saving the response as response object
    res = requests.get(url = URL, params = PARAMS)
    data = res.json()
 
    # extracting latitude, longitude and formatted address 
    latitude = data['results'][0]['geometry']['location']['lat']
    longitude = data['results'][0]['geometry']['location']['lng']
    formatted_address = data['results'][0]['formatted_address']
 
    # printing the output of the landmark --xxx added for stack3
    print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
      %(latitude, longitude,formatted_address))
    output = {"address":formatted_address} 
    
    return output
