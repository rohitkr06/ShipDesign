import pygame
import random
import project
import copy
pygame.init()
run=True

cabup=[]
cabdown=[]
#DECLARING DATA ####
fn = []
ff = []
nf = []
#data= []
area = 0

numgen = 90
joker=numgen
x = 0
y = 0
z = 0
x1 = 0
y1 = 0
z1 = 0
m = 0
n = 0

bestfit1=100000
bestfit2=100000
bestfit3=100000

bestop1 = []
bestop2 = []    
bestop3 = []

####BASIC INPUT OUTPUT CONSOLE ####

print("\n\n######## Welcome to Layput Optimization Console ########" " \n")
print("\n Please select ventilation type based on the following:")
print("\n\tVentilation Type:" "\n" "\nFORCED IN NATURAL OUT = 'FN'" "\n" "FORCED IN FORCED OUT  = 'FF'")
print("NATURAL IN FORCED OUT = 'NF'")

loca = input("\nEnter the location of layout(A: Ahead Midship; B: Behind Midship.) : ")
L = int(input("\n Enter the length of Layout Area(m) : "))
B = int(input("Enter the breadth of Layout area(m) : "))

cabins = int(input("Enter the number of compartments : "))


for i in range (cabins):
    type = input("\n Please enter the Ventilation type of the Cabin :")

    if type == 'FN' or type == 'fn':
        cn1 = input("Enter the Cabin Name : ")
        ppl1 = int(input("Enter No of Occupants :"))
        min1 = int(input("Enter the Min area required(sq. m) :"))
        fn.append([cn1,ppl1,min1])
        area = area+min1

    if type == 'FF' or type == 'ff':
        cn2 = input("Enter the Cabin Name : ")
        ppl2 = int(input("Enter No of Occupants :"))
        min2 = int(input("Enter the Min area required(sq. m) :"))
        ff.append([cn2,ppl2,min2])
        area = area+min2

    if type == 'NF' or type == 'nf':
        cn3 = input("Enter the Cabin Name : ")
        ppl3 = int(input("Enter No of Occupants :"))
        min3 = int(input("Enter the Min area required(sq. m) :"))
        nf.append([cn3,ppl3,min3])
        area = area+min3

#data.append([fn,ff,nf])


#### Passage Area Calculation ####

if L <= 15:
    pass_area = 1.6*L

if L > 15 and L<=25:
    pass_area = 1.6*L + (B-1.6)*1.6

if L > 25:
    pass_area = 1.6*L + 2*1.6*(B-1.6)

print("\nGross area of Layout(sq. m) : ", L*B)
print("\nRequired Passage Area(sq. m): ", pass_area)
print("\nNet Area available for compartments(sq. m) : ", L*B - pass_area )
print("\nMin area required by all cabins(sq. m) : ", area)


#### Passage Area Check ####

if area > (L*B - pass_area):
    print("\n Min area required by all cabins exceed the available net area. Please do changes.")


#### CO-ORDINATES AND AREA GENERATION CODE ####
    
length= L
breadth= B

au=[]
al=[]

pos=round((breadth/2 - 0.8)/2,2)
y=breadth/2-0.8

if cabins%2==0:
    up=int(cabins/2)
    lower=int(cabins/2)
else:
    up=int(cabins/2 +1)
    lower=int(cabins/2)
    
#CASE 1
if length<=15:
    newx=round(length/(2*up),2)
    
    
    #Area
    area=y*length
    
    uparea=round(area/up,2)
    downarea=round(area/lower,2)

    au.append((newx,pos,uparea))
    
    for i in range(up-1):
        au.append((round(newx+length/up,2),pos,uparea))
        newx=newx+length/up

    newlx=length/(2*lower)

    al.append((newlx,-pos,downarea))

    for i in range(lower-1):
        al.append((round(newlx + length/lower,2),-pos,downarea))
        newlx=newlx + length/lower

#CASE 2
elif length>15 and length<=25:
    if up%2==0:
        c1=c2=int(up/2)
    else:
        c1=int(up/2+1)
        c2=int(up/2)

    if lower%2==0:
        c3=c4=int(lower/2)
    else:
        c3=int(lower/2 +1)
        c4=int(lower/2)

        
    newl=length/2-0.8

    #Area

    area=y*newl

    areac1=round(area/c1,2)
    areac2=round(area/c2,2)
    areac3=round(area/c3,2)
    areac4=round(area/c4,2)

    newx=round(newl/(2*c1),2)
    au.append((newx,pos,areac1))

    for i in range(c1-1):
        au.append((round(newx+newl/c1,2),pos,areac1))
        newx=round(newx+newl/c1,2)

    newxr=round(newl + 1.6 + newl/(2*c2) ,2)    
    au.append((newxr,pos,areac2))

    for i in range(c2-1):
        au.append((round(newxr + newl/c2,2),pos,areac2))
        newxr=round(newxr + newl/c2 ,2)

    newxd=round(newl/(2*c3),2)
    al.append((newxd,-pos,areac3))
    for i in range(c3-1):
        al.append((round(newxd+newl/c3,2),-pos,areac3))
        newxd=round(newxd+newl/c3 ,2)

    newxd=round(newl + 1.6 + newl/(2*c4),2)    
    al.append((newxd,-pos,areac4))

    for i in range(c4-1):
        al.append((round(newxd + newl/c4,2),-pos,areac4))
        newxd=round(newxd + newl/c4 , 2)

        
     #CASE 3   
