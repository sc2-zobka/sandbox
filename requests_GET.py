import requests, json

# API documentation https://swapi.dev/documentation

# GET Method

# API endpoint
URL = 'https://swapi.dev/api/people/'
PARAMS = {
    "search": "Darth Vader"
          }

r = requests.get(url=URL, params=PARAMS)
data = r.json()


print(data["results"][0]['name'])

# r = requests.get(URL) => Response Obj
# r.status_code => Integer
# r.text => String
# r.headers => access the header
# r.content => content of the response in bytes
# r.url => full URL

# Serialize obj to a JSON formatted str
# json_obj = json.dumps(data)
