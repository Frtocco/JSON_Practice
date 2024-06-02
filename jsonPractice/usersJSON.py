import json
from urllib.request import urlopen

with urlopen("https://jsonplaceholder.typicode.com/users?format=json") as response:
    source = response.read()

data = json.loads(source)
print(type(data))

for user in data:
    print(user['id'])

for username in data:
    print(username['username'])

for geocords in data:
    print(geocords['username'], geocords['address']['geo']['lat'], geocords['address']['geo']['lng'])

print(data)