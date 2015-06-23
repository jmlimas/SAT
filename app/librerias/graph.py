# from sys import argv
import networkx as nx


# Get parameters.
# script, graph_input = argv

def add_graph(graph_to_analyze, weight=False):
	# Load library.

	DG=nx.DiGraph()

	for line in graph_to_analyze:
		# Remove text nuances.
		line = line.strip()

		# Get the edge attributes.
		edge = line.split(",")
		
		# Get edge properties.
		source = edge[0]
		destination = edge[1]

		if weight: 
			peso = edge[2]
			# Add an edge to the networkx object.
			DG.add_edge(source, destination, weight=peso)
		else:
			DG.add_edge(source, destination)
	
	nodes = DG.nodes()

	# Get inedges and outedges.

	# DG.in_edges(nbunch=node, data=False)
	# DG.out_edges(nbunch=node, data=False)

	# For debugging purposes.

	print len(nodes), "nodos encontrados."
	print DG.number_of_edges(), "arcos encontrados."

	# Returns a networkx object with the graph loaded.
	return DG

def graph_from_file(file_path):

	# Let's read the file.
	with open(file_path, "r") as graph_file:

		# Read every line from file (edges).
		graph_to_analyze = graph_file.read()
		graph_to_analyze = graph_to_analyze.split("\n")
		
		# For debugging purposes.		
		# # Sample of graph loaded.
		# for i in range(3):
		# 	print "Linea", i, ":", graph_to_analyze[i]

		return add_graph(graph_to_analyze)

# graph_from_file(graph_input)