# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 17:15:46 2024

@author: Curry
"""

from numpy import *
import numpy as np

#define constant
theta_v  = 0.7          #degree
w1  = 110.7          #interlayer hopping term //mev
r1 = 1  # w1/w0 in 1-2 layer
w0 = w1*(r1)

#r12 = 0.5  # w1/w0 in 1-2 layer
#w0 = w1*(r12)
d      = 1.420          #angstrom, whatever is ok.
hv     = 1.5*d*2970     #meV*angstrom, Fermi velocity for SLG
N      = 3              #truncate range
valley = +1             #+1 for K, -1 for K'
npoints  = 50           #density of k points, 50 is good

#parameters of continum model's moire bands 
theta  = theta_v/180.0*np.pi 
I      = complex(0, 1)
ei120  = cos(2*pi/3) + valley*I*sin(2*pi/3)
ei240  = cos(2*pi/3) - valley*I*sin(2*pi/3)

#The reciprocal lattice of moire brzone 
b1m  = 8*np.pi*sin(theta/2)/3/d*np.array([0.5, -np.sqrt(3)/2])
b2m  = 8*np.pi*sin(theta/2)/3/d*np.array([0.5, np.sqrt(3)/2])

#High sym points in moire 1st BZ
qb  = 8*np.pi*sin(theta/2)/3/sqrt(3)/d*array([0, -1])
K1  = 8*np.pi*sin(theta/2)/3/sqrt(3)/d*array([-sqrt(3)/2,-0.5])
K2  = 8*np.pi*sin(theta/2)/3/sqrt(3)/d*array([-sqrt(3)/2,0.5])
K2_p  = 8*np.pi*sin(theta/2)/3/sqrt(3)/d*array([sqrt(3)/2, 0.5])
M  = 8*np.pi*sin(theta/2)/3/sqrt(3)/d*array([-sqrt(3)/2,0]) 
G  = np.array([0,0]) 

#define the pauli matrices
s0 = np.array([[1,0],[0,1]], dtype=complex)
sx = np.array([[0,1],[1,0]], dtype=complex)
sy = np.array([[0,-1.j],[1.j, 0]], dtype=complex)
sz = np.array([[1,0],[0,-1]],  dtype=complex)

#others
sq3 = np.sqrt(3)