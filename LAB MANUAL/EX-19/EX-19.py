import numpy as np
import matplotlib.pyplot as plt
nodes=np.array([[0,0],[10,5],[20,10],[30,15]])
tx_power=0
d0=1
n=2
for i in range(len(nodes)):
    for j in range(i+1,len(nodes)):
        d=np.linalg.norm(nodes[i]-nodes[j])
        d=max(d,d0)
        rssi=tx_power-10*n*np.log10(d/d0)
        print(f"Node {i+1} to Node {j+1}: Distance={d:.2f} m, Signal={rssi:.2f} dBm")
plt.scatter(nodes[:,0],nodes[:,1],color="blue")
for i,(x,y) in enumerate(nodes):
    plt.text(x,y,f"Node {i+1}")
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.title("Signal Strength Between Nodes")
plt.grid(True)
plt.show()
