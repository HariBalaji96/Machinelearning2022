f=open("A.txt","r").readlines()
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
a=float(input("Enter the Alpha :"))
error=0
for j in range(len(x1)):
    I=w0+w1*x1[j]+w2*x2[j]
    print("In DP",j+1)
    if(I<1):
        print("\ny=",0)
    else:
        print("\ny=",1)
    if(t[j]-I==0):
        print("No Weight Updation...")
    else:
        w0=w0+a*(t[j]-I)*1
        w1=w1+a*(t[j]-I)*x1[j]
        w2=w2+a*(t[j]-I)*x2[j]
        print("\nW0 = ",w0,"\nW1 = ",w1,"\nW2 = ",w2)
    error=error+(t[j]-I)*(t[j]-I)
print("Error=",error)