import networkx as nx
import matplotlib.pyplot as plt
# from fa2 import ForceAtlas2
import plotly.graph_objects as go


# Dictionary to store PCs and links
network_graph = nx.Graph()

# Function to add a new PC
def add_pc(pc_name):
    network_graph.add_node(pc_name)
    print(f"PC '{pc_name}' added to the network.")

# Function to add a link between two PCs
def add_link(pc1, pc2, weight=1):
    if network_graph.has_node(pc1) and network_graph.has_node(pc2):
        network_graph.add_edge(pc1, pc2, weight=weight)
        print(f"Link added between '{pc1}' and '{pc2}'.")
    else:
        print("One or both PCs not found in the network.")

# Function to remove a PC
def remove_pc(pc_name):
    if network_graph.has_node(pc_name):
        network_graph.remove_node(pc_name)
        print(f"PC '{pc_name}' removed from the network.")
    else:
        print(f"PC '{pc_name}' not found.")

# Function to remove a link between two PCs
def remove_link(pc1, pc2):
    if network_graph.has_edge(pc1, pc2):
        network_graph.remove_edge(pc1, pc2)
        print(f"Link removed between '{pc1}' and '{pc2}'.")
    else:
        print(f"No link between '{pc1}' and '{pc2}'.")

# Function to print all active PCs
def print_active_pcs():
    print("Currently Active PCs:", list(network_graph.nodes))

# Function to print routing table of a PC (neighbors)
def print_routing_table(pc_name):
    if network_graph.has_node(pc_name):
        print(f"Routing Table of '{pc_name}':", list(network_graph.neighbors(pc_name)))
    else:
        print(f"PC '{pc_name}' not found.")



def visualize_interactive():
    pos = nx.spring_layout(network_graph, seed=42)  # Use spring layout for positions

    edge_x, edge_y = [], []
    for edge in network_graph.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    node_x, node_y = zip(*pos.values())
    node_text = list(network_graph.nodes())

    edge_trace = go.Scatter(x=edge_x, y=edge_y, mode='lines', line=dict(width=1, color='gray'))
    node_trace = go.Scatter(
        x=node_x, y=node_y, mode='markers+text', text=node_text,
        marker=dict(size=10, color='skyblue', line=dict(width=2, color='black')),
        textposition='top center'
    )

    fig = go.Figure(data=[edge_trace, node_trace])
    fig.update_layout(title="Interactive Network", showlegend=False, title_x=0.5)
    fig.show()



def visualize_shortest_path(pc1, pc2):
    try:
        # Calculate the shortest path
        path = nx.shortest_path(network_graph, source=pc1, target=pc2, weight='weight')
        print(f"Shortest path from '{pc1}' to '{pc2}': {path}")

        # Generate positions using spring layout
        pos = nx.spring_layout(network_graph, seed=42)

        # Prepare edge traces for the entire network
        edge_x, edge_y = [], []
        for edge in network_graph.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])

        # Prepare a separate trace for the shortest path edges
        path_edge_x, path_edge_y = [], []
        path_edges = list(zip(path, path[1:]))  # Consecutive nodes in the shortest path
        for edge in path_edges:
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            path_edge_x.extend([x0, x1, None])
            path_edge_y.extend([y0, y1, None])

        # Create traces for edges
        edge_trace = go.Scatter(
            x=edge_x, y=edge_y, mode='lines', line=dict(width=1, color='gray'), hoverinfo='none'
        )

        path_trace = go.Scatter(
            x=path_edge_x, y=path_edge_y, mode='lines', 
            line=dict(width=3, color='red'), hoverinfo='none'
        )

        # Prepare node trace
        node_x, node_y = zip(*pos.values())
        node_text = list(network_graph.nodes())

        node_trace = go.Scatter(
            x=node_x, y=node_y, mode='markers+text', text=node_text,
            marker=dict(size=10, color='skyblue', line=dict(width=2, color='black')),
            textposition='top center'
        )

        # Create the Plotly figure
        fig = go.Figure(data=[edge_trace, path_trace, node_trace])
        fig.update_layout(
            title=f"Shortest Path from {pc1} to {pc2}", 
            title_x=0.5, showlegend=False
        )
        fig.show()

    except nx.NetworkXNoPath:
        print(f"No path between '{pc1}' and '{pc2}'.")
    except nx.NodeNotFound:
        print(f"One or both PCs not found.")



# Example usage
if __name__ == "__main__":
    while True:
        print("\n1 : Add new PCs to the Network")
        print("2 : Add Links between 2 PCs")
        print("3 : Print Routing Table of PC")
        print("4 : Print shortest path from one PC to another")
        print("5 : Remove a link between 2 PCs")
        print("6 : Remove a PC from the Network")
        print("7 : Print currently Active PCs")
        print("8 : Visualize Network")
        print("9 : Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            pc_name = input("Enter PC name: ")
            add_pc(pc_name)

        elif choice == 2:
            pc1 = input("Enter first PC: ")
            pc2 = input("Enter second PC: ")
            weight = int(input("Enter weight of the link: "))
            add_link(pc1, pc2, weight)

        elif choice == 3:
            pc_name = input("Enter PC name: ")
            print_routing_table(pc_name)

        elif choice == 4:
            pc1 = input("Enter source PC: ")
            pc2 = input("Enter destination PC: ")
            visualize_shortest_path(pc1, pc2)

        elif choice == 5:
            pc1 = input("Enter first PC: ")
            pc2 = input("Enter second PC: ")
            remove_link(pc1, pc2)

        elif choice == 6:
            pc_name = input("Enter PC name: ")
            remove_pc(pc_name)

        elif choice == 7:
            print_active_pcs()

        elif choice == 8:
            visualize_interactive()

        elif choice == 9:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")
