import requests
import pdb
import json
# pdb.set_trace()

def provider_url(provider, zipcode):
  return {
    'viacep': 'https://viacep.com.br/ws/'+zipcode+'/json/',
    'postmon': 'http://api.postmon.com.br/v1/cep/'+zipcode
  }[provider]

def request_address(provider, zipcode):
  url = provider_url(provider, zipcode)

  response = requests.get(url)
  response.raise_for_status()

  return response

def get_address(zipcode):
  try:
    response = request_address('postmon', zipcode)
  except:
    response = request_address('viacep', zipcode)

  return response

print('Loading function')


def lambda_handler(event, context):
  print('Loaded!')
  print('Received event: ' + json.dumps(event, indent=2))

  for record in event['Records']:
      # print(record['eventID'])
      print(record['eventName'])
      # print("DynamoDB Record: " + json.dumps(record['dynamodb'], indent=2))
      if(record['eventName'] == 'INSERT'):
          print('ZIPCODENUMBER: ' + record['dynamodb']['Keys']['zipcode']['S'])
  return 'Successfully processed {} records.'.format(len(event['Records']))
