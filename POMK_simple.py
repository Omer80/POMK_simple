"""
Simple POMK solver
"""
__version__=1.0
__author__ = """Omer Tzuk (omertz@post.bgu.ac.il)"""

import numpy
import matplotlib.pyplot as plt
from rhs import dbdt,dwdt


# Model's parameters
d = 7.335
p = 0.985934
m = 0.5
n = 64
l = 32.0

# initial condition
b0 = 0.5*(numpy.random.random(n))  # random initial conditions
w0 = 0.5*(numpy.random.random(n))  # random initial conditions

start  = 0.0
step   = 5.0
finish = 500.0
dt     = 0.1


dx  = float(l/n)
dx2 = dx**2
X = numpy.linspace(0,l,n)
b_n = b0.copy()
w_n = w0.copy()
plt.ion()
title=plt.title('time=%2.1f'%start)
plt.xlim(0,l)
plt.ylim(0,3)
plt.draw()

t=start

# start loop
for tout in numpy.arange(start+step,finish+step,step):
    while t < tout:
		#print t
		b_n_plus_1 = b_n + dt*dbdt(b_n,w_n,p,m,d,dx2)
		w_n_plus_1 = w_n + dt*dwdt(b_n,w_n,p,m,d,dx2)
		#print max(b_n), max(w_n)
		b_n = b_n_plus_1
		w_n = w_n_plus_1
		plt.clf()
		t+=dt
    plt.clf()
    plt.xlim(0,l)
    plt.ylim(-2,2)
    plt.plot(X,b_n,'g')
    plt.plot(X,w_n,'b')
    title.set_text('time=%.1f'%(t))
    plt.draw()
    
