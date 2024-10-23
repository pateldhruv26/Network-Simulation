from PC import PCNode,pc_hash
import heapq
newPCId=[1]

heapq.heapify(newPCId)


# pc_hash[1] = 32

# newPC = PCNode(1)

# newPC = PCNode(2)

# newPC = PCNode(3)

# newPC = PCNode(4)

# newPC = PCNode(5)

# newPC = PCNode(6)

# newPC = PCNode(7)


# pc_hash[4].makeRoutingTable()


def addNewPC():
    newId = heapq.heappop(newPCId)
    PCNode(newId)
    if len(newPCId) == 0:
        heapq.heappush(newPCId,newId+1)


def removePC(id):
    if id in pc_hash:
        pc_hash[id].removePC()
        heapq.heappush(newPCId,id)
        makeNetwork()
    
    else:
        print("PC does not exsist")


def addLinks():
    linksToAdd = int(input("Enter Number of Links To Add: "))
    while linksToAdd>0:
        pc1Id,pc2Id,cost=map(int, input("Enter <PC1 id,PC2 id,Cost>: ").split())
        if pc1Id in pc_hash and pc2Id in pc_hash:
            pc_hash[pc1Id].addLink(pc2Id,cost)
    
        else:
            print("One or both PC does not exsist")
        
        linksToAdd-=1;

    makeNetwork()


# Dont run makeNetwork()
def deleteLinks(pc1Id,pc2Id):
    if pc1Id in pc_hash and pc2Id in pc_hash and pc2Id in pc_hash[pc1Id].neighbourList:
        pc_hash[pc1Id].deleteLink(pc2Id)
    
    else:
        print("One or both PC does not exsist or link does not exsist")

def makeNetwork():
    for key in pc_hash:
        pc_hash[key].makeRoutingTable()

def pathTracing(pc1Id,pc2Id):
    if pc1Id==pc2Id:
        print("Both PC are same")
    
    elif pc_hash[pc1Id].routingTable[pc2Id][0] == float('inf'):
        print("Pc2 is unreachable from PC1")

    elif pc1Id in pc_hash and pc2Id in pc_hash:
        path=[pc1Id]
        currentPCId=pc1Id

        while pc_hash[currentPCId].routingTable[pc2Id][1] != currentPCId:
            path.append(pc_hash[currentPCId].routingTable[pc2Id][1])
            currentPCId=pc_hash[currentPCId].routingTable[pc2Id][1]
        
        path.append(pc2Id)

        for i in range(0,len(path)-1):
            print(path[i]," -> ",path[i+1])  

    else:
        print("One or both PC does not exsist")

def printActivePC():
    print(pc_hash)

addNewPC()
addNewPC()
addNewPC()
addNewPC()
addNewPC()
addNewPC()
addNewPC()

printActivePC()
# pc_hash[1].addLink(2, 40)
# pc_hash[1].addLink(3, 10)
# pc_hash[1].addLink(4, 15)
# pc_hash[2].addLink(3, 5)
# pc_hash[2].addLink(5, 25)
# pc_hash[3].addLink(5, 20)
# pc_hash[3].addLink(4, 30)
# pc_hash[4].addLink(6, 10)
# pc_hash[5].addLink(6, 5)
# pc_hash[6].addLink(7, 1)

# makeNetwork()

addLinks()
print(pc_hash[1].routingTable)

pathTracing(1,7)


deleteLinks(4,6)
deleteLinks(2,3)
deleteLinks(6,7)


pathTracing(1,7)

# addLinks()



# Shortest distances from source node 1: {1: 0, 2: 40, 3: 10, 4: 15, 5: 30, 6: 40}
