import matplotlib.pyplot as plt
f=open("P.txt","r").readlines()
x1=[]
x2=[]
t=[]
for i in f:
    st=i.split(",")
    x1.append(float(st[0]))
    x2.append(float(st[1]))
    t.append(float(st[2]))
w0=0
w1=0.5
w2=0.5
for j in range(len(x1)):
    I=w0+w1*x1[j]+w2*x2[j]
    if(I<1):
        y=0
    else:
        y=1
    if(t[j]==y):
        print("In DP",j+1)
        print("No Weight Updation...")
    else:
        w0=w0+0.3*(t[j]-y)*1
        w1=w1+0.3*(t[j]-y)*x1[j]
        w2=w2+0.3*(t[j]-y)*x2[j]
        print("In DP",j+1)
        print("\nW0 = ",w0,"\nW1 = ",w1,"\nW2 = ",w2)
plt.plot(x1)
plt.plot(x2)

        