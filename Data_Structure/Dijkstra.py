from Data_Structure.Priority_Queue import PriorityQueue

def shortestPathAlgo(srcId,pc_hash):
    distance = {key: float('inf') for key in pc_hash.keys()}
    distance[srcId]=0
    pq=PriorityQueue()
    pq.push(0,srcId) # Distance,ID

    while not pq.isEmpty():
        top_PC = pq.pop()
        topDist = top_PC[0]
        topID = top_PC[1]

        node=pc_hash[topID]

        for neighbourPC in node.neighbourList:
            neighbourID = neighbourPC[0]
            neighbourCost = neighbourPC[1]

            newDistance=topDist + neighbourCost

            if newDistance < distance[neighbourID]:
                distance[neighbourID] = newDistance
                pq.push(newDistance, neighbourID)

    return distance