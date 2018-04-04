# Dataset location: http://www.quantum-machine.org/

import numpy as np
from scipy.io import loadmat

import matplotlib.pyplot as plt 
import seaborn as sns
sns.set_style('whitegrid')

qm7_dict = loadmat('qm7.mat')

print(qm7_dict.keys(),"\n")

qm7_descr = {'X' : 'Coulomb matrices', 
             'R' : 'cartesian coordinates', 
             'Z' : 'atomic charges', 
             'T' : 'atomization energies', 
             'P' : 'splits for cross-validation'}

for key, value in qm7_dict.items():
    if isinstance(value, np.ndarray):
        print(key, ": ", qm7_descr[key], value.shape, "\n", value, "\n")
    else:
        print(key, ": ", value, "\n")

X = qm7_dict['X']
R = qm7_dict['R']
Z = qm7_dict['Z']
T = qm7_dict['T']
P = qm7_dict['P']

y = T[0,:]

print('Atomization energies, kcal/mol ','\t%.4f\t\t%.4f\t\t%.4f' % (y.min(), y.mean(), y.max()))

sns.distplot(y/(np.absolute(y).max()), hist=False, norm_hist=True)
plt.show()