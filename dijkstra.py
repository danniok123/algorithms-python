# Dijkstra Algorithm

import sys
import math
import heapq
from collections import defaultdict

# Graph Class from https://gist.github.com/econchick/4666413
class Graph:
	def __init__(self):
		self.nodes = set()
		self.edges = defaultdict(list)
		self.dist = {}

	def add_node(self, val):
		self.nodes.add(val)

	# Directed Graph
	def add_edge(self, from_v, to_v, dist):
		self.edges[from_v].append(to_v)
		self.dist[(from_v, to_v)] = dist


# Adapted implementation from the pseudocode in https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
def dijkstra(graph, source):
	Q = set()

	# for each v in graph
	dist = {x : math.inf for x in graph.nodes} # unknown distance
	prev = {x : None for x in graph.nodes} # undefined

	dist[source] = 0

	while Q != graph.nodes:
		u = min(set(dist.keys()) - Q)

		for neigh_v in set(graph.edges[u]):
			alt = dist[u] + graph.dist[u, neigh_v]

			if alt < dist[neigh_v]:
				dist[neigh_v] = alt
				prev[neigh_v] = u

		Q.add(u)

	return (dist, prev)

def path(graph, source, target):
	dist, prev = dijkstra(graph, source)

	if dist[target] == math.inf:
		print('No path between %s and %s' % (source, target))
	else:
		path = []
		node = target
		while node is not None:
			path.append(node)
			node = prev[node]
		path.reverse()
		print('The shortest path between %s and %s is ' % (source, target) + '->'.join(path) )

# Used example from CLRS (Intro to Algo)
if __name__ == '__main__':

	g = Graph()

	g.add_node('s')
	g.add_node('t')
	g.add_node('x')
	g.add_node('y')
	g.add_node('z')

	g.add_edge('s', 't', 10)
	g.add_edge('s', 'y', 5)
	g.add_edge('t', 'y', 2)
	g.add_edge('t', 'x', 1)
	g.add_edge('y', 't', 3)
	g.add_edge('y', 'z', 2)
	g.add_edge('y', 'x', 9)
	g.add_edge('z', 's', 7)
	g.add_edge('z', 'x', 6)
	g.add_edge('x', 'z', 4)

	path(g, 's', 'x')