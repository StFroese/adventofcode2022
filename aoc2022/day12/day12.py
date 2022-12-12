from tqdm import tqdm

def read_input():
    g = Graph()
    with open('input.txt', 'r') as f:
        grid = [''.join([chr(ord('z')+1) if char == 'E' else char for char in row]) for row in f.read().split('\n')[:-1]]
        for row_idx, row in enumerate(grid):
            for col_idx, char in enumerate(row):
                g.add_node((row_idx,col_idx))

                unicode = ord(char) - ord('a')
                if unicode == (ord('z') - ord('a') + 1):
                    g.end = (row_idx, col_idx)
                if unicode == ord('S') - ord('a'):
                    g.start = (row_idx, col_idx)
                    unicode = 0
                g.add_unicode((row_idx,col_idx), unicode)
                # calc connections left right upper lower
                for con in check_nearest(grid, row_idx, col_idx, unicode):
                    g.add_edge((row_idx, col_idx), con)
    return g

def test_input():
    g = Graph()
    with open('test_input.txt', 'r') as f:
        grid = [''.join([chr(ord('z')+1) if char == 'E' else char for char in row]) for row in f.read().split('\n')[:-1]]
        for row_idx, row in enumerate(grid):
            for col_idx, char in enumerate(row):
                g.add_node((row_idx,col_idx))

                unicode = ord(char) - ord('a')
                if unicode == (ord('z') - ord('a') + 1):
                    g.end = (row_idx, col_idx)
                if unicode == ord('S') - ord('a'):
                    g.start = (row_idx, col_idx)
                    unicode = 0
                g.add_unicode((row_idx,col_idx), unicode)
                # calc connections left right upper lower
                for con in check_nearest(grid, row_idx, col_idx, unicode):
                    g.add_edge((row_idx, col_idx), con)
    return g

def check_nearest(grid, row_idx, col_idx, height):
    connections = []
    # check left
    if col_idx != 0 and (ord(grid[row_idx][col_idx-1]) - ord('a')) - height <= 1:
        connections.append((row_idx, col_idx-1))
    # check right
    if col_idx != len(grid[row_idx]) - 1 and (ord(grid[row_idx][col_idx+1]) - ord('a')) - height <= 1:
        connections.append((row_idx, col_idx+1))
    # check upper
    if row_idx != 0 and (ord(grid[row_idx-1][col_idx]) - ord('a')) - height <= 1:
        connections.append((row_idx-1, col_idx))
    # check lower
    if row_idx != len(grid) - 1 and (ord(grid[row_idx+1][col_idx]) - ord('a')) - height <= 1:
        connections.append((row_idx+1, col_idx))

    return connections

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = {}
        self.start = None
        self.end = None
        self.unicode = {}

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, from_node, to_node):
        if from_node not in self.edges:
            self.edges[from_node] = [to_node]
        else:
            self.edges[from_node].append(to_node)

    def add_unicode(self, node, unicode):
        self.unicode[node] = unicode

    def starting_points_part_two(self):
        return [node for node in self.nodes if self.unicode[node] == 0]

class Dijkstra:
    def __init__(self, graph):
        self.graph = graph
        self.distance = {node: float('inf') for node in graph.nodes}
        self.distance[graph.start] = 0
        self.parent = {node: None for node in graph.nodes}

    def __call__(self):
        nodes = self.graph.nodes.copy()

        while len(nodes) != 0:
            node_sd = self._smallest_distance_node(nodes)
            nodes.remove(node_sd)
            if node_sd == self.graph.end:
                break
            if node_sd in self.graph.edges.keys():
                for connection in self.graph.edges[node_sd]:
                    if connection in nodes:
                        self._update_distance(node_sd, connection)

    def _smallest_distance_node(self, nodes):
        smallest_distance = min([self.distance[node] for node in nodes])
        node_with_sd = [node for node in nodes if self.distance[node] == smallest_distance][0]
        return node_with_sd

    def _update_distance(self, from_node, to_node):
        # distance between two nodes is always 1
        alternative = self.distance[from_node] + 1
        if alternative < self.distance[to_node]:
            self.distance[to_node] = alternative
            self.parent[to_node] = from_node

    def shortest_path(self):
        path = [self.graph.end]
        node = self.graph.end
        while node in self.parent.keys():
            node = self.parent[node]
            path.append(node)

        return path

def main():
    graph = read_input()

    # part 1
    dijkstra = Dijkstra(graph)
    dijkstra()
    print(len(dijkstra.shortest_path())-2)

    # part 2
    starting_points = graph.starting_points_part_two()
    distances = []
    for start in tqdm(starting_points):
        graph.start = start
        dijkstra = Dijkstra(graph)
        dijkstra()
        distance = len(dijkstra.shortest_path())-2
        if distance != 0:
            distances.append(distance)
    print(min(distances))



if __name__ == '__main__':
    main()
