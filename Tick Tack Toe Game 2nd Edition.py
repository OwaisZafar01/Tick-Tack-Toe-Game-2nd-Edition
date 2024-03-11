#Tick Tack Toe Game

#TAKE INPUT FROM USER AND CHECK WHO WIN 

g1=input("Enter values:")
g2=input("Enter values:")
g3=input("Enter values:")
k=[]
l=[]
m=[]
n=[]
g1=g1.split()
for i in g1:
    a=int(i)
    k.append(a)
    
l.append(k)

g2=g2.split()
for j in g2:
    b=int(j)
    m.append(b)

l.append(m)

g3=g3.split()
for k in g3:
    c=int(k)
    n.append(c)

l.append(n)

if l[0][0]==l[0][1]==l[0][2]:
    print("PLAYER",l[0][0],"won")

elif l[1][0]==l[1][1]==l[1][2]:
    print("PLAYER",l[1][0],"won")

elif l[2][0]==l[2][1]==l[2][2]:
    print("PLAYER",l[2][0],"won")

elif l[0][0]==l[1][0]==l[2][0]:
    print("PLAYER",l[0][0],"won")

elif l[0][1]==l[1][1]==l[2][1]:
    print("PLAYER",l[0][1],"won")

elif l[0][2]==l[1][2]==l[2][2]:
    print("PLAYER",l[0][2],"won")

elif l[0][0]==l[1][1]==l[2][2]:
    print("PLAYER",l[0][0],"won")

elif l[2][0]==l[1][1]==l[0][0]:
    print("PLAYER",l[2][0],"won")

else:
    print("GAME DRAW")