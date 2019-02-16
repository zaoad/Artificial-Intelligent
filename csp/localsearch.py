import random
import time
import sys
def conflict(x,y,allocation,n):
    count=0
    for i in range(0, n):
        if i==x:
            continue
        if allocation[i][y]==1:
            #print('row')
            count=count+1

    #check upperleft diagonal
    for i in range(1,x+1):
        if y-i<0:
            break
        if allocation[x-i][y-i]==1:
            #print('upperleft')
            count=count+1
    #check lowerleft diagonal
    for i in range(1,x+1):
        if y+i==n:
            break
        if allocation[x-i][y+i]==1:
            #print('lowerleft')
            count=count+1
    #check upperright diagonal
    for i in range(1,n-x):
        if y-i<0:
            break
        if allocation[x+i][y-i]==1:
            #print('upright')
            count=count+1
    #check lowerright diagonal
    for i in range(1,n-x):
        if y+i==n:
            break
        if allocation[x+i][y+i]==1:
            #print('lowright')
            count=count+1
    return count

def conflictedrow(row,allocation,n):
    #print('dok')
    for i in range(0,n):
        #print(row, i)
        m=conflict(row,i,allocation,n)
        if allocation[row][i]==1 & m>0:

            return m
    return 0

def checksatisfaction(allocation,n):
    for i in range(0,n):
        if(conflictedrow(i,allocation,n)>0):
            return False
    return  True

def printboard(allocation,n):
    for i in range(0,n):
        sys.stdout.write('| ')
        sys.stdout.flush()
        for j in range(0,n):
            a=str(allocation[j][i])+" "
            sys.stdout.write(a)
            sys.stdout.flush()
        print('|')
    return

def columnchange(row,y,allocation,n):
    for i in range(0,n):
        allocation[row][i]=0
    allocation[row][y]=1

def localsearch(allocation,maxit,n):
    step=1
    prevrow=-1
    row=0
    for i in range(0,maxit):
        if(checksatisfaction(allocation,n)):
            print('satisfied')
            return (True,step,allocation)
        #print('row ',row)
        row=(row+1)%n
        while(conflictedrow(row,allocation,n)==0):
            #print('doke',row)
            row=(row+1)%n
        #print('row ', row)
        #print('---------------------')
        #print('step '+ str(step))
        step=step+1
        cnt=10000
        ind=0
        row=row%n
        for i in range(0,n):
            tempcnt=conflict(row,i,allocation,n)
            #print('i',i,tempcnt)
            if(tempcnt<cnt):
                ind=i
            if(tempcnt==cnt):
                r=random.randint(0,10000)
                if r%2==1:
                    ind=i
            cnt=min(cnt,tempcnt)
            columnchange(row,ind,allocation,n)
        #printboard(allocation,n)
    return (False,step,allocation)
1
for t in range(10,101,5):
    print('----------------------------------------------------------')
    print('number '+str(t))
    start =time.time()
    maxit = 100000
    n=t
    allocation = [[0 for i in range(n)] for j in range(n)]
    for i in range(0,n):
        r=random.randint(0,n-1)
        #print(r)
        allocation[i][r]=1
    printboard(allocation,n)
    conflictedrow(0,allocation,n)
    answer=localsearch(allocation,maxit,n)
    if(answer[0]):
        printboard(allocation,n)
    else:
        print('max iteration exceed')
    end=time.time()
    print("time",str(end-start)+'ms')
    print('step',answer[1])
    print('------------------------------------------------------')
