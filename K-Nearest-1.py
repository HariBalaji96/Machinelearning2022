import math as m
f=open("K-Nearest Data 1.txt","r").read()
print("=======================Program Real Class=======================")
lines=f.split("\n")
DP1=lines[0].split(",")
DP2=lines[1].split(",")
DP3=lines[2].split(",")
DP4=lines[3].split(",")
DP5=lines[4].split(",")
Q=lines[5].split(",")
print("=======================DP=======================")
print("DP1:",DP1)
print("DP2:",DP2)
print("DP3:",DP3)
print("DP4:",DP4)
print("DP5:",DP5)
print("Q:",Q)
DP1Q=m.sqrt(m.pow(float(DP1[0])-float(Q[0]),2)+m.pow(float(DP1[1])-float(Q[1]),2)+m.pow(float(DP1[2])-float(Q[2]),2)+m.pow(float(DP1[3])-float(Q[3]),2))
DP2Q=m.sqrt(m.pow(float(DP2[0])-float(Q[0]),2)+m.pow(float(DP2[1])-float(Q[1]),2)+m.pow(float(DP2[2])-float(Q[2]),2)+m.pow(float(DP2[3])-float(Q[3]),2))
DP3Q=m.sqrt(m.pow(float(DP3[0])-float(Q[0]),2)+m.pow(float(DP3[1])-float(Q[1]),2)+m.pow(float(DP3[2])-float(Q[2]),2)+m.pow(float(DP3[3])-float(Q[3]),2))
DP4Q=m.sqrt(m.pow(float(DP4[0])-float(Q[0]),2)+m.pow(float(DP4[1])-float(Q[1]),2)+m.pow(float(DP4[2])-float(Q[2]),2)+m.pow(float(DP4[3])-float(Q[3]),2))
DP5Q=m.sqrt(m.pow(float(DP5[0])-float(Q[0]),2)+m.pow(float(DP5[1])-float(Q[1]),2)+m.pow(float(DP5[2])-float(Q[2]),2)+m.pow(float(DP5[3])-float(Q[3]),2))
print("=======================Distances=======================")
print("d(DP1,Q) = ",DP1Q)
print("d(DP2,Q) = ",DP2Q)
print("d(DP3,Q) = ",DP3Q)
print("d(DP4,Q) = ",DP4Q)
print("d(DP5,Q) = ",DP5Q)
DP=[DP1Q,DP2Q,DP3Q,DP4Q,DP5Q]
K=[]
C=[]
for i in range(3):
    temp=min(DP)
    K.append(temp)
    DP.remove(temp)
print(K)
for j in K:
    if(j==DP1Q):
        C.append(0.6)
    elif(j==DP2Q):
        C.append(0.9)
    elif(j==DP3Q):
            C.append(0.33)
    elif(j==DP4Q):
        C.append(0.4)
    elif(j==DP5Q):
        C.append(0.7)
print(C)
print("It Belongs to Class :",sum(C)/3)
