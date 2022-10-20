file1 = open('Naive', 'r')
q=[]
temp = file1.readline().split(" ")
for i in range(len(temp)-1):
    val=input("Enter query value for data x:")
    q.append(val)
print("************************************************************************")
Lines = file1.readlines()
list1=[]
count=0
yes=0
no=0
q1=0
q2=0
q3=0
q4=0
file1 = open('Naive', 'r')
Lines=file1.readlines()
for line in Lines:
    x=line.split(" ")
    count=count+1
    list1.append(x[-1])
res = [*set(list1)]
for line in Lines:
    x=line.split(" ")
    if x[4]=="yes\n":
        yes=yes+1
    else:
        no=no+1
pyes=0
pno=0
pc1=0
pc2=0
pyes=yes/count 
pno=no/count 
print("Probability of yes:",round(pyes,3))
print("Probability of no:",round(pno,3))
print("************************************************************************")
for line in Lines:
    x=line.split(" ")
    if x[4]=="yes\n":
        if q[0]==x[0]:
            q1=q1+1
        if q[1]==x[1]:
            q2=q2+1
        if q[2]==x[2]:
            q3=q3+1
        if q[3]==x[3]:
            q4=q4+1
pc1=round((q1/yes)*(q2/yes)*(q3/yes)*(q4/yes),3)
pc1=round(pc1*pyes,3)
print("\nProbability of class1:",pc1)
q1=0
q2=0
q3=0
q4=0
for line in Lines:
    x=line.split(" ")
    if x[4]=="no\n":
        if q[0]==x[0]:
            q1=q1+1
        if q[1]==x[1]:
            q2=q2+1
        if q[2]==x[2]:
            q3=q3+1
        if q[3]==x[3]:
            q4=q4+1
pc2=round((q1/no)*(q2/no)*(q3/no)*(q4/no),3)
pc2=round(pc2*pno,3)
print("Probability for Class2:",pc2)
if pc1>pc2:
    print("\n\n\n\n\nYes he buys a computer")
else:
    print("\n\n\n\n\nNo he not buys a computer")
