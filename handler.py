
import countryApi
import requests
import json

def response(text):
    respHeaders = {
        'Access-Control-Allow-Origin': '*'
    }

    return {
        'statusCode': 200,
        'headers':respHeaders,
        'body': json.dumps(text)
    }

def hello(event, context):
    print(event)
    path=event['requestContext']['resourcePath']
    pathParams=event['pathParameters']
    print('path             : ' + path)
    if(path=='/country/all'):
        body=countryApi.init()
    elif(path=='/country/name/{country-name}'):
        body=countryApi.getCountry(pathParams['country-name'])
    elif(path=='/country/capital/{capital-name}'):
        body=countryApi.getCountryByCapital(pathParams['capital-name'])
    return response(body)

