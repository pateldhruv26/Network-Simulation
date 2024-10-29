from Data_Structure.Dijkstra import shortestPathAlgo
pc_hash={}

class PCNode:
    def __init__(self,id):
        self.id=id;
        self.neighbourList={} # Adjacency List for the PC
        self.routingTable=[0] # Table: PCID -> [Cost to reach PCID, Via]
        self.linkUsed=set()   # Links Used in Dijkstra's Shortest Path

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
    
    