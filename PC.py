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
        self.neighbourList={} #adj list
        self.routingTable=[0] #Dijkstra #[Cost , Via]
        self.linkUsed=set() 

        self.updatePcHashTable()
    
    def updatePcHashTable(self):
        pc_hash[self.id]=self
    
    #To run makeRoutingTable from outside
    def addLink(self,neighbourId,cost):
        self.neighbourList[neighbourId]=cost
        pc_hash[neighbourId].neighbourList[self.id]=cost
    
    def deleteLink(self,neighbourId):
        del self.neighbourList[neighbourId]
        del pc_hash[neighbourId].neighbourList[self.id]
        linkId=str(min(self.id,neighbourId))+'Connects'+str(max(self.id,neighbourId))
        
        for key in pc_hash:
            if linkId in pc_hash[key].linksUsed:
                pc_hash[key].makeRoutingTable()

    
    
    # #To run makeRoutingTable from outside
    # def addNeighbour(self,neighbourId,cost,flag):
    #     self.neighbourList[neighbourId]=cost
    #     neighbourPc = pc_hash[neighbourId]

    #     if(flag==0):
    #         neighbourPc.addNeighbour(self.id,cost,1)


    
    #To run makeRoutingTable from outside
    def removePC(self):
        for key in self.neighbourList:
            del pc_hash[key].neighbourList[self.id]    

    def makeRoutingTable(self):
        distance,via,self.linksUsed=shortestPathAlgo(self.id,pc_hash)

        for ind in range(1, len(pc_hash) + 1):
            pair = [distance[ind], via[ind]]
            if ind >= len(self.routingTable):
                self.routingTable.append(pair)
            else:
                self.routingTable[ind] = pair

        # print(self.id,self.routingTable,self.linksUsed)


        #adj list,

        #Dijkstra (id,pc_hash) 1st -> add -> neighbourList
        # 1-> 2,3,4

    
    