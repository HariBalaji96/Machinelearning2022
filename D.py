import math as m
file=open("Decision.txt","r").read()
age=[]
income=[]
student=[]
credit=[]
buy=[]
f=file.split("\n")
data=[]
for i in f:
    data.append(i.split(","))
for i in f:
    st=i.split(",")
    age.append(st[0])
    income.append(st[1])
    student.append(st[2])
    credit.append(st[3])
    buy.append(st[4])
C1=buy.count("yes") 
C2=buy.count("no")
T=len(buy)
Y=age.count("youth")
M=age.count("midaged")
S=age.count("senior")
YC1=0
YC2=0
MC1=0
MC2=0
SC1=0
SC2=0
Ibuy=-1*((C1/T)*m.log2(C1/T)+(C2/T)*m.log2(C2/T))
for i in range(T):
    if(data[i][0]=="youth" and data[i][4]=="yes"):
        YC1+=1
    if(data[i][0]=="youth" and data[i][4]=="no"):
        YC2+=1
    if(data[i][0]=="midaged" and data[i][4]=="yes"):
        MC1+=1
    if(data[i][0]=="midaged" and data[i][4]=="no"):
        MC2+=1
    if(data[i][0]=="senior" and data[i][4]=="yes"):
        SC1+=1
    if(data[i][0]=="senior" and data[i][4]=="no"):
        SC2+=1
YC1=YC1/Y
YC2=YC2/Y
MC1=MC1/M
MC2=MC2/M
try:
    exp=MC2*m.log2(MC2)
except ValueError:
    exp=0
SC1=SC1/S
SC2=SC2/S
Iage=(Y/T)*(-YC1*m.log2(YC1)-YC2*m.log2(YC2))+(M/T)*(-MC1*m.log2(MC1)-exp)+(S/T)*(-1*SC1*m.log2(SC1)-SC2*m.log2(SC2))
H=income.count("high")
ME=income.count("medium")
L=income.count("low")
HC1=0
HC2=0
MEC1=0
MEC2=0
LC1=0
LC2=0
for i in range(T):
    if(data[i][1]=="high" and data[i][4]=="yes"):
        HC1+=1
    if(data[i][1]=="high" and data[i][4]=="no"):
        HC2+=1
    if(data[i][1]=="medium" and data[i][4]=="yes"):
        MEC1+=1
    if(data[i][1]=="medium" and data[i][4]=="no"):
        MEC2+=1
    if(data[i][1]=="low" and data[i][4]=="yes"):
        LC1+=1
    if(data[i][1]=="low" and data[i][4]=="no"):
        LC2+=1
HC1=HC1/H
HC2=HC2/H
MEC1=MEC1/ME
MEC2=MEC2/ME
LC1=LC1/L
LC2=LC2/L
Iincome=(H/T)*(-HC1*m.log2(HC1)-HC2*m.log2(HC2))+(ME/T)*(-MEC1*m.log2(MEC1)-MEC2*m.log2(MEC2))+(L/T)*(-1*LC1*m.log2(LC1)-LC2*m.log2(LC2))
YS=student.count("yes")
N=student.count("no")
YSC1=0
YSC2=0
NC1=0
NC2=0
for i in range(T):
    if(data[i][2]=="yes" and data[i][4]=="yes"):
        YSC1+=1
    if(data[i][2]=="yes" and data[i][4]=="no"):
        YSC2+=1
    if(data[i][2]=="no" and data[i][4]=="yes"):
        NC1+=1
    if(data[i][2]=="no" and data[i][4]=="no"):
        NC2+=1
YSC1=YSC1/YS
YSC2=YSC2/YS
NC1=NC1/N
NC2=NC2/N

def Idata(A,A1,A2,A3,A4,A5):
    return((A/T)*(-A1*m.log2(A1)-A2*m.log2(A2))+(A3/T)*(-A4*m.log2(A4)-A5*m.log2(A5)))
Istudent=Idata(YS,YSC1,YSC2,N,NC1,NC2)


F=credit.count("fair")
E=credit.count("excellent")
FC1=0
FC2=0
EC1=0
EC2=0
for i in range(T):
    if(data[i][3]=="fair" and data[i][4]=="yes"):
        FC1+=1
    if(data[i][3]=="fair" and data[i][4]=="no"):
        FC2+=1
    if(data[i][3]=="excellent" and data[i][4]=="yes"):
        EC1+=1
    if(data[i][3]=="excellent" and data[i][4]=="no"):
        EC2+=1
FC1=FC1/F
FC2=FC2/F
EC1=EC1/E
EC2=EC2/E
Icerdit=Idata(F,FC1,FC2,E,EC1,EC2)
print("Info(age) : ",Iage)
print("Info(Income) : ",Iincome)
print("Info(student) : ",Istudent)
print("Info(cerdit) : ",Icerdit)

print("\nGain(age) : ",Ibuy-Iage)
print("Gain(Income) : ",Ibuy-Iincome)
print("Gain(student) : ",Ibuy-Istudent)
print("Gain(cerdit) : ",Ibuy-Icerdit)

def Sdata(Y1,Y2,Y3):
    return((-Y1/T)*m.log2(Y1/T)+(-Y2/T)*m.log2(Y2/T)+(-Y3/T)*m.log2(Y3/T))

def Sdata1(S1,S2):
    return((-S1/T)*m.log2(S1/T)+(S2/T)*m.log2(S2/T))


print("\nSplit_Info(age) : ",Sdata(Y, M, S))
print("Split_Info(income) : ",Sdata(H, ME, L))
print("Split_Info(student) : ",Sdata1(YS, N))
print("Split_Info(cerdit) : ",Sdata1(F, E))
