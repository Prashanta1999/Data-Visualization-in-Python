#Code to plot axis of a graph 
import numpy as np
from matplotlib import pyplot as plt

plt.plot(np.array([1,2,3,4]),'ro')
# plt.plot(np.array([[1,2,3,4],[1,4,9,16]]),'ro')
plt.axis([0,6,0,20])
plt.title("Axis")
plt.plot(np.array([[1,2,3,4],[1,4,9,16]]),'ro')
plt.show()
