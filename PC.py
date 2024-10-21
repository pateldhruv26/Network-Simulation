# from Data_Structure import greet

# print(Data_Structure.greet())      # Output: Hello from module 1!
# print(Data_Structure.farewell())

# from Data_Structure.Priority_Queue import greet
# print(greet())

from Data_Structure.Dijkstra import shortestPathAlgo
pc_hash={}

class PCNode:
    def __init__(self,id):
        self.id=id;
        self.neighbourList=[] #adj list
        self.routingTable=[0] #Dijkstra
        self.linkUsed=set() 
    
    def addNeighbour(self,neighbourId,cost,flag):
        self.neighbourList.append([neighbourId,cost])
        neighbourPc = pc_hash[neighbourId]

        if(flag==0):
            neighbourPc.addNeighbour(self.id,cost,1)
        
        
    
    # def removeNeighbour(self,neighbourId):
    def updatePcHashTable(self,address):
        pc_hash[self.id]=address

    def makeRoutingTable(self):
        # self.routingTable[0]=[0,self.id] #[Cost , Via]

        distance,via,self.linksUsed=shortestPathAlgo(self.id,pc_hash)

        for ind in range(1, len(pc_hash) + 1):
            pair = [distance[ind], via[ind]]
            if ind >= len(self.routingTable):
                self.routingTable.append(pair)
            else:
                self.routingTable[ind] = pair

        #routingTable={cost,via}
        print(self.routingTable,self.linksUsed)


        #adj list,

        #Dijkstra (id,pc_hash) 1st -> add -> neighbourList
        # 1-> 2,3,4

    
    