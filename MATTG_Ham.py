# -*- coding: utf-8 -*-
"""
The Hamiltonian of the twist bilayer Graphene with magic angle xxx

@author: Curry
"""

from numpy import *
import numpy as np
from config import *

#define the interlayer hopping term matrix Tth
def T_mat(i):    
    return w0*s0 + w1*(cos((2*pi/3)*(i-1))*sx + sin((2*pi/3)*(i-1))*sy)

T1    =  T_mat(1)
T2   =  T_mat(2)
T3   =  T_mat(3)

T1_h   = np.array(np.matrix(T1).H)
T2_h  = np.array(np.matrix(T2).H)
T3_h  = np.array(np.matrix(T3).H)

invL = np.zeros((2*N+1, 2*N+1), int)
L = []

def Lattice(n):
    count = 0
    for i in np.arange(-n, n+1):
        for j in np.arange(-n, n+1):
            L.append([i, j])
            invL[i+n, j+n] = count
            count = count + 1

Lattice(N)
siteN = (2*N+1)**2
L = np.array(L)

print("invL is:", invL)
print("L is:", L)

def Hamiltonian(k):
    kx, ky = k
    
    H = array(zeros((6*siteN, 6*siteN)), dtype=complex)
    
    for i in np.arange(siteN):
        #diagonal term
        m = L[i, 0]
        n = L[i, 1]
        
        ax = kx - valley*K1[0] + m*b1m[0] + n*b2m[0]
        ay = ky - valley*K1[1] + m*b1m[1] + n*b2m[1] 
        
        qx = cos(theta/2) * ax + sin(theta/2) * ay
        qy =-sin(theta/2) * ax + cos(theta/2) * ay
        
        #diagonal term of the first layer 
        H[2*i, 2*i+1] = hv * (valley*qx - I*qy)
        H[2*i+1, 2*i] = hv * (valley*qx + I*qy)
        
        #diagonal term of the third layer
        H[2*i+4*siteN, 2*i+4*siteN+1] = hv * (valley*qx - I*qy)
        H[2*i+4*siteN+1, 2*i+4*siteN] = hv * (valley*qx + I*qy)
        
        ax2 = kx  - valley*K2[0] + m*b1m[0] + n*b2m[0] 
        ay2 = ky  - valley*K2[1] + m*b1m[1] + n*b2m[1]

        qx2 = cos(theta/2) * ax2 - sin(theta/2) * ay2
        qy2 = sin(theta/2) * ax2 + cos(theta/2) * ay2
        
        #diagonal term of the second layer 
        H[2*(i+siteN), 2*(i+siteN)+1] = hv * (valley*qx2 - I*qy2)
        H[2*(i+siteN)+1, 2*(i+siteN)] = hv * (valley*qx2 + I*qy2)

        #off-diagonal term when m1-m2==0 and n1-n2==0
        #lower left part (1st-layer -> 2nd-layer)
        j = i + siteN
        H[2*j, 2*i]     = T1_h[0, 0]
        H[2*j, 2*i+1]   = T1_h[0, 1]
        H[2*j+1, 2*i]   = T1_h[1, 0]
        H[2*j+1, 2*i+1] = T1_h[1, 1]
        
        #upper right part
        H[2*i, 2*j]     = T1[0, 0]
        H[2*i, 2*j+1]   = T1[0, 1]
        H[2*i+1, 2*j]   = T1[1, 0]
        H[2*i+1, 2*j+1] = T1[1, 1]
        
        #upper right part (2nd-layer -> 3rd-layer)
        H[2*j, 2*i+4*siteN]     = T1[0, 0]
        H[2*j, 2*i+4*siteN+1]   = T1[0, 1]
        H[2*j+1, 2*i+4*siteN]   = T1[1, 0]
        H[2*j+1, 2*i+4*siteN+1] = T1[1, 1]
        
            
        #lower left part
        H[2*i+4*siteN, 2*j]   = T1[0, 0]
        H[2*i+4*siteN, 2*j+1]   = T1[0, 1]
        H[2*i+4*siteN+1, 2*j]   = T1[1, 0]
        H[2*i+4*siteN+1, 2*j+1]   = T1[1, 1]
        
        
        #off-diagonal term when m1-m2==0, n1-n2==-1*valley
        if (n != valley*N):
            j = invL[m+N, n+valley*1+N] + siteN
            
            #lower left part (1st-layer -> 2nd-layer)
            H[2*j, 2*i]     = T2_h[0, 0]
            H[2*j, 2*i+1]   = T2_h[0, 1]
            H[2*j+1, 2*i]   = T2_h[1, 0]
            H[2*j+1, 2*i+1] = T2_h[1, 1]
            
            #upper right part
            H[2*i, 2*j]     = T2[0, 0]
            H[2*i, 2*j+1]   = T2[0, 1]
            H[2*i+1, 2*j]   = T2[1, 0]
            H[2*i+1, 2*j+1] = T2[1, 1]
            
            #upper right part (2nd-layer -> 3rd-layer)
            H[2*j, 2*i+4*siteN]     = T2_h[0, 0]
            H[2*j, 2*i+4*siteN+1]   = T2_h[0, 1]
            H[2*j+1, 2*i+4*siteN]   = T2_h[1, 0]
            H[2*j+1, 2*i+4*siteN+1] = T2_h[1, 1]
            
                
            #lower left part
            H[2*i+4*siteN, 2*j]   = T2[0, 0]
            H[2*i+4*siteN, 2*j+1]   = T2[0, 1]
            H[2*i+4*siteN+1, 2*j]   = T2[1, 0]
            H[2*i+4*siteN+1, 2*j+1]   = T2[1, 1]
            
            
        #off-diagonal term when m1-m2==1*valley, n1-n2==0
        if (m != -valley*N):
            j = invL[m-valley*1+N, n+N] + siteN
            
            #lower left part 1st-layer -> 2nd-layer)
            H[2*j, 2*i]     = T3_h[0, 0]
            H[2*j, 2*i+1]   = T3_h[0, 1]
            H[2*j+1, 2*i]   = T3_h[1, 0]
            H[2*j+1, 2*i+1] = T3_h[1, 1]
            
            #upper right part
            H[2*i, 2*j]     = T3[0, 0]
            H[2*i, 2*j+1]   = T3[0, 1]
            H[2*i+1, 2*j]   = T3[1, 0]
            H[2*i+1, 2*j+1] = T3[1, 1]
            
            #upper right part (2nd-layer -> 3rd-layer)
            H[2*j, 2*i+4*siteN]     = T3_h[0, 0]
            H[2*j, 2*i+4*siteN+1]   = T3_h[0, 1]
            H[2*j+1, 2*i+4*siteN]   = T3_h[1, 0]
            H[2*j+1, 2*i+4*siteN+1] = T3_h[1, 1]
            
                
            #lower left part
            H[2*i+4*siteN, 2*j]   = T3[0, 0]
            H[2*i+4*siteN, 2*j+1]   = T3[0, 1]
            H[2*i+4*siteN+1, 2*j]   = T3[1, 0]
            H[2*i+4*siteN+1, 2*j+1]   = T3[1, 1]
            
    return H

#set_printoptiopns in printing
np.set_printoptions(threshold=np.inf)
H = Hamiltonian(G)
#print(H[0][:])
