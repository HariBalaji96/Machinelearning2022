import matplotlib.pyplot as plt
f=open("linear data.txt","r")
lines=f.readlines()
indep=[]
dep=[]
for line in lines:
    st=line.split(",")
    indep.append(float(st[0]))
    dep.append(float(st[1]))
dep=0

print(indep)    
print(dep)
xrsum=0
x2sum=0 
w1=0 
xmean=sum(indep)/len(indep)
rmean=sum(dep)/len(dep)
for i in range(0,len(dep)):
    xrsum=xrsum+dep[i]*indep[i]
    x2sum=x2sum+indep[i]*indep[i]
w1=(xrsum-(len(dep)*xmean*rmean))/(x2sum-(len(dep)*xmean*xmean))
print(w1)
w0=rmean-w1*xmean
print(w0)
G=[]
for x in range(1,len(dep)+1):
    print("G(",x,")=",w1*x+w0)
    G.append(float(w1*x+w0))
plt.plot(indep, G,marker='o', markerfacecolor='red', markersize=5)
plt.show(indep,G)
user=int(input("Enter the Values:"))
print("G(",user,")=",w1*user+w0)
fs=open("linear store.txt","a")
for s in range(0,len(dep)):
    fs.write(str(G[s]))