else:

    if up%3==0:
        c1=c2=c3=int(up/3)
    else:
        rem=up%3
        c1=int(up/3 + rem)
        c2=int(up/3)
        c3=int(up/3)
        
    if lower%3==0:
        c4=c5=c6=int(lower/3)
    else:
        rem=lower%3
        c4=int(lower/3 + rem)
        c5=int(lower/3)
        c6=int(lower/3)
    
    
    newl=length/3 - 0.8

    #Area
    area=y*newl

    areac1=round(area/c1,2)
    areac2=round(area/c2,2)
    areac3=round(area/c3,2)
    areac4=round(area/c4,2)
    areac5=round(area/c5,2)
    areac6=round(area/c6,2)
    

    #UPPER
    newx=round(newl/(2*c1),2)
    au.append((newx,pos,areac1))

    for i in range(c1-1):
        au.append((round(newx+newl/c1,2),pos,areac1))
        newx=newx+newl/c1

    newx2=round(newl+1.6+newl/(2*c2),2)
    au.append((newx2,pos,areac2))

    for i in range(c2-1):
        au.append((round(newx2+newl/c2,2),pos,areac2))
        newx2=newx2+newl/c2

    newx3=round(2*newl+3.2+newl/(2*c3),2)
    au.append((newx3,pos,areac3))

    for i in range(c3-1):
        au.append((round(newx3+newl/c3,2),pos,areac3))
        newx3=newx3+newl/2*c3

    #LOWER
    newx=round(newl/(2*c4),2)
    al.append((newx,-pos,areac4))

    for i in range(c4-1):
        al.append((round(newx+newl/c4,2),-pos,areac4))
        newx=newx+newl/c4

    newx2=round(newl+1.6+newl/(2*c5),2)
    al.append((newx2,-pos,areac5))

    for i in range(c5-1):
        al.append((round(newx2+newl/c5,2),-pos,areac5))
        newx2=newx2+newl/c5

    newx3=round(2*newl+3.2+newl/(2*c6),2)
    al.append((newx3,-pos,areac6))

    for i in range(c6-1):
        al.append((round(newx3+newl/c6,2),-pos,areac6))
        newx3=newx3+newl/2*c6    

        

cabs=[]

cabs.append((au,al))

print("\n",cabs)


#### GENETIC ALGORITHM ####
parent1=[]
parent2=[]


def parent(parent1,parent2):

    if numgen<=joker/3:
        parent1.clear()
        parent2.clear()
        parent1.append([fn,ff,nf])
        parent2.append([fn,nf,ff])

    if numgen>(joker/3) and numgen<=(2*joker/3):
        parent1.clear()
        parent2.clear()
        parent1.append([nf,fn,ff])
        parent2.append([nf,ff,fn])

    if numgen>(2*joker/3):
        parent1.clear()
        parent2.clear()
        parent1.append([ff,fn,nf])
        parent2.append([ff,nf,fn])
    return parent1,parent2
    

def mutation():
    #print("\n in mutation random i and j :")
    L1 = len(fn)
    if L1>=1:
        i = random.randint(0,L1-1)
        j = random.randint(0,L1-1)
        fn[i],fn[j]=fn[j],fn[i]
        #print("for FN array i and j ", i,j)
    L2 = len(ff)
    if L2>=1:
        i = random.randint(0,L2-1)
        j = random.randint(0,L2-1)
        ff[i],ff[j]=ff[j],ff[i]
        #print("for FF array i and j ", i,j)
    L3 = len(nf)
    if L3>=1:
        i = random.randint(0,L3-1)
        j = random.randint(0,L3-1)
        nf[i],nf[j]=nf[j],nf[i]
        #print("for nf array i and j ", i,j)

