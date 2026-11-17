import numpy as np
import matplotlib.pyplot as plt
loads=np.array([10,20,30,40,50,60,70,80,90,100])
pdr=95-0.35*loads
delay=10+0.8*loads
throughput=loads*0.85
plt.figure(figsize=(8,5))
plt.plot(loads,pdr,'bo-',label='Packet Delivery Ratio (%)')
plt.plot(loads,throughput,'go-',label='Throughput (Mbps)')
plt.xlabel('Network Load (Number of Nodes)')
plt.ylabel('Performance')
plt.title('MANET Performance Analysis')
plt.legend()
plt.grid(True)
plt.show()
plt.figure(figsize=(8,5))
plt.plot(loads,delay,'ro-',label='Average Delay (ms)')
plt.xlabel('Network Load (Number of Nodes)')
plt.ylabel('Delay (ms)')
plt.title('MANET Delay Analysis')
plt.legend()
plt.grid(True)
plt.show()
for i in range(len(loads)):
    print(f"Load={loads[i]}, PDR={pdr[i]:.1f}%, Delay={delay[i]:.1f} ms, Throughput={throughput[i]:.1f} Mbps")
