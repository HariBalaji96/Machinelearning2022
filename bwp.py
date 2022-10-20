import numpy as ny
import math as mt
print("Backward Propagation....")
f=open("back.txt","r").readlines()
I1=[]
I2=[]
O=[]
for i in f :
    st=i.split(" ")
    I1.append(float(st[0]))
    I2.append(float(st[1]))
    O.append(float(st[2]))              # Here Step:1
l=int(input("Enter the Value of l :"))
m=int(input("Enter the Value of m :"))
n=int(input("Enter the Value of n :"))
r=2*l
if(m<l or m>r):                         # Here Step:2
    print("Your Entered a Wrong Value for 'm' Please Verify.....")
a=float(input("Enter the Value of Alpha :"))
b=float(input("Enter the Value of Beta :"))
W0=[[0.2],[-0.5]]
DW=[[0.0],[0.0]]
V0=[[0.1,0.4],[-0.2,0.2]]
DV=[[0.0,0.0],[0.0,0.0]]                # Here Step:3
for i in range(len(I1)):
    OI=[]
    print("For ",I1[i]," ",I2[i])
    OI=[[I1[i]],[I2[i]]]                    # Here Step:4 and Step:17
    VT=ny.transpose(V0)
    IH=ny.dot(VT,OI)                    # Here Step:5
    OH=[[1/(1+mt.exp(-1*IH[0]))],[1/(1+mt.exp(-1*IH[1]))]]    # Here Step:6
    WT=ny.transpose(W0)
    IO=ny.dot(WT,OH)
    OO=1/(1+mt.exp(-1*IO))              # Here Step:8
    error=mt.sqrt((O[i]-OO)**2/n)       # Here Step:9
    D=(O[i]-OO)*OO*(1-OO)              # Here Step:10
    Y=ny.dot(OH,D)                     # Here Step:11   
    DW1=ny.add(ny.dot(a, DW),ny.dot(b, Y))  # Here Step:12
    E=ny.dot(W0,D)
    D=[[E[0][0]*OH[0][0]*(1-OH[0][0]),E[1][0]*OH[1][0]*(1-OH[1][0])]]   # Here Step:13
    X=ny.dot(OI,D)                          
    DV=ny.dot(a,ny.transpose(DV))+ny.dot(b,X)
    VT=VT+DV                            # Here Step:14
    WT=WT+ny.transpose(DW)              # Here Step:15
    error_rate=error/5                  # Here Step:16
    print("Error Rate : ",error_rate)

    
    
    
    
    
    
    
    
