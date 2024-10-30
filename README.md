# Network-Simulation

This project is a simulation of a real-world **Link-State Routing Algorithm**, allowing for dynamic manipulation of network elements. With this simulation, you can add or remove routers, PCs, and links, demonstrating how routing algorithms adapt in real-time to changes in network topology. This simulation is built in **Python** using the `networkx` and `graphviz` libraries for efficient graph handling and visualization.

## Features

- **Dynamic Network Manipulation**: Add or remove routers/PCs and establish or delete connections between nodes in real-time.
- **Adaptive Link-State Routing**: The algorithm adapts automatically to changes, updating routing tables and paths across the network.
- **Custom Data Structures**: Data structures have been designed from scratch to support efficient storage and retrieval of network information.
- **Dijkstra's Algorithm**: Utilized to calculate the shortest path between two routers, enhancing pathfinding efficiency.
- **Graph Visualization**: Network structure and shortest paths are visualized using `networkx` and `graphviz` to illustrate the routing process dynamically.

## Technologies

- **Language**: Python
- **Libraries**: `networkx`, `graphviz`

## Project Structure

- **Simulated Routing**: Implements link-state routing, recalculating routes dynamically as the network changes.
- **Visualization**: Visualizes the entire network and shortest paths between nodes.

## Usage

1. **Initial Terminal Interface**

   ![Initial Terminal Interface](./Photos/initial.png)

   When you start the Network Simulator, you’re presented with a menu to choose actions like adding/removing PCs and links, viewing routing tables, and visualizing the network.

2. **Printing Routing Table of a Router**

   ![Printing Routing Table](./Photos/routing.png)

   This option allows you to see the routing table for a specific PC, which includes paths and costs.

3. **Visualizing the Whole Network**

   ![Network Visualization](./Photos/graph.png)

   This displays the entire network graph with all routers and connections, as created in the simulator.

4. **Visualizing the Shortest Path**

   ![Shortest Path Visualization](./Photos/shortest.png)

   Shows the shortest path between two PCs, calculated using Dijkstra’s algorithm.


## How to Run

1. Install the required libraries:
   ```bash
   pip install networkx graphviz
   ```

2. Install graphviz tool from [official website](https://graphviz.org/download/) and add it to your PATH in windows. 

3. For checking proper installation of graphviz run
   ```bash
   dot -V
   ```
 
4. Run the network.py file for running the main program
   ```bash
   python Network.py
   ``` 