def fitness(bestfit1,bestfit2,bestfit3,bestop1,bestop2,bestop3):

    sum1 = 0
    sum2 = 0
    x=len(parent1[0][0])
    y=len(parent1[0][1])
    z=len(parent1[0][2])

    x1=len(parent2[0][0])
    y1=len(parent2[0][1])
    z1=len(parent2[0][2])

    m=len(au)
    n=len(al)

    for i in range(cabins):
        if(i+1<=x):
            a1=parent1[0][0][i][1]
        elif(i+1>x and i+1-x<=y):
            a1=parent1[0][1][i-x][1]
        else:
            a1=parent1[0][2][i-x-y][1]
        if(i+1<=m):
            a2=cabs[0][0][i][0]
        else:
            a2=cabs[0][1][i-m][0]

        #print("for parent1 a1 and a2 are : ",a1,a2)
        sum1=sum1+a1*a2
        
    for ij in range(cabins):
        if(ij+1<=x1):
            b1=parent2[0][0][ij][1]
        elif(ij+1>x1 and ij+1-x1<=y1):
            b1=parent2[0][1][ij-x1][1]
        else:
            b1=parent2[0][2][ij-x1-y1][1]

        if(ij+1<=m):
            b2=cabs[0][0][ij][0]
        else:
            b2=cabs[0][1][ij-m][0]

        #print("for parent2 b1 and b2 are : ",b1,b2)
        sum2=sum2+b1*b2
        
    if sum1< bestfit1:
        bestfit3 = bestfit2
        bestop3[:] = bestop2
        
        bestfit2 = bestfit1
        bestop2[:] = bestop1

        bestfit1 = sum1
        bestop1[:] = copy.deepcopy(parent1)
        
        
    if sum1>bestfit1 and sum1<bestfit2:
        bestfit3 = bestfit2
        bestop3[:] = bestop2
        
        bestfit2 = sum1
        bestop2[:] = copy.deepcopy(parent1)
        
        
    if sum1>bestfit2 and sum1<bestfit3:
        bestfit3 = sum1
        bestop3[:] = copy.deepcopy(parent1)
        

    if sum2< bestfit1:
        bestfit3 = bestfit2
        bestop3[:] = bestop2
        
        bestfit2 = bestfit1
        bestop2[:] = bestop1
        
        bestfit1 = sum2
        bestop1[:] = copy.deepcopy(parent2)
        
        
    if sum2>bestfit1 and sum2<bestfit2:
        bestfit3 = bestfit2
        bestop3[:] = bestop2
        
        bestfit2 = sum2
        bestop2[:] = copy.deepcopy(parent2)
        

    if sum2>bestfit2 and sum2<bestfit3:
        bestfit3 = sum2
        bestop3[:] = copy.deepcopy(parent2)

        

    return bestfit1,bestfit2,bestfit3,bestop1,bestop2,bestop3
    
while(numgen):
    parent1,parent2 = parent(parent1,parent2)
    mutation()
    bestfit1,bestfit2,bestfit3,bestop1,bestop2,bestop3=fitness(bestfit1,bestfit2,bestfit3,bestop1,bestop2,bestop3)
    
    if numgen==1:
        print("Generation : ",91-numgen)
        print("Best 1:",bestfit1, bestop1,"\nBest 2:",bestfit2, bestop2,"\nBest 3:",bestfit3, bestop3)
    
    numgen = numgen-1
    
"""
print("\nbest fit 3 = ", bestfit3)
print("best op 3 = ", bestop3)

print("\nbest fit 2 = ", bestfit2)
print("best op 2 = ", bestop2)

print("\nbest fit 1 = ", bestfit1)
print("best op 1 = ", bestop1)
"""
bol=[]
both1=[]

for i in range(0,len(bestop1[0][0])):
    both1.append(bestop1[0][0][i])  
for i in range(0,len(bestop1[0][1])):
    both1.append(bestop1[0][1][i])
for i in range(0, len(bestop1[0][2])):
    both1.append(bestop1[0][2][i])
bol.append(both1)

both2=[]

for i in range(0,len(bestop2[0][0])):
    both2.append(bestop2[0][0][i])  
for i in range(0,len(bestop2[0][1])):
    both2.append(bestop2[0][1][i])
for i in range(0, len(bestop2[0][2])):
    both2.append(bestop2[0][2][i])
bol.append(both2)    

both3=[]

for i in range(0,len(bestop3[0][0])):
    both3.append(bestop3[0][0][i])  
for i in range(0,len(bestop3[0][1])):
    both3.append(bestop3[0][1][i])
for i in range(0, len(bestop3[0][2])):
    both3.append(bestop3[0][2][i])
bol.append(both3) 
'''
if len(bol[0])%2==0:
    for i in range(0,int(len(bol[0])/2)):
        cabup.append(bol[0][i])
    for j in range(i+1,len(bol[0])):
        cabdown.append(bol[0][j])
else:
    for i in range(0,int(len(bol[0])/2)+1):
        cabup.append(bol[0][i])
    for j in range(i+1,len(bol[0])):
        cabdown.append(bol[0][j])

for i in bol[0]:
    i[0],i[1]=i[1],i[0]
'''    
#print(both)    
project.main(L,B,loca,cabins,bol)
    





               


