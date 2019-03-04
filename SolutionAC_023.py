from fractions import gcd
import math
import copy
import Queue
import random
import time
import matplotlib.pyplot as plot

def isPrime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True

def constraint1(xi, xj):
    return xj > xi


def constraint2(xi, xj):
    return gcd(xj, xi) == 1

def constraint3(xi, xj):
    return xj > xi+10


def constraint4(xi, xj):
    return xj % xi == 0


def constraint5(xi, xj):
    return xj % xi != 0

def constraint6(xi,xj):
    return xj==xi*xi

def change_domain_constraint(domain_xi,domain_xj,constraint):
    flag = True
    temp_domain_xi=copy.deepcopy(domain_xi)
    temp_domain_xj=copy.deepcopy(domain_xj)
    temp_temp_domain_xi = copy.deepcopy(temp_domain_xi)
    temp_temp_domain_xj = copy.deepcopy(temp_domain_xj)

    for x in temp_temp_domain_xi:
        flag = True
        for y in temp_temp_domain_xj:
            if constraint(x,y):
                flag=False
                break
        if flag:
            temp_domain_xi.remove(x)

    flag=True
    for y in temp_temp_domain_xj:
        flag=True
        for x in temp_temp_domain_xi:
            if constraint(x,y):
                flag=False
                break
        if flag:
            temp_domain_xj.remove(y)

    return temp_domain_xi, temp_domain_xj


def change_domain_constraint_xi(domain_xi,domain_xj,constraint):
    flag = True
    temp_domain_xi = copy.deepcopy(domain_xi)
    temp_domain_xj = copy.deepcopy(domain_xj)
    temp_temp_domain_xi = copy.deepcopy(temp_domain_xi)
    temp_temp_domain_xj = copy.deepcopy(temp_domain_xj)

    for x in temp_temp_domain_xi:
        flag = True
        for y in temp_temp_domain_xj:
            if constraint(x, y):
                flag = False
        if flag:
            temp_domain_xi.remove(x)
    return temp_domain_xi


def change_domain_constraint_xj(domain_xi,domain_xj,constraint):
    flag = True
    temp_domain_xi = copy.deepcopy(domain_xi)
    temp_domain_xj = copy.deepcopy(domain_xj)
    temp_temp_domain_xi = copy.deepcopy(temp_domain_xi)
    temp_temp_domain_xj = copy.deepcopy(temp_domain_xj)
    for y in temp_temp_domain_xj:
        flag=True
        for x in temp_temp_domain_xi:
            if constraint(x,y):
                flag=False
        if flag:
            temp_domain_xj.remove(y)
    return temp_domain_xj


def domain_number(i):
    if isPrime(i):
        return 1
    if i % 5 == 0:
        return 5
    if i % 4 == 0:
        return 4
    if i % 2 == 0:
        return 3
    if i % 2 == 1:
        return 2
    return 0


def check_consistency(xi,xj,domain_xi,domain_xj):
    if(xj>xi and xi%2==0 and xj%2==0):
        #print '1',xi,xj
        (domain_xi, domain_xj) = change_domain_constraint(domain_xi, domain_xj,constraint1)
        return domain_xi, domain_xj
    if(isPrime(xi)==False and isPrime(xj)==False):
        #print '2',xi,xj
        (domain_xi, domain_xj) = change_domain_constraint(domain_xi, domain_xj,constraint2)
        return domain_xi, domain_xj
    if((xi%2==1 and xj%2==0) or (xi%2==0 and xj%2==1)):
        #print '3',xi,xj
        (domain_xi, domain_xj) = change_domain_constraint(domain_xi, domain_xj,constraint3)
        return domain_xi, domain_xj
    if(xj>xi and xi%2==1 and xj%2==1):
        #print '4',xi,xj
        (domain_xi, domain_xj) = change_domain_constraint(domain_xi, domain_xj,constraint4)
        return domain_xi, domain_xj
    if xj>2*xi and xi%4!=0:
        #print '5',xi,xj
        (domain_xi, domain_xj) = change_domain_constraint(domain_xi, domain_xj,constraint5)
        return domain_xi, domain_xj
    if xj%4==0 and xi%2==1:
        #print '6',xi,xj
        (domain_xi, domain_xj) = change_domain_constraint(domain_xi, domain_xj, constraint6)
        return domain_xi, domain_xj
    return domain_xi,domain_xj

