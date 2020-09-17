import numpy as np
import matplotlib.pyplot as plt

long_dom = 100
c = 300
nb_pts = 100
CFL = 1

delta_x = long_dom/nb_pts
delta_t = CFL*delta_x/c

x = np.linspace(0,long_dom+1, num=nb_pts,endpoint=False)
t0 = 0
tf = 1
nb_pas = int((tf-t0)/delta_t)

valeurs_back = np.zeros((nb_pas, nb_pts))

def diff_finie_back(CFL, u_n_j, u_n_jmoins):
       u_nplus_j = u_n_j - CFL*(u_n_j-u_n_jmoins)
       return u_nplus_j

def diff_finie_front(CFL, u_n_jplus, u_n_j):
       u_nplus_j = u_n_j - CFL*(u_n_j-u_n_jmoins)
       return u_nplus_j

def diff_finie_center(CFL, u_n_jplus, u_n_jmoins):
       u_nplus_j = u_n_j - CFL*(u_n_j-u_n_jmoins)
       return u_nplus_j



for i in range(nb_pas):
       plt.clf()
       for j in range(nb_pts):
              if i==0:
                     if (j*delta_x<40 or j*delta_x>60):
                            u_nplus_j = 0
                            valeurs_back[i][j] = u_nplus_j
                     elif (j*delta_x>=40 and j*delta_x<=60):
                            u_nplus_j = 100
                            valeurs_back[i][j] = u_nplus_j
              else:
                     if j==0:
                            u_n_jmoins = -valeurs_back[i-1][j-1]
                            u_n_j = valeurs_back[i-1][j]
                            
                     else:
                            u_n_jmoins = valeurs_back[i-1][j-1]
                            u_n_j = valeurs_back[i-1][j]
                     
                     u_nplus_j = diff_finie_back(CFL, u_n_j, u_n_jmoins)
                     valeurs_back[i][j] = u_nplus_j
       plt.figure(1)
       plt.plot(x,valeurs_back[i])
       plt.axis([0, 100, 0, 150])
       plt.xlabel('Distance sur le domaine (m)')
       plt.ylabel('Vitesse (m/s)')
       plt.show()
       plt.pause(0.1)

#%%
indice_t = int(0.0833/delta_t)
plt.figure(2)
plt.plot(x,valeurs_back[indice_t])
plt.axis([0, 100, 0, 150])
plt.xlabel('Distance sur le domaine (m)')
plt.ylabel('Vitesse (m/s)')
plt.show()                  
                     
              