from Data_Structure.PC import PCNode,pc_hash
import heapq
import time
newPCId=[1]
activePC = set()

heapq.heapify(newPCId)

def addNewPCs():
    pcToAdd = int(input("Enter Number of PCs To Add: "))
    while pcToAdd>0:
        newId = heapq.heappop(newPCId)
        PCNode(newId)
        activePC.add(newId)
        if len(newPCId) == 0:
            heapq.heappush(newPCId,newId+1)
        
        pcToAdd-=1


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

def removePC(id):
    if id in pc_hash:
        pc_hash[id].removePC()
        activePC.remove(id)
        heapq.heappush(newPCId,id)
        makeNetwork()
    
    else:
        print("PC does not exsist")

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
    
    elif len(pc_hash[pc1Id].routingTable)<=pc2Id or pc_hash[pc1Id].routingTable[pc2Id][0] == float('inf'):
        print("PC2 is unreachable from PC1")

    elif pc1Id in pc_hash and pc2Id in pc_hash:
        path=[pc1Id]
        currentPCId=pc1Id

        while pc_hash[currentPCId].routingTable[pc2Id][1] != currentPCId:
            path.append(pc_hash[currentPCId].routingTable[pc2Id][1])
            currentPCId=pc_hash[currentPCId].routingTable[pc2Id][1]
        
        path.append(pc2Id)

        for i in range(0,len(path)-1):
            print(path[i]," -> ",path[i+1])
        
        print("Total Cost is ",pc_hash[pc1Id].routingTable[pc2Id][0])

    else:
        print("One or both PC does not exsist")

def printActivePC():
    print(activePC)


def menu(option):
    match option:
        case '1':
            addNewPCs()
            print("New PCs added.")
        case '2':
            addLinks()
            print("Links added.")
        case '3':
            pcId = int(input("Enter PC ID to print routing table: "))
            if pcId in pc_hash:
                print(pc_hash[pcId].routingTable)
            else:
                print("PC does not exist.")
        case '4':
            pc1Id = int(input("Enter PC1 ID: "))
            pc2Id = int(input("Enter PC2 ID: "))
            pathTracing(pc1Id, pc2Id)
        case '5':
            pc1Id = int(input("Enter PC1 ID: "))
            pc2Id = int(input("Enter PC2 ID: "))
            deleteLinks(pc1Id,pc2Id)
        case '6':
            pcId = int(input("Enter PC ID to remove: "))
            removePC(pcId)
            print("PC removed if it existed.")
        case '7':
            print("Currently active PCs:")
            printActivePC()
        case _:
            print("Invalid option. Please try again.")

while True:
    print("\n\nWelcome to Network Simulator\n")
    print("\nSelect an option")
    print("1 : Add new PCs to the Network")
    print("2 : Add Links between 2 PCs")
    print("3 : Print Routing Table of PC")
    print("4 : Print shortest path from one PC to another")
    print("5 : Remove a link between 2 PCs")
    print("6 : Remove a PC from the Network")
    print("7 : Print currently Active PCs")
    print("8 : Exit")

    option = input("Enter your choice: ")
    print("\033c", end="")
    print("Network Simulator\n")
    if option == '8':
        break
    menu(option)
    time.sleep(0.5)
    







# addNewPC()
# addNewPC()
# addNewPC()
# addNewPC()
# addNewPC()
# addNewPC()
# addNewPC()

# printActivePC()
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

# addLinks()
# print(pc_hash[1].routingTable)

# pathTracing(1,7)


# deleteLinks(4,6)
# deleteLinks(2,3)
# deleteLinks(6,7)


# pathTracing(1,7)

# addLinks()

# addNewPc, addLinks, routing table print, pathTracing, remove pc, active pc