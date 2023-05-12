import matplotlib.pyplot as plt
import numpy as np

x=np.array([10,60,15,15]);
lab=np.array(['app','baba','grap','man']);

plt.pie(x,labels=lab);
plt.show();