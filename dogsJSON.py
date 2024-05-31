import json
from urllib.request import urlopen

with urlopen("https://dog.ceo/api/breeds/image/random?format=json") as response:
    source = response.read()

data = json.loads(source)
print(data)
print(data['message'])