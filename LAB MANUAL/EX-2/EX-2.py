import matplotlib.pyplot as plt
import numpy as np
n=7
a=np.linspace(0,2*np.pi,7,endpoint=False)
x=[0]+list(2*np.cos(a))
y=[0]+list(2*np.sin(a))
c=['red','blue','green','yellow','blue','green','yellow','red']
for i in range(8):
    plt.scatter(x[i],y[i],s=1800,c=c[i],edgecolors='black')
    plt.text(x[i],y[i],f'Cell {i+1}',ha='center',va='center',fontsize=9)
plt.title("Cellular Layout and Frequency Reuse")
plt.axis('equal')
plt.axis('off')
plt.show()
