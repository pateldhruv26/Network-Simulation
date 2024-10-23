from Data_Structure.Priority_Queue import PriorityQueue

def shortestPathAlgo(srcId,pc_hash):
    n=len(pc_hash)
    n=n+1
    distance = [float('inf')] * n

    via = [float('-1')] * n
    parent = [float('-1')] * n

    linksUsed = set()
    distance[srcId]=0
    via[srcId]=srcId
    pq=PriorityQueue()
    pq.push([0,srcId,srcId]) # Distance,ID
    parent[srcId]=srcId

    while not pq.isEmpty():
        top_PC = pq.pop()
        topDist = top_PC[0]
        topID = top_PC[1] 
        topVia = top_PC[2]   

        node=pc_hash[topID]

        for key,value in node.neighbourList.items():
            neighbourID = key
            neighbourCost = value

            newDistance=topDist + neighbourCost

            if newDistance < distance[neighbourID]:
                distance[neighbourID] = newDistance
                parent[neighbourID]=topID
                via[neighbourID]=topVia
                pq.push([newDistance, neighbourID,neighbourID if topID==srcId else topID])
    
    for id in pc_hash:
        if parent[id] != -1 and id != parent[id]:
            linksUsed.add(str(min(id,parent[id]))+"Connects"+str(max(id,parent[id])))
            

    return distance,via,linksUsed