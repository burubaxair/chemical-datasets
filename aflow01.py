# http://aflowlib.org/

from aflow import K, search

result = search(
        ).filter((K.species == "Al") & (K.species == "O")
        ).select(K.compound, 
                 K.Egap)

print('Number of results found:',len(result),'\n')

print("%-20s %-20s" 
       %  ('Compound', 'Band Gap (eV)'),
    '\n')

for entry in result:
    print("%-20s %-20s" 
        % (entry.compound, entry.Egap))