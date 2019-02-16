import sys
def NQueen(allocation, row, n):
    if row == n:
        return (True, allocation)
    for i in range(0, n):
        allocation[row][i] = 1
        if(checkpositionvalidity(row, i, allocation, n)):
            result=NQueen(allocation, row+1, n)
            if result[0]==True:
                return result
        allocation[row][i]=0
    return (False,allocation)

def checkpositionvalidity(x,y,allocation,n):
    #check row
    for i in range(0, x):
        if allocation[i][y]==1:
            return False
    #check upper diagonal
    for i in range(1,x+1):
        if y-i<0:
            break
        if allocation[x-i][y-i]==1:
            return False
    #check lower diagonal
    for i in range(1,x+1):
        if y+i==n:
            break
        if allocation[x-i][y+i]==1:
            return False
    return True
n=input()
allo = [[0 for i in range(n)] for j in range(n)]
for i in range(0,n):
    for j in range(0,n):
        allo[i][j]=0

result=NQueen(allo, 0, n)
if result[0]==False:
    print("solution doesn't exist")
    exit()
allocation=result[1]
for i in range(0, n):
        print(allocation[i])

