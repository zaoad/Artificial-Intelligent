
def backTracking(assign_variable,unassign_variable,csp,assignment,domain):
    """
    print('----------------')
    print(unassign_var)
    print(assignment)
    """
    if len(unassign_variable)==0:
        return assignment
    var=unassign_variable[0]
    for a in domain:
        if checkconsistency(csp,a,var,assignment):

            assign_variable.append(var)
            unassign_var.remove(var)
            assignment[var]=a
            result=backTracking(assign_variable,unassign_variable,csp,assignment,domain)
            if len(result)!=0 :
                return result
    return []




def checkconsistency(csp, val, node, assignment ):
    neighbours=csp[node]
    for neighbour in neighbours:
        if neighbour in assignment:
            if assignment[neighbour]==val:
                return False
    return True

domain = ['blue', 'red', 'green']
csp={'WA':{'NT','SA'},'NT':{'WA','SA','Q'},'Q':{'NT','SA','NSW'},'NSW':{'SA','Q','V'},'V':{'SA','NSW'},'SA':{'WA','NT','Q','NSW','V'},'T':{}}
unassign_var=['WA','NT','SA','Q','NSW','V','T']
assignment=dict()
answer=backTracking([],unassign_var,csp,{},domain)
if len(answer)!=0:
    print(answer)
else:
    print('no solution')