def check_consistency_AC3(xi,xj,domain_xi,domain_xj):
    if xi<xj:
        if(xj>xi and (xi%2==0 and xj%2==0)):
            domain_xi= change_domain_constraint_xi(domain_xi, domain_xj,constraint1)
            return domain_xi
        if(isPrime(xi)==False and isPrime(xj)==False):
            domain_xi = change_domain_constraint_xi(domain_xi, domain_xj,constraint2)
            return domain_xi
        if((xi%2==1 and xj%2==0) or (xi%2==0 and xj%2==1)):
            domain_xi= change_domain_constraint_xi(domain_xi, domain_xj,constraint3)
            return domain_xi
        if(xj>xi and xi%2==1 and xj%2==1):
            domain_xi = change_domain_constraint_xi(domain_xi, domain_xj,constraint4)
            return domain_xi
        if(xj>2*xi and xi%4!=0):
            domain_xi = change_domain_constraint_xi(domain_xi, domain_xj,constraint5)
            return domain_xi
        if xj % 4 == 0 and xi % 2 == 1:
            domain_xi = change_domain_constraint_xi(domain_xi, domain_xj, constraint6)
            return domain_xi
        return  domain_xi
    else:
        temp=xi
        xi=xj
        xj=temp
        if (xj > xi and (xi % 2 == 0 and xj % 2 == 0)):
            domain_xj = change_domain_constraint_xj(domain_xi, domain_xj, constraint1)
            return domain_xj
        if (isPrime(xi) == False and isPrime(xj) == False):
            domain_xj = change_domain_constraint_xj(domain_xi, domain_xj, constraint2)
            return domain_xj
        if ((xi % 2 == 1 and xj % 2 == 0) or (xi % 2 == 0 and xj % 2 == 1)):
            domain_xj = change_domain_constraint_xj(domain_xi, domain_xj, constraint3)
            return domain_xj
        if (xj > xi and xi % 2 == 1 and xj % 2 == 1):
            domain_xj = change_domain_constraint_xj(domain_xi, domain_xj, constraint4)
            return domain_xj
        if (xj > 2 * xi and xi%4!=0):
            domain_xj = change_domain_constraint_xj(domain_xi, domain_xj, constraint5)
            return domain_xj
        if xj % 4 == 0 and xi % 2 == 1:
            domain_xj = change_domain_constraint_xj(domain_xi, domain_xj, constraint6)
            return domain_xj
        return domain_xj
def put_edge_to_queue(edge_list,node,queue,queue1):
    for i,j in edge_list:
        if i==node:
            if j < i:
                if (i,j) not in queue:
                    queue.append((i,j))
                if (j,i) not in queue1:
                    queue1.append((j,i))
        if j==node:
            if i < j:
                if (j,i) not in queue:
                    queue.append((j,i))
                if (i,j) not in queue1:
                    queue1.append((i,j))
    return  queue,queue1


def put_edge_to_queue1(edge_list,queue1,k,i,m):
    for u,v in edge_list:
        if u==k:
            p=v
            if p<=i and p!=m:
                if (p,k) not in queue1:
                    queue1.append((p,k))
        if v==k:
            p=u
            if p<i and p!=m:
                if (p,k) not in queue1:
                    queue1.append((p,k))
    return queue1

def edgeExist(i,j,edge_list):
    for u,v in edge_list:
        if (i==u and j==v) or (i==v  and j==u):
            return  True
    return  False
def check_consistence_value(xi,xj,x,y):
    if xi<xj:
        if(xj>xi and xi%2==0 and xj%2==0):
            return constraint1(x,y)
        if(isPrime(xi)==False and isPrime(xj)==False):
            return constraint2(x, y)
        if((xi%2==1 and xj%2==0) or (xi%2==0 and xj%2==1)):
            return constraint3(x, y)
        if(xj>xi and xi%2==1 and xj%2==1):
            return constraint4(x, y)
        if(xj>2*xi and xi%4!=0):
            return constraint5(x,y)
        if xj % 4 == 0 and xi % 2 == 1:
            return constraint6(x,y)
        return True
    else:
        temp=xi
        xi=xj
        xj=temp
        if (xj > xi and (xi % 2 == 0 and xj % 2 == 0)):
            return constraint1(y,x)
        if (isPrime(xi) == False and isPrime(xj) == False):
            return constraint2(y, x)
        if (xi % 2 == 1 and xj % 2 == 0) or (xi % 2 == 0 and xj % 2 == 1):
            return constraint3(y,x)
        if (xj > xi and xi % 2 == 1 and xj % 2 == 1):
            return constraint4(y, x)
        if (xj > 2 * xi and x%4 !=0):
            return constraint5(y, x)
        if xj % 4 == 0 and xi % 2 == 1:
            return constraint6(y,x)

        return True

