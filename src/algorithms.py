from heapq import *
import constants as con

def manhattanDistance(a, b):
	# Distância de Manhattan para o A*
   return abs(a[0] - b[0]) + abs(a[1] - b[1])

def checkNeighbours(grid, x, y):
	# Check para não pegar quadrados fora do limite da tela
    limits = lambda x, y: True if 0 <= x < (con.TILES_VERTICAL) and 0 <= y < (con.TILES_HORIZONTAL) else False

	# Possíveis vizinhos (excluindo diagonais)
    neighbours = [-1, 0], [0, -1], [1, 0], [0, 1]

	# Retornando o par de custo para mover para cada vizinho (custo, (x, y))
    return [(grid[x + dx][y + dy], (x + dx, y + dy)) for dx, dy in neighbours if limits(x + dx, y + dy)]

def aStar(start, end, cells):
	queue = []
	grid = cells.grid
	heappush(queue, (0, start))
	cost_visited = {start: 0}
	visited = {start: None}

	global graph
	graph = {}
	
	# Mapeando cada nó com seus vizinhos e custos pro A*
	for y, row in enumerate(grid):
		for x, col in enumerate(row):
			graph[(x, y)] = graph.get((x, y), []) + checkNeighbours(grid, x, y)
	
	# Algoritmo A*
	while queue:
		cur_cost, cur_node = heappop(queue)
		if cur_node == end:
			break

		neighbours = graph[cur_node]
		for neighbour in neighbours:
			neigh_cost, neigh_node = neighbour
			new_cost = cost_visited[cur_node] + neigh_cost

			if neigh_node not in cost_visited or new_cost < cost_visited[neigh_node]:
				# A* priorização pro heap
				priority = new_cost + manhattanDistance(neigh_node, end)
				heappush(queue, (priority, neigh_node))
				cost_visited[neigh_node] = new_cost
				visited[neigh_node] = cur_node

	reversePath = []
	reverseAnswer = []

	cur_node = end
	reversePath.append(cur_node)
	reverseAnswer.append(cells.matrix[cur_node[0]][cur_node[1]])
	
	# Encontrando solução
	while cur_node != start:
		cur_node = visited[cur_node]
		reversePath.append(cur_node)
		reverseAnswer.append(cells.matrix[cur_node[0]][cur_node[1]])

	path = list(reversed(reversePath))
	# print(path)

	answer = list(reversed(reverseAnswer))
	return answer