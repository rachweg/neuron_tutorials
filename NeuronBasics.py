#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 17:21:51 2021

@author: rachweg
"""


from neuron import h
import matplotlib.pyplot as plt

soma = h.Section(name='soma')
soma.L = 20
soma.diam = 20
soma.insert('hh')
iclamp = h.IClamp(soma(0.5))
print([item for item in dir(iclamp) if not item.startswith('__')])
iclamp.delay = 2
iclamp.dur = 0.1
iclamp.amp = 0.9
v = h.Vector().record(soma(0.5)._ref_v)             # Membrane potential vector
t = h.Vector().record(h._ref_t)                     # Time stamp vector
h.load_file('stdrun.hoc')
h.finitialize(-65)
h.continuerun(40)
plt.figure()
plt.plot(t, v)
plt.xlabel('t (ms)')
plt.ylabel('v (mV)')
plt.show()
