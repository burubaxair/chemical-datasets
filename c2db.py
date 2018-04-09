#https://cmr.fysik.dtu.dk/c2db/c2db.html

import ase.db # https://wiki.fysik.dtu.dk/ase/

con = ase.db.connect('c2db.db')

print('Number of records: ',len(list(con.select())),'\n')

print("%-12s %-20s %-20s %-20s %-20s" 
  %  ('Material', 'Elastic tensor (xx)', 
                  'Elastic tensor (xy)', 
                  'Elastic tensor (yy)', 
                  'Band gap (PBE), eV'), '\n')

for row in con.select():
    data =  row.key_value_pairs
    print( "%-12s %-20s %-20s %-20s %-20s" 
      % (row.formula, data.get('c_11'), 
                      data.get('c_12'), 
                      data.get('c_22'),
                      data.get('gap')))

