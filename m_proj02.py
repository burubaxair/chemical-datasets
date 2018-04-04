from pymatgen import MPRester

m = MPRester("Your-API-Key")

query = {
    'elements': {'$in': ['Al', 'Ga', 'In'], '$all': ['O']},
    'nelements': {'$lte': 4},
}

properties = [
    'pretty_formula',
    'formation_energy_per_atom',
    'band_gap'
]

data = m.query(query, properties)

print('Query: ', query)
print('data: ', type(data))
print('Number of results: ', len(data),'\n')

print('\tE_f_per_atom\tbandgap')

for d in data:
    print(d.get('pretty_formula'), '\t%.4f\t\t%.4f' %(
          d.get('formation_energy_per_atom'),
          d.get('band_gap')))