''' JavaScript Object Notation '''
import json

with open('states.json') as f:
  data = json.load(f)

for state in data['states']:
  del state['area_codes']

for abbreviation in data['states']:
  del abbreviation['abbreviation']

with open('states_only.json', 'w') as f:
  json.dump(data, f, indent=2)