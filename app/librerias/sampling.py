from graph import graph_from_file, add_graph 
from random import random, sample
import networkx as nx


def get_node_from_list(nodes):
	# s = sample(nodes, 1)
	# print s	
	return sample(nodes, 1)[0]

def random_walk(sample_size, fly_back_probability=0.15, graph=None, file_path=None):
	
	

	# Step 1: Initialization

	sample = nx.DiGraph()
	add_node_to_sample = sample.add_node
	add_edge_to_sample = sample.add_edge

	# Check if a file path was supplied.
	if file_path is not None:
		graph = graph_from_file(file_path) 	# Networkx object.

	# Check for a list of edges(source_node, destination_node, weight).
	elif graph is not None:
		graph = add_graph(file_path)		# Networkx object.

	
	nodes = graph.nodes()					# List of nodes
	nodes_size = graph.number_of_nodes() 	# Number of nodes

	# Step 2: Select a random node to be the starting point.
	starting_node = get_node_from_list(nodes)

	add_node_to_sample(starting_node) 		# Include this node in the sample.

	# Step 3: Random walking
	current_node = starting_node 			# Set the starting point for the random walk.
	steps_since_added_node = 0

	while sample.number_of_nodes() < sample_size:
		
		# Check if we're going to look for a neighbor or we're flying back to the initial node.
		walk_to_neighbor = random()

		if walk_to_neighbor > fly_back_probability:
			# Walk to a neighbor.

			# IMPORTANT: Only selects from outer edges
			neighbors = graph.neighbors(current_node)			# Get the list of neighbors. 
			selected_neighbor = get_node_from_list(neighbors)	# Choose one of the neighbors at random.
			add_edge_to_sample(current_node, selected_neighbor)	# Add the edge to the graph, it also adds the node.
			current_node = selected_neighbor					# Let's change the current node to the selected neighbor.
			steps_since_added_node = 0

		else:
			steps_since_added_node = steps_since_added_node + 1
			# Change starting point if steps since last added node if greater the limit.
			if(steps_since_added_node > 100):
				starting_node = get_node_from_list(nodes)

			current_node = starting_node 	# Fly back to the starting node.

	return sample 		# Networkx object.

		


