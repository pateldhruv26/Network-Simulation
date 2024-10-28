import networkx as nx
import json

# Create the graph
G = nx.Graph()

# Function to add a PC to the network
def add_pc(name):
    G.add_node(name)

# Function to add a link between two PCs with a weight (distance)
def add_link(pc1, pc2, weight):
    G.add_edge(pc1, pc2, weight=weight)

# Function to generate an HTML file with vis.js visualization
def generate_vis_js_html(filename="network.html"):
    nodes = [{'id': n, 'label': str(n)} for n in G.nodes()]
    edges = [{'from': u, 'to': v} for u, v in G.edges()]

    # HTML template with embedded vis.js code
    html_content = f"""
    <html>
    <head>
      <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.js"></script>
      <link href="https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.css" rel="stylesheet" type="text/css" />
      <style type="text/css">
        #mynetwork {{
          width: 100%;
          height: 600px;
          border: 1px solid lightgray;
        }}
      </style>
    </head>
    <body>
      <center><h1>Network Visualization</h1></center>
      <div id="mynetwork"></div>

      <script type="text/javascript">
        // Create an array with nodes
        var nodes = new vis.DataSet({json.dumps(nodes)});

        // Create an array with edges
        var edges = new vis.DataSet({json.dumps(edges)});

        // Create a network
        var container = document.getElementById('mynetwork');
        var data = {{
          nodes: nodes,
          edges: edges
        }};
        var options = {{
          nodes: {{
            shape: 'dot',
            size: 20,
            color: {{
              border: '#2B7CE9',
              background: '#97C2FC'
            }},
            font: {{
              color: 'black',
              size: 14
            }}
          }},
          edges: {{
            width: 2,
            color: 'gray'
          }},
          physics: {{
            enabled: true
          }}
        }};
        var network = new vis.Network(container, data, options);
      </script>
    </body>
    </html>
    """

    # Write the HTML content to the file
    with open(filename, 'w') as f:
        f.write(html_content)

    print(f"HTML visualization saved as {filename}")

# Example Usage
add_pc("PC1")
add_pc("PC2")
add_pc("PC3")
add_pc("PC4")

add_link("PC1", "PC2", 5)
add_link("PC2", "PC3", 3)

# Generate the HTML visualization
generate_vis_js_html()
