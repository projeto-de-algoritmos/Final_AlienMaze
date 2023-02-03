from heapq import *
import constants as con
import math

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

def dist(p1, p2):
    return math.sqrt(((p2[1]-p1[1])**2)+((p2[0]-p1[0])**2))


def closest_brute_force(points):
    min_dist = float("inf")
    p1 = None
    p2 = None
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            d = dist(points[i], points[j])
            if d < min_dist:
                min_dist = d
                p1 = points[i]
                p2 = points[j]
    return p1, p2, min_dist


def rec(xsorted, ysorted):
    n = len(xsorted)
    # Usar força bruta, pois são poucos pontos
    if n <= 3:
        return closest_brute_force(xsorted)
    else:
        # Encontrar o ponto médio
        midpoint = xsorted[n//2]
        # Dividir pontos eixo x
        xsorted_left = xsorted[:n//2]
        xsorted_right = xsorted[n//2:]
        ysorted_left = []
        ysorted_right = []
        # Dividir eixo y comparando pelo ponto médio achado
        for point in ysorted:
            ysorted_left.append(point) if (
                point[0] <= midpoint[0]) else ysorted_right.append(point)
		# Encontrar os par mais próximo na parte esquerda(delta-left)
        (p1_left, p2_left, delta_left) = rec(xsorted_left, ysorted_left)
		# Encontrar os par mais próximo na parte direita(delta-right)
        (p1_right, p2_right, delta_right) = rec(xsorted_right, ysorted_right)
		# Encontrar a menor distância possível entre pontos no plano dividido(delta)
        (p1, p2, delta) = (p1_left, p2_left, delta_left) if (delta_left < delta_right) else (p1_right, p2_right, delta_right)
        # Encontrar pontos que podem estar em diferentes planos, na faixa da menor distância
        in_band = [point for point in ysorted if midpoint[0] -
                   delta < point[0] < midpoint[0]+delta]
		# Para cada ponto encontrado na faixa, substituir se a distância for menor do que delta
        for i in range(len(in_band)):
            for j in range(i+1, min(i+7, len(in_band))):
                d = dist(in_band[i], in_band[j])
                if d < delta:
                    print(in_band[i], in_band[j])
                    (p1, p2, delta) = (in_band[i], in_band[j], d)
        return p1, p2, delta


def closest(points):
    # Ordenar para facilitar na hora de achar o ponto médio
    xsorted = sorted(points, key=lambda point: point[0])
    ysorted = sorted(points, key=lambda point: point[1])
    return rec(xsorted, ysorted)
