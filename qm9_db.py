# Dataset location: http://www.quantum-machine.org/

import numpy as np
import os

import matplotlib.pyplot as plt 
import seaborn as sns
sns.set_style('whitegrid')

path = os.fsencode('dsgdb9nsd.xyz')

charge = {'C' : 6, 'H' : 1, 'O' : 8, 'N' : 7, 'F' : 9}

# Atomic reference data
E_H = {'U0' : -0.500273 , 'U' : -0.498857 , 'H' : -0.497912 , 'G' : -0.510927}
E_C = {'U0' : -37.846772, 'U' : -37.845355, 'H' : -37.844411, 'G' : -37.861317}
E_N = {'U0' : -54.583861, 'U' : -54.582445, 'H' : -54.581501, 'G' : -54.598897}
E_O = {'U0' : -75.064579, 'U' : -75.063163, 'H' : -75.062219, 'G' : -75.079532}
E_F = {'U0' : -99.718730, 'U' : -99.717314, 'H' : -99.716370, 'G' : -99.733544}
E_0 = {'U0' : 0.0, 'U' : 0.0, 'H' : 0.0, 'G' : 0.0}

E_ref = {1 : E_H, 
         6 : E_C, 
         7 : E_N, 
         8 : E_O, 
         9 : E_F,
         0 : E_0}

n_at = []
z_mol = []
r_mol = []
indx_mol = [] # Consecutive, 1-based integer identifier of molecule
mu_mol = [] # Dipole moment
alpha_mol = [] # Isotropic polarizability
homo_mol = [] # Energy of Highest occupied molecular orbital (HOMO)
lumo_mol = [] # Energy of Lowest occupied molecular orbital (LUMO)
gap_mol = [] # Gap, difference between LUMO and HOMO
r2_mol = [] # Electronic spatial extent
zpve_mol = [] # Zero point vibrational energy
U0_mol = [] # Internal energy at 0 K
U_mol = [] # Internal energy at 298.15 K
H_mol = [] # Enthalpy at 298.15 K
G_mol = [] # Free energy at 298.15 K
Cv_mol = [] # Heat capacity at 298.15 K
omega_mol = []

for entry in os.scandir(path): 
    with open(entry.path,"r") as file:
        lines = [line.strip().split() for line in file]
    na = int(lines[0][0])
    n_at.append(na)
    indx_mol.append(int(lines[1][1]))
    mu_mol.append(float(lines[1][5]))
    alpha_mol.append(float(lines[1][6]))
    homo_mol.append(float(lines[1][7]))
    lumo_mol.append(float(lines[1][8]))
    gap_mol.append(float(lines[1][9]))
    r2_mol.append(float(lines[1][10]))
    zpve_mol.append(float(lines[1][11]))
    U0_mol.append(float(lines[1][12]))
    U_mol.append(float(lines[1][13]))
    H_mol.append(float(lines[1][14]))
    G_mol.append(float(lines[1][15]))
    Cv_mol.append(float(lines[1][16]))
    z_mol.append([charge[lines[i][0]] for i in range(2,na+2)])
    r_mol.append([ list(map(lambda x: float(x.replace('*^','e')) ,lines[i][1:4])) for i in range(2,na+2)])
    omega_mol.append(     max( list(map(lambda x: float(x) ,lines[na+2][:]))  )    )                 

n_atoms = np.array(n_at, dtype=int)
print('n_atoms', n_atoms.shape, type(n_atoms), n_atoms.min(), n_atoms.max())

n_molec = n_atoms.shape[0]
print('n_molec',n_molec)

max_atoms = len(sorted(z_mol, key=len, reverse=True)[0])
print('max_atoms',max_atoms,'\n')

Z = np.array([x+[0]*(max_atoms-len(x)) for x in z_mol])
print('Z', Z.shape, type(Z), '\n', Z[0])

R = np.array([x+[[0.0]*3]*(max_atoms-len(x)) for x in r_mol])
print('R', R.shape, type(R))

indx = np.array(indx_mol, dtype=int) # Consecutive, 1-based integer identifier of molecule
print('\nindx', indx.shape, type(indx), indx.min(), indx.max(),'\n')

