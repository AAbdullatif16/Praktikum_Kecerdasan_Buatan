# -*- coding: utf-8 -*-
"""Selamat Datang di Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb
"""

#2106145_A.Abdul Latif-BFS

def bfs(graph, source):
    visited = set() 
    bfs_traversal = list()
    queue = list()

    queue.append(source)
    visited.add(source)

    while queue:
        current_node = queue.pop(0)
        bfs_traversal.append(current_node)
        for neighbour_node in graph[current_node]:
            if neighbour_node not in visited:
                visited.add(neighbour_node)
                queue.append(neighbour_node)
    return bfs_traversal

def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F', 'G'],
        'D': ['B'],
        'E': ['B'],
        'F': ['C'],
        'G': ['C']
    }

    bfs_traversal = bfs(graph, 'A')
    print(f"BFS: {bfs_traversal}")

if __name__=='__main__':
    main()

#2106145_A.Abdul Latif-DFS

def dfs(graph, source, visited, dfs_traversal):
    if source not in visited:
        dfs_traversal.append(source)
        visited.add(source)

        for neighbour_node in graph[source]:
            dfs (graph, neighbour_node, visited, dfs_traversal)   

    return dfs_traversal

def main():
    visited = set()
    dfs_traversal = list()

    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': [],
        'E': [],
        'F': [],
        'G': []
    }

    print(f"DFS: {dfs(graph, 'A', visited, dfs_traversal)}")

if __name__=="__main__":
    main()

#2106145_A.Abdul Latif-UCS
#returns the minimum cost in a vektor( if there are multiple goal states)
def uniform_cost_search(goal, start):

	# minimum cost upto
	# goal state from starting
	global graph,cost
	answer = []

	# create a priority queue
	queue = []

	# set the answer vector to max value
	for i in range(len(goal)):
		answer.append(10**8)

	# insert the starting index
	queue.append([0, start])

	# map to store visited node
	visited = {}

	# count
	count = 0

	# while the queue is not empty
	while (len(queue) > 0):

		# get the top element of the
		queue = sorted(queue)
		p = queue[-1]

		# pop the element
		del queue[-1]

		# get the original value
		p[0] *= -1

		# check if the element is part of
		# the goal list
		if (p[1] in goal):

			# get the position
			index = goal.index(p[1])

			# if a new goal is reached
			if (answer[index] == 10**8):
				count += 1

			# if the cost is less
			if (answer[index] > p[0]):
				answer[index] = p[0]

			# pop the element
			del queue[-1]

			queue = sorted(queue)
			if (count == len(goal)):
				return answer

		# check for the non visited nodes
		# which are adjacent to present node
		if (p[1] not in visited):
			for i in range(len(graph[p[1]])):

				# value is multiplied by -1 so that
				# least priority is at the top
				queue.append( [(p[0] + cost[(p[1], graph[p[1]][i])])* -1, graph[p[1]][i]])

		# mark as visited
		visited[p[1]] = 1

	return answer

# main function
if __name__ == '__main__':

	# create the graph
	graph,cost = [[] for i in range(8)],{}

	# add edge
	graph[0].append(1)
	graph[0].append(3)
	graph[3].append(1)
	graph[3].append(6)
	graph[3].append(4)
	graph[1].append(6)
	graph[4].append(2)
	graph[4].append(5)
	graph[2].append(1)
	graph[5].append(2)
	graph[5].append(6)
	graph[6].append(4)

	# add the cost
	cost[(0, 1)] = 2
	cost[(0, 3)] = 5
	cost[(1, 6)] = 1
	cost[(3, 1)] = 5
	cost[(3, 6)] = 6
	cost[(3, 4)] = 2
	cost[(2, 1)] = 4
	cost[(4, 2)] = 4
	cost[(4, 5)] = 3
	cost[(5, 2)] = 6
	cost[(5, 6)] = 3
	cost[(6, 4)] = 7

	# goal state
	goal = []

	# set the goal
	# there can be multiple goal states
	goal.append(6)

	# get the answer
	answer = uniform_cost_search(goal, 0)

	# print the answer
	print("Minimum cost from 0 to 6 is = ",answer[0])

#2106145_A.Abdul Latif-IDDFS
# python program to print DFS traversal from a given
# given graph

from collections import defaultdict

# This class represents a directed graph using adjacency
# list representation

class Graph:
    def __init__ (self, vertices):

        # Ho. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u]. append(v)


    # A function to perform a Depth-Linited search
    # from given source "src’
    def DLS (self, src, target, maxDepth):

        if src == target : return True

        # IF reached the maximum depth, stop recursing.
        if maxDepth <= 0 : return False

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[src]:
            if (self.DLS(i, target, maxDepth-1)):
                return True
        return False

    # TODFS to search if target is reachable from v.
    # It uses recursive DLS()
    def IDDFS(self, src, target, maxDepth):

        # Repeatedly depth-linit search till the
        # maximum depth
        for i in range(maxDepth):
            if (self.DLS(src, target, i)):
                return True
        return False

# Create a graph given in the above diagram
g = Graph (7);
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 4)
g.addEdge(1, 3)
g.addEdge(1, 5)
g.addEdge(2, 6)

target = 6; maxDepth = 3; src = 0

if g.IDDFS(src, target, maxDepth) == True:
    print ("Target is reachable from source " +
           "within max depth")
else :
    print ("Target is NOT reachable from source " +
           "within max depth")

#2106145_A.Abdul Latif-BS
# Python3 program for Bidirectional BFS
# Search to check path between two vertices

# Class definition for node to
# be added to graph
class AdjacentNode:

	def __init__(self, vertex):

		self.vertex = vertex
		self.next = None

