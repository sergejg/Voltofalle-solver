import numpy as np
from numpy.core.numeric import count_nonzero

a = np.array([[0,1,2],[0,0,3]],dtype=int)
print(np.count_nonzero(a))
#print([np.where(a[:,0]==0,)),np.where(a[:,1]==0)),np.count_nonzerowhere(a[:,2]==0)])
a = [False, False, False]
print(not(any(a)))