import numpy as np
users=4
rb=8
rates=np.random.randint(1,10,users)
alloc=np.zeros(users,dtype=int)
for r in range(rb):
    u=np.argmin(alloc)
    alloc[u]+=1
print("User Rates:",rates)
print("RB Allocation:",alloc)
print("Fairness Index:",round(sum(alloc)**2/(users*sum(alloc**2)),3))
