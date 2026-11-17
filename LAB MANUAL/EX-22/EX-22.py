import matplotlib.pyplot as plt
import random
from collections import deque
from matplotlib.animation import FuncAnimation
x=deque(maxlen=30)
y=deque(maxlen=30)
fig,ax=plt.subplots()
line,=ax.plot([],[], 'b-o')
def update(frame):
    x.append(frame)
    y.append(random.uniform(1,100))
    line.set_data(x,y)
    ax.set_xlim(max(0,frame-29),max(30,frame))
    ax.set_ylim(0,110)
    ax.set_xlabel("Time (seconds)")
    ax.set_ylabel("Throughput (Mbps)")
    ax.set_title("Live Network Throughput Monitoring")
    ax.grid(True)
    return line,
ani=FuncAnimation(fig,update,interval=1000,cache_frame_data=False)
plt.tight_layout()
plt.show()
