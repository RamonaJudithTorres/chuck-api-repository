from enum import unique
import requests


url="https://api.chucknorris.io/jokes/random"

def get_api_chuck(url):
    responses=[]
    for response in range(25):
        response =requests.get(url)
        objecto_json= response.json()
        responses.append(objecto_json)
    unique_response  = list(
        {
            dictionary['id']: dictionary
            for dictionary in responses
        }.values())  
        
    return unique_response 