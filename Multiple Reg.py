import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
f=open("Multiple Data.txt","r")
lines=f.readlines()
indep1=[]
indep2=[]
dep=[]
for line in lines:
    st=line.split(",")
    indep1.append(float(st[0]))
    indep2.append(float(st[1]))
    dep.append(float(st[2]))
print(indep1)    
print(indep2)    
print(dep)
n=len(dep)
sumx1t=sum(indep1)
sumx2t=sum(indep2)
sumx1tsq=0
sumx2tsq=0
sumx1x2t=0
I=sum(dep)
II=0
III=0
for i in range(0,n):
    sumx1tsq=sumx1tsq+indep1[i]*indep1[i]
    sumx2tsq=sumx2tsq+indep2[i]*indep2[i]
    sumx1x2t=sumx1x2t+indep1[i]*indep2[i]
    II=II+indep1[i]*dep[i]
    III=III+indep2[i]*dep[i]
ni=int(input("Enter the Number of iteration:"))
w0=0
w1=0
w2=0
for j in range(1,ni+1):
    w0=(I-n*w1-sumx2t*w2)/n
    w1=(II-sumx1t*w0-sumx1x2t*w2)/sumx1tsq
    w2=(III-sumx2t*w0-sumx1x2t*w1)/sumx2tsq
    print("\nIn Iteration",j,":\nW0=",w0,"\nW1=",w1,"\nW2=",w2)
print("\n *******************Equations***************************")
G=[]
for k in range(0,len(dep)):
    G.append(w0+indep1[k]*w1+indep2[k]*w2)
    print("G(",int(indep1[k]),",",int(indep2[k]),")=",w0+indep1[k]*w1+indep2[k]*w2)
fig = plt.figure(figsize=(4,4))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(indep1,indep2,G)
plt.show()


    