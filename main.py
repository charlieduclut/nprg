from pylab import *
import numpy as np
import matplotlib.pyplot as plt
from time import time

from global_variables import *
from step_dicho import *

Ndicho=30

kmin=3.
kmax=6.
kappa=(kmin+kmax)/2.

folderPath='results/N'+str(int(NN))+'d'+str(int(dim))+'alpha'+str(int(alpha))+'NT'+str(NT)+'Nrho'+str(Nrho)+'NQ'+str(NQ)+'/'
fileName=folderPath+'Veta-'+str(Ndicho)+'-'+str(Nomeg)+'-'+str(Lomeg)+'-'+str(beta)+'-'+str(kappa)+'-moinsomega'
etaZResults=[]
etaXResults=[]
Vresults=[]
kappaResults=[]

tsimu = time()
for i in range(Ndicho):
  print "i=",i, " time =",(time()-tsimu),"for simu ",fileName
  kappa=(kmin+kmax)/2.
  print "kappa=",kappa
  Vinit=0.1*(rho-kappa)#linspace(-0.3,0.7,Nrho)+vmid
  
  phase,etaZPlot,etaXPlot,Vplot=step_dicho(Vinit) #phase=0 : low temp, =1, high temp
  
  if phase==0:
    kmax = kappa
  else:
    kmin=kappa
  
  etaZResults.append(np.array(etaZPlot))
  etaXResults.append(np.array(etaXPlot))
  Vresults.append(np.array(Vplot))
  kappaResults.append(kappa)


etaZResults=np.array(etaZResults)
etaXResults=np.array(etaXResults)
Vresults=np.array(Vresults)
kappaResults=np.array(kappaResults)
np.savez(fileName,etaZResults=etaZResults,etaXResults=etaXResults,Vresults=Vresults,kappaResults=kappaResults)
print "SIMU beta=",beta," IS TERMINAOUCH after ",time()-tsimu,"seconds"