def checkconsist():
    for i in range(1,10):
        i=5
    return

def domainExist(x,domain):
    for a in domain:
        if a==x:
            return True
    return False


def AC1(node_domain,edge_list):
    flag=False
    while flag==False:
        #print 'doke'
        flag=True
        for u,v in edge_list:
            xi=min(u,v)
            xj=max(u,v)
            #print node_domain[xi],node_domain[xj]
            lenth_domain_xi=len(node_domain[xi])
            lenth_domain_xj=len(node_domain[xj])
            node_domain[xi],node_domain[xj]=check_consistency(xi,xj,node_domain[xi],node_domain[xj])
            #print xi,xj,node_domain[xi],node_domain[xj]
            if len(node_domain[xi])==0 or len(node_domain[xj])==0:
                return {}

            if lenth_domain_xi !=len(node_domain[xi]) or lenth_domain_xj != len(node_domain[xj]):
                flag=False
    return node_domain


def AC2(node_domain , edge_list,tatal_node):
    q = []
    q1 = []
    for i in range(1,tatal_node+1):
        q,q1=put_edge_to_queue(edge_list,i,q,q1)
        while len(q)!=0:
            while len(q)!=0:
                xi,xj=q[0] #xi==k and xj==m
                q.pop(0)
                xi = int(xi)
                xj = int(xj)
                checkconsist()
                if xi < xj:
                    prev_len_domain_xi = len(node_domain[xi])
                    node_domain[xi] = check_consistency_AC3(xi, xj, node_domain[xi], node_domain[xj])
                    if len(node_domain[xi])==0:
                        return {}
                    if (prev_len_domain_xi != len(node_domain[xi])):
                        q1=put_edge_to_queue1(edge_list,q1,xi,i,xj)
                else:
                    prev_len_domain_xi = len(node_domain[xj])
                    node_domain[xi] = check_consistency_AC3(xi, xj, node_domain[xj], node_domain[xi])
                    if (prev_len_domain_xi != len(node_domain[xi])):
                        if len(node_domain[xi]) == 0:
                            return {}
                        q1=put_edge_to_queue1(edge_list,q1,xi,i,xj)
            while len(q1)!=0:
                #print 'q1',q1
                e=q1[0]
                q1.pop(0)
                q.append(e)

    return node_domain



def AC3(node_domain,edge_list):
    q=[]
    for a,b in edge_list:
        q.append((a,b))
        q.append((b,a))
    while len(q)!=0:
        xi,xj=q[0]
        q.pop(0)
        xi=int(xi)
        xj=int(xj)
        if xi < xj:
            prev_len_domain_xi=len(node_domain[xi])
            node_domain[xi]=check_consistency_AC3(xi,xj,node_domain[xi],node_domain[xj])
            if len(node_domain[xi]) == 0:
                return {}
            if(prev_len_domain_xi!=len(node_domain[xi])):
                for a,b in edge_list:
                    if a==xi:
                        if (b,a) not in q:
                            q.append((b,a))
                            continue
                    if b==xi:
                        if (a,b) not in q:
                            q.append((a,b))


        else:
            prev_len_domain_xi=len(node_domain[xj])
            node_domain[xi] = check_consistency_AC3(xi, xj, node_domain[xj], node_domain[xi])
            if len(node_domain[xi]) == 0:
                return {}
            if(prev_len_domain_xi!=len(node_domain[xi])):
                for a, b in edge_list:
                    if a==xi:
                        if (b,a) not in q:
                            q.append((b,a))
                            continue
                    if b==xi:
                        if (a,b) not in q:
                            q.append((a,b))

    return node_domain