mu = np.array(mu_mol, dtype=float) # Dipole moment

alpha = np.array(alpha_mol, dtype=float) # Isotropic polarizability

homo = np.array(homo_mol, dtype=float) # Energy of Highest occupied molecular orbital (HOMO)

lumo = np.array(lumo_mol, dtype=float) # Energy of Lowest occupied molecular orbital (LUMO)

gap = np.array(gap_mol, dtype=float) # Gap, difference between LUMO and HOMO

lumo_homo_gap = lumo-homo-gap
#print('lumo_homo_gap', lumo_homo_gap.shape, type(lumo_homo_gap), lumo_homo_gap.min(), lumo_homo_gap.max(),'\n',lumo_homo_gap[:3])

r2 = np.array(r2_mol, dtype=float) # Electronic spatial extent

zpve = np.array(zpve_mol, dtype=float) # Zero point vibrational energy

U0 = np.array(U0_mol, dtype=float) # Internal energy at 0 K

for i in range(len(U0)):
    U0[i] = U0[i] - sum(E_ref[x]['U0'] for x in Z[i])

U = np.array(U_mol, dtype=float) # Internal energy at 298.15 K

for i in range(len(U)):
    U[i] = U[i] - sum(E_ref[x]['U'] for x in Z[i])

H = np.array(H_mol, dtype=float) # Enthalpy at 298.15 K

for i in range(len(H)):
    H[i] = H[i] - sum(E_ref[x]['H'] for x in Z[i])

G = np.array(G_mol, dtype=float) # Free energy at 298.15 K

for i in range(len(G)):
    G[i] = G[i] - sum(E_ref[x]['G'] for x in Z[i])

Cv = np.array(Cv_mol, dtype=float) # Heat capacity at 298.15 K

omega = np.array(omega_mol, dtype=float) # the highest fundamental vibrational wavenumber

# ------------------------------------------------------------------------------------

y = np.column_stack((mu[:,np.newaxis],
                     alpha[:,np.newaxis],
                     homo[:,np.newaxis],
                     lumo[:,np.newaxis],
                     gap[:,np.newaxis],
                     r2[:,np.newaxis],
                     zpve[:,np.newaxis],
                     U0[:,np.newaxis],
                     U[:,np.newaxis],
                     H[:,np.newaxis],
                     G[:,np.newaxis],
                     Cv[:,np.newaxis],
                     omega[:,np.newaxis]))

labs=['mu','alpha','homo','lumo','gap','r2','zpve','U0','U','H','G','Cv','omega']

print('y', y.shape)

n_prop = y.shape[1]      # number of target properties
print('Number of target properties:',n_prop,'\n')

for i in range(n_prop):
    print(labs[i], '\t%.4f\t\t%.4f\t\t%.4f' % (y[:,i].min(), y[:,i].mean(), y[:,i].max()))

# ------------------------------------------------------------------------------------

N = np.array([(z>1).sum() for z in Z]) # number of heavy atoms in molecule
print('\nN', N.shape, N.min(), N.max())
Nu = np.bincount(N)
Nii = np.nonzero(Nu)[0]
print(np.vstack((Nii,Nu[Nii])).T,'\n')

# ------------------------------------------------------------------------------------
ind_exclude = np.loadtxt('ind_exclude.txt',dtype='int32')

indx_0 = np.setdiff1d(indx,ind_exclude) # some papers exclude them, others don't
print('indx_0', indx_0.shape,'\n')
# ------------------------------------------------------------------------------------

indx_9 = indx[N==9] # molecules with 9 heavy atoms
print('indx_9', indx_9.shape,'\n')

y_9 = y[N==9,:]
print('y_9', y_9.shape)

for i in range(n_prop):
    print(labs[i], '\t%.4f\t\t%.4f\t\t%.4f\t\t%.4f' % (y_9[:,i].min(), y_9[:,i].mean(), y_9[:,i].max(), np.absolute(y_9[:,i]).max()))

for i in range(n_prop):
    sns.distplot(y_9[:,i]/(np.absolute(y_9[:,i]).max()), label=labs[i], hist=False, norm_hist=True)

plt.legend()
plt.show()
