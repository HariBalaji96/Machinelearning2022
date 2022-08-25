import math
f=open("Logistic Data.txt","r")
lines=f.readlines()
x1=[]
x2=[]
x3=[]
y=[]
for line in lines:
    st=line.split(",")
    x1.append(float(st[0]))
    x2.append(float(st[1]))
    x3.append(float(st[2]))
    y.append(int(st[3]))
print("X1=",x1)
print("X2=",x2)
print("X3=",x3)
print("Y=",y)
n=len(x1)
print("N=",n)
w0=0
w1=0
w2=0
w3=0
p=[]
for i in range(0,n):
    output=-1*(w0+w1*x1[i]+w2*x2[i]+w3*x3[i])
    p=1/(1+math.exp(output))
    print("==========In DP",i+1,"==========")
    w0=w0+0.3*(y[i]-p)*p*(1-p)*1
    w1=w1+0.3*(y[i]-p)*p*(1-p)*x1[i]
    w2=w2+0.3*(y[i]-p)*p*(1-p)*x2[i]
    w3=w3+0.3*(y[i]-p)*p*(1-p)*x3[i]
    print("\nW0=",w0,"\nW1=",w1,"\nW2=",w2,"\nW3=",w3)
    if p>=0.5:
        print("Class 1")
    else:
        print("Class 0")