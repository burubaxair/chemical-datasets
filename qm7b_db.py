# Dataset location: http://www.quantum-machine.org/

import numpy as np
from scipy.io import loadmat

import matplotlib.pyplot as plt 
import seaborn as sns
sns.set_style('whitegrid')


qm7b_dict = loadmat('qm7b.mat')

print(qm7b_dict.keys(),"\n")

qm7b_descr = {'X' : 'Coulomb matrices', 
              'T' : 'molecular properties',
              'names': 'names of the properties'} # names of properties are in a strange encoding: unreadable

# print the data
for key, value in qm7b_dict.items():
    if isinstance(value, np.ndarray) and key != 'names':
        print(key, ": ", qm7b_descr[key], value.shape)
    elif key != 'names':
        print(key, ": ", value, "\n")

X = qm7b_dict['X']
n_molec = X.shape[0]    # number of molecules (number of labeled examples)
max_atoms = X.shape[1]  # max number of atoms in a molecule
print('Max number of atoms in a molecule', max_atoms)

# targets (labels)
y = np.zeros_like(qm7b_dict['T'])
n_prop = y.shape[1]      # number of target properties
print('Number of target properties:',n_prop,'\n')

y[:,0]  = qm7b_dict['T'][:,0]*0.043  # Atomization energies, eV. In the database, they are in kcal/mole, we convert them to eV here
y[:,1]  = qm7b_dict['T'][:,1]  # Excitation energies, eV
y[:,2]  = qm7b_dict['T'][:,2]  # Maximal absorption intensities, arbitrary units
y[:,3]  = qm7b_dict['T'][:,3]  # HOMO(ZINDO), eV
y[:,4]  = qm7b_dict['T'][:,4]  # LUMO(ZINDO), eV
y[:,5]  = qm7b_dict['T'][:,5]  # First excitation energies, eV
y[:,6]  = qm7b_dict['T'][:,6]  # Ionization potentials, eV
y[:,7]  = qm7b_dict['T'][:,7]  # Electron affinity, eV
y[:,8]  = qm7b_dict['T'][:,8]  # HOMO_PBE0, eV
y[:,9]  = qm7b_dict['T'][:,9]  # LUMO_PBE0,  eV
y[:,10] = qm7b_dict['T'][:,10] # HOMO_GW, eV
y[:,11] = qm7b_dict['T'][:,11] # LUMO_GW, eV
y[:,12] = qm7b_dict['T'][:,12] # PBE0 molecular polarizabilities, A^3
y[:,13] = qm7b_dict['T'][:,13] # SCS molecular polarizabilities, A^3


y_min = y.min(axis=0)
y_max = y.max(axis=0)
y_mean = y.mean(axis=0)
y_std = y.std(axis=0)

print('min, mean, and max values of the target properties:\n')
print('Atomization energies, eV                        ','\t%.4f\t\t%.4f\t\t%.4f' % (y_min[0], y_mean[0], y_max[0]))
print('Excitation energies, eV                         ','\t%.4f\t\t%.4f\t\t%.4f' % (y_min[1], y_mean[1], y_max[1]))
print('Maximal absorption intensities,  arbitrary units','\t%.4f\t\t%.4f\t\t%.4f' % (y_min[2], y_mean[2], y_max[2]))
print('HOMO_ZINDO, eV                                  ','\t%.4f\t\t%.4f\t\t%.4f' % (y_min[3], y_mean[3], y_max[3]))
print('LUMO_ZINDO, eV                                  ','\t%.4f\t\t%.4f\t\t%.4f' % (y_min[4], y_mean[4], y_max[4]))
print('First excitation energies, eV                   ','\t%.4f\t\t%.4f\t\t%.4f' % (y_min[5], y_mean[5], y_max[5]))
print('Ionization potentials, eV                       ','\t%.4f\t\t%.4f\t\t%.4f' % (y_min[6], y_mean[6], y_max[6]))
print('Electron affinity, eV                           ','\t%.4f\t\t%.4f\t\t%.4f' % (y_min[7], y_mean[7], y_max[7]))
print('HOMO_PBE0, eV                                   ','\t%.4f\t\t%.4f\t\t%.4f' % (y_min[8], y_mean[8], y_max[8]))
print('LUMO_PBE0,  eV                                  ','\t%.4f\t\t%.4f\t\t%.4f' % (y_min[9], y_mean[9], y_max[9]))
print('HOMO_GW, eV                                     ','\t%.4f\t\t%.4f\t\t%.4f' % (y_min[10], y_mean[10], y_max[10]))
print('LUMO_GW, eV                                     ','\t%.4f\t\t%.4f\t\t%.4f' % (y_min[11], y_mean[11], y_max[11]))
print('PBE0 molecular polarizabilities, A^3            ','\t%.4f\t\t%.4f\t\t%.4f' % (y_min[12], y_mean[12], y_max[12]))
print('SCS molecular polarizabilities, A^3             ','\t%.4f\t\t%.4f\t\t%.4f' % (y_min[13], y_mean[13], y_max[13]))


labs = ['E','E_*','I','HOMO_ZINDO','LUMO_ZINDO','E1','IP','EA','HOMO_PBE0','LUMO_PBE0','HOMO_GW','LUMO_GW','alpha_PBE0','alpha_SCS',]

for i in range(n_prop):
    sns.distplot(y[:,i]/(np.absolute(y[:,i]).max()), label=labs[i], hist=False, norm_hist=True)
plt.legend()
plt.show()