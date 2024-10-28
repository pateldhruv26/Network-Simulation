from Data_Structure.PC import PCNode,pc_hash
import heapq
import time
import graphviz
import networkx as nx

newPCId=[1]
activePC = set()
graph = nx.Graph()
heapq.heapify(newPCId)

def addNewPCs():
    pcToAdd = int(input("Enter Number of PCs To Add: "))
    while pcToAdd>0:
        newId = heapq.heappop(newPCId)
        PCNode(newId)
        activePC.add(newId)
        graph.add_node(newId)
        if len(newPCId) == 0:
            heapq.heappush(newPCId,newId+1)
        
        pcToAdd-=1


def addLinks():
    linksToAdd = int(input("Enter Number of Links To Add: "))
    links=[]
    while linksToAdd>0:
        pc1Id,pc2Id,cost=map(int, input("Enter <PC1 id,PC2 id,Cost>: ").split())
        if pc1Id in pc_hash and pc2Id in pc_hash and pc1Id!=pc2Id:
            links.append([pc1Id,pc2Id,cost])
            linksToAdd-=1
    
        else:
            if pc1Id not in pc_hash:
                print("PC1 does not exsist")
            elif pc2Id not in pc_hash:
                print("PC2 does not exsist")
            else:
                print("Same PC not allowed")
    
    for link in links:
        pc_hash[link[0]].addLink(link[1],link[2])
        graph.add_edge(link[0],link[1],cost=link[2])
    makeNetwork()

def removePC(id):
    if id in pc_hash:
        pc_hash[id].removePC()
        activePC.remove(id)
        graph.remove_node(id)
        heapq.heappush(newPCId,id)
        makeNetwork()
    
    else:
        print("PC does not exsist")

# Dont run makeNetwork()
def deleteLink(pc1Id,pc2Id):
    if pc1Id in pc_hash and pc2Id in pc_hash and pc2Id in pc_hash[pc1Id].neighbourList:
        pc_hash[pc1Id].deleteLink(pc2Id)
        graph.remove_edge(pc1Id, pc2Id)
        print("PC removed successfully.")
    
    else:
        if pc1Id not in pc_hash:
            print("PC1 does not exsist")
        elif pc2Id not in pc_hash:
            print("PC2 does not exsist")
        else:
            print("Link does not exsist")

def makeNetwork():
    for key in pc_hash:
        pc_hash[key].makeRoutingTable()

def pathTracing(pc1Id,pc2Id):
    if pc1Id==pc2Id:
        print("Both PC are same")
        return []
    
    elif len(pc_hash[pc1Id].routingTable)<=pc2Id or pc_hash[pc1Id].routingTable[pc2Id][0] == float('inf'):
        print("PC2 is unreachable from PC1")
        return []

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
        return path

    else:
        print("One or both PC does not exsist")

def visualizeNetwork():
    graphviz_graph = graphviz.Graph()
    graphviz_graph.attr(rankdir='LR',nodesep='1',ranksep='1')
    graphviz_graph.edge_attr.update(fontsize='25')

    for node in graph.nodes():
        graphviz_graph.node(str(node), color='lightblue', style='filled', width='0.7', height='0.7', shape='ellipse', fontsize='25')

    for edge in graph.edges(data=True):
        pc1Id, pc2Id, cost = edge
        graphviz_graph.edge(str(pc1Id),str(pc2Id), label=str(cost['cost']),penwidth='4',color='blue',fontcolor='blue')

    graphviz_graph.render('graph', format='png', view=True)

def visualizeShortestPath(pc1Id,pc2Id):
    path=pathTracing(pc1Id, pc2Id)
    if(len(path)==0):
        return

    graphviz_graph = graphviz.Graph()
    graphviz_graph.attr(rankdir='LR',nodesep='1',ranksep='1')
    graphviz_graph.edge_attr.update(fontsize='25')

    for node in graph.nodes():
        graphviz_graph.node(str(node), color='orange' if node in path else 'lightblue', style='filled', width='0.7', height='0.7', shape='ellipse', fontsize='25')
    
    for edge in graph.edges(data=True):
        pc1Id, pc2Id, cost = edge
        if pc1Id in path and pc2Id in path and abs(path.index(pc1Id)-path.index(pc2Id))==1:
            graphviz_graph.edge(str(pc1Id),str(pc2Id), label=str(cost['cost']),penwidth='4',color='red',fontcolor='red')
        else:
            graphviz_graph.edge(str(pc1Id),str(pc2Id), label=str(cost['cost']),penwidth='4',color='blue',fontcolor='blue')    
    graphviz_graph.render('graph', format='png', view=True)

def printActivePC():
    print("Currently active PCs are: ",activePC)

def printMenu():
    print("\n\nWelcome to Network Simulator\n")
    print("\nSelect an option")
    print("1 : Add new PCs to the Network")
    print("2 : Add Links between 2 PCs")
    print("3 : Remove a PC from the Network")
    print("4 : Remove a link between 2 PCs")
    print("5 : Print currently Active PCs")
    print("6 : Print Routing Table of PC")
    print("7 : Visualize the network")
    print("8 : Print shortest path from one PC to another")
    print("9 : Exit")

def menu(option):
    match option:
        case '1':
            addNewPCs()
            print("New PCs added.")
        case '2':
            addLinks()
            print("Links added.")
        case '3':
            pcId = int(input("Enter PC ID to remove: "))
            removePC(pcId)
        case '4':
            pc1Id = int(input("Enter PC1 ID: "))
            pc2Id = int(input("Enter PC2 ID: "))
            deleteLink(pc1Id,pc2Id)
        case '5':
            print("Currently active PCs:")
            printActivePC()
        case '6':
            pcId = int(input("Enter PC ID to print routing table: "))
            if pcId in pc_hash:
                print("PCiD [Cost,Via]")
                for i in range(1,len(pc_hash[pcId].routingTable)):
                    print(i,"  ",pc_hash[pcId].routingTable[i])
            else:
                print("PC does not exist.")
        case '7':
            visualizeNetwork()
        case '8':
            pc1Id = int(input("Enter PC1 ID: "))
            pc2Id = int(input("Enter PC2 ID: "))
            visualizeShortestPath(pc1Id, pc2Id)
        case _:
            print("Invalid option. Please try again.")


def main():
    while True:
        printMenu()
        option = input("Enter your choice: ")
        print("\033c", end="")
        print("Network Simulator\n")
        if option == '9':
            break

        try:
            menu(option)
        except Exception as e:
            print("Oops some error occured!! Try again")
        time.sleep(1)

main()