# BidirectionalSearch implementation
class BidirectionalSearch:

	def __init__(self, vertices):

		# Initialize vertices and
		# graph with vertices
		self.vertices = vertices
		self.graph = [None] * self.vertices

		# Initializing queue for forward
		# and backward search
		self.src_queue = list()
		self.dest_queue = list()

		# Initializing source and
		# destination visited nodes as False
		self.src_visited = [False] * self.vertices
		self.dest_visited = [False] * self.vertices

		# Initializing source and destination
		# parent nodes
		self.src_parent = [None] * self.vertices
		self.dest_parent = [None] * self.vertices

	# Function for adding undirected edge
	def add_edge(self, src, dest):

		# Add edges to graph

		# Add source to destination
		node = AdjacentNode(dest)
		node.next = self.graph[src]
		self.graph[src] = node

		# Since graph is undirected add
		# destination to source
		node = AdjacentNode(src)
		node.next = self.graph[dest]
		self.graph[dest] = node

	# Function for Breadth First Search
	def bfs(self, direction = 'forward'):

		if direction == 'forward':

			# BFS in forward direction
			current = self.src_queue.pop(0)
			connected_node = self.graph[current]

			while connected_node:
				vertex = connected_node.vertex

				if not self.src_visited[vertex]:
					self.src_queue.append(vertex)
					self.src_visited[vertex] = True
					self.src_parent[vertex] = current

				connected_node = connected_node.next
		else:

			# BFS in backward direction
			current = self.dest_queue.pop(0)
			connected_node = self.graph[current]

			while connected_node:
				vertex = connected_node.vertex

				if not self.dest_visited[vertex]:
					self.dest_queue.append(vertex)
					self.dest_visited[vertex] = True
					self.dest_parent[vertex] = current

				connected_node = connected_node.next

	# Check for intersecting vertex
	def is_intersecting(self):

		# Returns intersecting node
		# if present else -1
		for i in range(self.vertices):
			if (self.src_visited[i] and
				self.dest_visited[i]):
				return i

		return -1

	# Print the path from source to target
	def print_path(self, intersecting_node,
				src, dest):

		# Print final path from
		# source to destination
		path = list()
		path.append(intersecting_node)
		i = intersecting_node

		while i != src:
			path.append(self.src_parent[i])
			i = self.src_parent[i]

		path = path[::-1]
		i = intersecting_node

		while i != dest:
			path.append(self.dest_parent[i])
			i = self.dest_parent[i]

		print("*****Path*****")
		path = list(map(str, path))

		print(' '.join(path))

	# Function for bidirectional searching
	def bidirectional_search(self, src, dest):

		# Add source to queue and mark
		# visited as True and add its
		# parent as -1
		self.src_queue.append(src)
		self.src_visited[src] = True
		self.src_parent[src] = -1

		# Add destination to queue and
		# mark visited as True and add
		# its parent as -1
		self.dest_queue.append(dest)
		self.dest_visited[dest] = True
		self.dest_parent[dest] = -1

		while self.src_queue and self.dest_queue:

			# BFS in forward direction from
			# Source Vertex
			self.bfs(direction = 'forward')

			# BFS in reverse direction
			# from Destination Vertex
			self.bfs(direction = 'backward')

			# Check for intersecting vertex
			intersecting_node = self.is_intersecting()

			# If intersecting vertex exists
			# then path from source to
			# destination exists
			if intersecting_node != -1:
				print(f"Path exists between {src} and {dest}")
				print(f"Intersection at : {intersecting_node}")
				self.print_path(intersecting_node,
								src, dest)
				exit(0)
		return -1

# Driver code
if __name__ == '__main__':

	# Number of Vertices in graph
	n = 15

	# Source Vertex
	src = 0

	# Destination Vertex
	dest = 6

	# Create a graph
	graph = BidirectionalSearch(n)
	graph.add_edge(0, 4)
	graph.add_edge(1, 4)
	graph.add_edge(2, 5)
	graph.add_edge(3, 5)
	graph.add_edge(4, 6)
	graph.add_edge(5, 6)
	graph.add_edge(6, 7)
	graph.add_edge(7, 8)
	graph.add_edge(8, 9)
	graph.add_edge(8, 10)
	graph.add_edge(9, 11)
	graph.add_edge(9, 12)
	graph.add_edge(10, 13)
	graph.add_edge(10, 14)

	out = graph.bidirectional_search(src, dest)

	if out == -1:
		print(f"Path does not exist between {src} and {dest}")

#2106145_A.Abdul Latif_Tugas01
def blind_search(start, goal, graph):

    # Inisialisasi antrian dan himpunan node yang telah dikunjungi
    queue = [[start]]
    visited = set()

    # Lakukan pencarian jalur terpendek
    while queue:
        path = queue.pop(0)
        node = path[-1]

        # Jika simpul yang dikunjungi sama dengan simpul tujuan, kembalikan jalur
        if node == goal:
            return path

        # Tambahkan simpul yang bertetanggaan dengan simpul yang sedang dikunjungi ke antrian
        # jika simpul tersebut belum dikunjungi sebelumnya
        if node not in visited:
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

            visited.add(node)

    # Jika tidak ditemukan jalur, kembalikan None
    return None

# Contoh penggunaan program
graph = {
    0: [1, 3, 4],
    1: [0, 2, 3],
    2: [1, 3],
    3: [0, 1, 2, 4],
    4: [0, 3],
}

start = 0
goal = 2

result = blind_search(start, goal, graph)

# Cek apakah ditemukan jalur atau tidak
if result is None:
    print("Tidak ada jalur yang ditemukan.")
else:
    print("Jalur terpendek dari", start, "ke", goal, "adalah:", result)