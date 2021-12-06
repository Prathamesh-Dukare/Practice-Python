from matplotlib import pyplot as plt
branch=["Computer","Mechanical","IT","Civil","E&TC"]
placed=[110,120,50,40,35]
colo=['r','g','k','b','w']
plt.pie(placed,labels=branch,colors=colo,startangle=90,shadow=True,explode=[0,0.1,0,0,0],autopct='%1.1f%%')
plt.legend()
plt.title('AVCOE PLACEMENTS')             

plt.show()