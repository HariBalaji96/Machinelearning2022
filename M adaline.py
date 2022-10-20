f=open("A.txt","r").readlines()
x1=[]
x2=[]
t=[]
for i in f:
    st=i.split(",")
    x1.append(float(st[0]))
    x2.append(float(st[1]))
    t.append(float(st[2]))
d1=[0.05,0.2,0.3]
d2=[0.1,0.2,0.15]
d3=[0.5,0.5,0.5]
a=float(input("Enter the Alpha :"))
for j in range(len(x1)):
    z1=d1[2]+d1[0]*x1[j]+d1[1]*x2[j]
    z2=d2[2]+d2[0]*x1[j]+d2[1]*x2[j]
    if(z1>0):
        zz1=1
    else:
        zz1=0
    if(z2>0):
        zz2=1
    else:
        zz2=0
    y=d3[2]+zz1*d3[0]+zz2*d3[1]
    if(y>0):
        y=1
    else:
        y=-1
    if(t[j]==y):
        print("In DP",j+1)
        print("z1 =",z1,"z2 =",z2)
        print("No Weight Updation...")
    else:
        print("In DP",j+1)
        print("z1 =",z1,"z2 =",z2)
        w11=d1[0]+a*(t[j]-z1)*x1[j]
        w12=d2[0]+a*(t[j]-z2)*x1[j]
        w21=d1[0]+a*(t[j]-z2)*x2[j]
        w22=d2[0]+a*(t[j]-z2)*x2[j]
        print("\nW11=",w11,"\nW12=",w12,"\nW21=",w21,"\nW22=",w22)
  

