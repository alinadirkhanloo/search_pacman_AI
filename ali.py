a={1:('B', '0:A->B', 1.0), 2:('C', '1:A->C', 2.0), 3:('D', '2:A->D', 4.0)}

print a[1]

q = []
visit = []
actions = []
start = problem.getStartState()
q.append(start)
visit.append(start)
neighbors = {}
while (len(q) != 0):
    node = q.pop()
    if neighbors:
        actions.append(neighbors[node])

    if problem.isGoalState(node):
        break
    else:
        temp = problem.getSuccessors(node)
        if temp:
            # print temp
            while temp:
                n = min(temp)
                temp.remove(n)
                if n[0] not in visit:
                    q.append(n[0])
                    visit.append(n[0])
                    neighbors[n[0]] = n[1]
                    print q
                    # print ("fffffffffffff", actions)
        else:
            actions = []





/////////////////////
q = []
visit = []
path = []
start = problem.getStartState()
q.append(start)
visit.append(start)
actions = {}
while (len(q) != 0):
    node = q.pop()
    if actions:
        path.append(actions[node])

    if problem.isGoalState(node):
        break
    else:
        temp = problem.getSuccessors(node)
        if temp:
            while temp:
                n = max(temp)
                temp.remove(n)
                if n[0] not in visit:
                    q.append(n[0])
                    visit.append(n[0])
                    actions[n[0]] = n[1]
                else:
                    actions[n[0]] = n[1]
                    # else:actions.pop()
                    print ("fffffffffffff", actions)
        else:
            path = []

# print ("aaaaaaaaaa",actions)
return path

print"------------------------------------------------"
q = []
visit = []
path = {}
start = problem.getStartState()
q.append(start)
visit.append(start)
actions = {}
while (len(q) != 0):
    node = q.pop()
    if actions:
        path[node] = actions[node]

    if problem.isGoalState(node):
        break
    else:
        temp = problem.getSuccessors(node)
        if temp:
            while temp:
                n = max(temp)
                temp.remove(n)
                if n[0] not in visit:
                    q.append(n[0])
                    visit.append(n[0])
                    actions[n[0]] = n[1]
                else:
                    actions[n[0]] = n[1]
                    # else:actions.pop()


        else:
            path = {}
act = []
print("-->", path)
while path:
    act.append(path.pop(min(path)))
return act


West West West West West West West West West West West West West West West West West West West West West West West West West West West West West West West West West South South South South South South South South South East East East North North North   North North North North East East South South South South South South East East North North North North North North East East South South South South East East North North East East East East East East East East               South East East East East East East East  South South South South South South South West West West West West West West West West West West West West West West West West South West West West West West West West West West
West West West West West West West West West West West West West West West West West West West West West West West West West West West West West West West West West South South South South South South South South South East East East North North North "North" North North North East East South South South South South South East East North North North North North North East East South South South South East East North North East East East East East East East East "South South" South East East East East East East East South South South South South South South West West West West West West West West West West West West West West West West West South West West West West West West West West West