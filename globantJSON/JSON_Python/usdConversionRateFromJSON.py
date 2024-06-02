import json
from urllib.request import urlopen

with urlopen("https://www.x-rates.com/table/?from=USD&amount=1?format=json") as response:
    source = response.read()

data = json.loads(source)
print(data)