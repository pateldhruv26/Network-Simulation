from flask import Flask, render_template, jsonify, request
import networkx as nx

app = Flask(__name__)
G = nx.Graph()  # Create an empty graph

# API route to add a new PC to the network
@app.route('/add-pc', methods=['POST'])
def add_pc():
    pc_name = request.json.get('name')
    G.add_node(pc_name)
    return jsonify({'message': f'PC {pc_name} added'}), 201

# API route to add a link between two PCs
@app.route('/add-link', methods=['POST'])
def add_link():
    data = request.json
    pc1, pc2 = data['pc1'], data['pc2']
    weight = data.get('weight', 1)
    G.add_edge(pc1, pc2, weight=weight)
    return jsonify({'message': f'Link between {pc1} and {pc2} added'}), 201

# API route to calculate the shortest path between two PCs
@app.route('/shortest-path', methods=['POST'])
def shortest_path():
    data = request.json
    source, target = data['source'], data['target']

    try:
        path = nx.shortest_path(G, source=source, target=target, weight='weight')
        edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        return jsonify({'path': path, 'edges': edges})
    except nx.NetworkXNoPath:
        return jsonify({'error': f'No path found between {source} and {target}'}), 404

# API route to fetch the current network data
@app.route('/network-data')
def get_network_data():
    nodes = [{'id': n, 'label': str(n)} for n in G.nodes()]
    edges = [{'from': u, 'to': v, 'color': 'gray'} for u, v in G.edges()]
    return jsonify({'nodes': nodes, 'edges': edges})

# Serve the HTML page with the vis.js visualization
@app.route('/')
def home():
    return render_template('index.html')

# Start the Flask app
if __name__ == '__main__':
    # Example: Add some initial PCs and links
    G.add_node("PC1")
    G.add_node("PC2")
    G.add_node("PC3")
    G.add_edge("PC1", "PC2", weight=5)
    G.add_edge("PC2", "PC3", weight=3)
    app.run(debug=True)