def AC4(node_domain, edge_list,total_node):
    temp_edge_list=copy.deepcopy(edge_list)
    for a,b in temp_edge_list:
        edge_list.append((b,a))
    #print 'edge list',edge_list
    S={}
    counter={}

    for i in range(1, total_node+1):
        for val in node_domain[i]:
            S[(i,val)]=[]
    DeletionStream=Queue.Queue()
    for i in range(1, total_node+1):
        for j in range(1,total_node+1):
            if (i,j) in edge_list:
                #print i,j
                temp_domain_xi = copy.deepcopy(node_domain[i])
                temp_domain_xj = copy.deepcopy(node_domain[j])
                for x in temp_domain_xi:
                    total=0
                    for y in temp_domain_xj:
                        if check_consistence_value(i,j,x,y):
                            #print x,y ,'nd'
                            total=total+1
                            S[(j,y)].append((i,x))
                    if total==0:
                        #print x,y,'d'
                        node_domain[i].remove(x)
                        #print 'nodedomain[i]',node_domain[i]
                        DeletionStream.put((i,x))
                        if len(node_domain[i])==0:
                            return {}
                    else:
                        counter[(i,j,x)]=total
    while DeletionStream.empty()==False:
        vi,x =DeletionStream.get()
        vi=int(vi)
        x=int(x)
        for vj,y in S[(vi,x)]:
            counter[(vj,vi,y)]=counter[(vj,vi,y)]-1
            if counter[(vj,vi,y)]==0:
                if domainExist(y,node_domain[vj]):
                    node_domain[vj].remove(y)
                    DeletionStream.put((vj,y))
                    if len(node_domain[vj])==0:
                        return {}
    return node_domain

def printnode(node_domain):
    if len(node_domain)==0:
        print 'incosistent graph'
    else:
        for node in node_domain:
            print node_domain[node]
    return

def createGraphRandom(total_node,edge_list):
    density=random.randint(1,20)

    total_edge=int(total_node*(total_node-1)*density/(2*100))
    for i in range(0,total_edge):
        #print i
        flag=True
        u = random.randint(1, total_node)
        v = random.randint(1, total_node)
        if u==v:
            u=(u+1)%(total_node+1)
            if u==0:
                u=1
        while True:
            minval=min(u,v)
            maxval=max(u,v)
            u=minval
            v=maxval
            if u==v:
                continue
            if (u,v) not in edge_list:
                edge_list.append((u,v))
                break
            for x in range(u,total_node+1):
                flag=False
                for y in range(x+1,total_node+1):
                    if (x,y) not in edge_list:
                        flag=True
                        break
                if flag:
                    u=x
                    v=y
                    break

            if u==v:
                continue
            if (u,v) not in edge_list:
                edge_list.append((u,v))
                break
    return edge_list
def create_DAG_graph(total_node,edge_list):
    visitedlist=[]
    for i in range(1,total_node):
        visitedlist.append(i)
        childnode=random.randint(0,5)
        for j in range(0,childnode):
            v=random.randint(1,total_node)
            temp=v
            while v in visitedlist:
                v=(v+1)%total_node+1
                if v==temp:
                    break
                if v==0:
                    v=1
            if v not in visitedlist:
                edge_list.append((i,v))
                visitedlist.append(v)
    return edge_list

def create_scale_free_graph(total_node,edge_list):
    #print 'function' ,edge_list
    degreelist=[]
    u=random.randint(1,total_node-1)
    v=random.randint(1,total_node)
    if u==v:
        u=u+1
    edge_list.append((u,v))
    degreelist.append(u)
    degreelist.append(v)
    for i in range(1,total_node+1):
        if i==u or i==v:
            continue
        x=len(degreelist)
        a=random.randint(0,x-1)
        b=random.randint(0,x-1)
        uc=degreelist[a]
        vc=degreelist[b]
        if uc!=vc:
            edge_list.append((i,uc))
            edge_list.append((i,vc))
            degreelist.append(uc)
            degreelist.append(vc)
        else:
            edge_list.append((i,uc))
            degreelist.append(uc)
            vc=(vc+1)%(total_node+1)
            if vc==0:
                vc=vc+1
            edge_list.append((i, vc))
            degreelist.append(vc)

    return edge_list

def create_domain(domain_number):
    domain = {}
    domain[1] = []
    domain[2] = []
    domain[3] = []
    domain[4] = []
    domain[5] = []
    for i in range(1, domain_number+1):
        domain[1].append(i)
    n=domain_number/4
    for i in range(1, domain_number+n+1):
        if i % 4 == 0:
            continue
        domain[2].append(i)

    for i in range(2, 2*domain_number+1, 2):
        domain[3].append(i)

    for i in range(1, domain_number):
        domain[4].append(i * i)

    for i in range(1, 2*domain_number+2, 2):
        domain[5].append(i)
    return domain
