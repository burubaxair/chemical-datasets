# https://github.com/materialsproject/mapidoc

import json
import requests

data = {
    'criteria': {
        'elements': {'$in': ['Al', 'Ga', 'In'], '$all': ['O']},
        'nelements': {'$lte': 4},
    },
    'properties': [
        'pretty_formula',
        'formation_energy_per_atom',
        'band_gap'
    ]
}

r = requests.post('https://materialsproject.org/rest/v2/query',
                 headers={'X-API-KEY': 'Your-API-Key'},
                 data={k: json.dumps(v) for k,v in data.items()})

response_content = r.json() # a dict

print('Search criteria: ', response_content['criteria'])
print('Properties: ', response_content['properties'])
print('Number of results: ', response_content['num_results'],'\n')

print('\tE_f_per_atom\tbandgap')

for k in response_content['response']:
    print(k['pretty_formula'], '\t%.4f\t\t%.4f' %(k['formation_energy_per_atom'],k['band_gap']))