#https://cmr.fysik.dtu.dk/catapp/catapp.html

import ase.db # https://wiki.fysik.dtu.dk/ase/

con = ase.db.connect('catapp.db')

print('Number of records: ',len(list(con.select())),'\n')

print("%-12s %-12s %-12s %-40s %-18s %-18s %-18s" 
       %  ('Reactant A', 'Reactant B', 'Product', 'Surface', 'Adsorption site', 'E_reaction (eV)', 'E_activation (eV)'),
    '\n')

for row in con.select():
    data = row.key_value_pairs
    print("%-12s %-12s %-12s %-40s %-18s %-18s %-18s"  
           % (data.get('a'),
              data.get('b'),
              data.get('ab'),
              data.get('surface'),
              data.get('site'),
              data.get('er'),
              data.get('ea')))


