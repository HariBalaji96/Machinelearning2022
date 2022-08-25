import matplotlib.pyplot as plt
f=open("Poly Data.txt","r")
lines=f.readlines()
indep=[]
dep=[]
for line in lines:
    st=line.split(",")
    indep.append(float(st[0]))
    dep.append(float(st[1]))
print(indep)      
print(dep)
n=len(dep)
sumxt=sum(indep)
sumxtsq=0
sumxtcub=0
sumxtp4=0
I=sum(dep)
II=0
III=0
for i in range(0,n):
    sumxtsq=sumxtsq+indep[i]*indep[i]
    sumxtcub=sumxtcub+indep[i]*indep[i]*indep[i]
    sumxtp4=sumxtp4+indep[i]*indep[i]*indep[i]*indep[i]
    II=II+indep[i]*dep[i]
    III=III+indep[i]*dep[i]*indep[i]
ni=int(input("Enter the Number of iteration:"))
w0=0
w1=0
w2=0
for j in range(1,ni+1):
    w0=(I-n*w1-sumxtsq*w2)/n
    w1=(II-sumxt*w0-sumxtcub*w2)/sumxtsq
    w2=(III-sumxtsq*w0-sumxtcub*w1)/sumxtp4
    print("\nIn Iteration",j,":\nW0=",w0,"\nW1=",w1,"\nW2=",w2)
G=[]
for k in range(0,len(dep)):
    G.append(w0+indep[k]*w1+indep[k]*indep[k]*w2)
    print("G(",int(indep[k]),")=",w0+indep[k]*w1+indep[k]*indep[k]*w2)

plt.plot(indep, G,marker='o', markerfacecolor='red', markersize=5)
plt.show(indep,G)


    