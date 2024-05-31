import json
from urllib.request import urlopen

with urlopen("https://api.adviceslip.com/advice?format=json") as response:
    source = response.read()

print(type(source))
data = json.loads(source)
print(data)
print(type(data))

print(data['slip']['id'],data['slip']['advice'])



