from PC import PCNode,pc_hash
# pc_hash[1] = 32

newPC = PCNode(1)
newPC.updatePcHashTable(newPC)

newPC = PCNode(2)
newPC.updatePcHashTable(newPC)

newPC = PCNode(3)
newPC.updatePcHashTable(newPC)

newPC = PCNode(4)
newPC.updatePcHashTable(newPC)

newPC = PCNode(5)
newPC.updatePcHashTable(newPC)

newPC = PCNode(6)
newPC.updatePcHashTable(newPC)

pc_hash[1].addNeighbour(2, 40, 0)
pc_hash[1].addNeighbour(3, 10, 0)
pc_hash[1].addNeighbour(4, 15, 0)

pc_hash[2].addNeighbour(3, 5, 0)
pc_hash[2].addNeighbour(5, 25, 0)

pc_hash[3].addNeighbour(5, 20, 0)
pc_hash[3].addNeighbour(4, 30, 0)

pc_hash[4].addNeighbour(6, 10, 0)

pc_hash[5].addNeighbour(6, 5, 0)


pc_hash[1].makeRoutingTable()


# Shortest distances from source node 1: {1: 0, 2: 40, 3: 10, 4: 15, 5: 30, 6: 40}