domain_n=input()
edge_list=[]
#domain = {1: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 2: {10, 11, 12, 13, 14, 15}, 3: {2, 4, 6, 8, 10}, 4: {1, 4, 9, 14, 16, 25, 36, 49, 64, 81, 100}, 5: {3, 5, 7, 9, 11}}
hor1=[]
ver1=[]
hor2=[]
ver2=[]
hor3=[]
ver3=[]
hor4=[]
ver4=[]
for k in range(10,101,10):
    hor1.append(k)
    hor2.append(k)
    hor3.append(k)
    hor4.append(k)
    domain = create_domain(domain_n)
    total_node=k
    print 'total node',total_node
    node_domain = {}

    for i in range(1, total_node + 1):
        node_domain[i] = copy.deepcopy(domain[domain_number(i)])

    #print 'nodedomain' ,node_domain
    # edge_list=createGraphRandom(total_node,edge_list)

    # edge_list=[(2, 5), (6, 10), (3, 10), (1, 7), (8, 9), (2, 9), (6, 8)]
    # edge_list=[(1,5),(7,10),(2,10),(4,5)]
    # edge_list=[(1,2),(2,3)]
    # edge_list=create_DAG_graph(total_node,edge_list)
    temp_edge_list=[]
    while True:
        #print 'templist', temp_edge_list
        temp_edge_list = createGraphRandom(total_node, [])
        edge_list_1=copy.deepcopy(temp_edge_list)
        temp_node_domain_1 = copy.deepcopy(node_domain)
        temp_node_domain = AC1(temp_node_domain_1, edge_list_1)
        #print 'koro', edge_list
        #print temp_node_domain
        if len(temp_node_domain)!=0:
            break


    edge_list=temp_edge_list
    #print(edge_list)
    #for i in range(1, total_node + 1):
        #print i, node_domain[i]
    temp_node_domain_5 = copy.deepcopy(node_domain)
    temp_node_domain_2=copy.deepcopy(node_domain)
    temp_node_domain_3=copy.deepcopy(node_domain)
    temp_node_domain_4=copy.deepcopy(node_domain)
    edge_list_1=copy.deepcopy(edge_list)
    edge_list_2=copy.deepcopy(edge_list)
    edge_list_3=copy.deepcopy(edge_list)
    edge_list_4=copy.deepcopy(edge_list)
    starttime=time.time()
    print('----------------------------AC1--------------')
    temp_node_domain=AC1(temp_node_domain_5,edge_list_1)
    printnode(temp_node_domain)
    endtime=time.time()
    a=endtime-starttime
    ver1.append(a)
    starttime = time.time()
    print('------------------------AC2-----------------')
    temp_node_domain=AC2(temp_node_domain_2,edge_list_2,total_node)
    printnode(temp_node_domain)
    endtime = time.time()
    b=endtime-starttime
    ver2.append(b)
    starttime=time.time()
    print('-------------------------AC3-----------')
    temp_node_domain=AC3(temp_node_domain_3,edge_list_3)
    printnode(temp_node_domain)
    endtime=time.time()
    c=endtime-starttime
    ver3.append(c)
    starttime=time.time()
    print('------------------------AC4-----------------')
    tem_node_domain=AC4(temp_node_domain_4,edge_list_4,total_node)
    printnode(temp_node_domain)
    endtime=time.time()
    d=endtime-starttime
    ver4.append(d)

print('ver1')
for a in ver1:
    print(a)
print('ver2')
for a in ver2:
    print(a)
print('ver3')
for a in ver3:
    print(a)
print('ver4')
for a in ver4:
    print(a)
plot.plot(hor1,ver1,'g-o',label='AC1')
plot.xlabel('no. of nodes')
plot.ylabel('Performing time')
plot.title('domain size'+str(domain_n))
plot.plot(hor2,ver2,'k-o',label='AC2')
plot.plot(hor3,ver3,'r-o',label='AC3')
plot.plot(hor4,ver4,'b-o',label='AC4')
plot.legend(loc='upper left')
plot.show()
"""
    5
    7
    1
    2
    1
    4
    1
    3
    2
    3
    2
    4
    3
    5
    4
    5
    """
"""
    4
    5
    1
    2
    1
    3
    2
    3
    2
    4
    3
    4
    """
