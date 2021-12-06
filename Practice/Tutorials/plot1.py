import matplotlib.pyplot as plt
from matplotlib import style

days=['m','t','w','th','f','sat','sun']
workload=[9,8,5,4,4,3,0]
plt.plot(days,workload,'r',linewidth=5)
plt.legend()
plt.xlabel("Days")
plt.ylabel('Workload')
plt.title("MY WEEK")
plt.show()

