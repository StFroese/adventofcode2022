from tqdm import tqdm

def read_input(test=False):
    file = "test_input.txt" if test else "input.txt"
    g = Graph()
    with open(file, "r") as f:
        for line in f.read().split('\n')[:-1]:
            words = line.split(' ')
            g.add_node(words[1], int(words[4][5:-1]))
            to_nodes = list(map(lambda x: x[:-1] if x[-1]==',' else x,words[9:]))
            for to_node in to_nodes:
                g.add_edge(words[1], to_node)
    return g

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = {}
        self.rates = {}

    def add_node(self, node, rate):
        self.nodes.append(node)
        self.rates[node] = rate

    def add_edge(self, from_node, to_node):
        if from_node in self.edges:
            self.edges[from_node].append(to_node)
        else:
            self.edges[from_node] = [to_node]




def bfs(graph, start, rates):
    q = []
    distances = {}
    explored = [start]
    q.append(start)
    distances[start] = 0
    while q:
        node = q.pop(0)
        for edge in graph.edges[node]:
            if edge not in explored:
                explored.append(edge)
                q.append(edge)
                distances[edge] = distances[node] + 1
    return distances

def paths_in_time(distances, time, rates):
    # this is DFS??? I guess
    pressures = []
    paths = []
    q = []
    minutes = []
    pressure = []
    q.append(['AA'])
    minutes.append(time)
    pressure.append(0)
    while q:
        path = q.pop()
        node = path[-1]
        minute = minutes.pop()
        pres = pressure.pop()
        end = False
        for edge in distances[node]:
            dist = distances[node][edge]
            # + 1 to open valve
            if dist + 1 > minute or edge in path or rates[edge] == 0: # don't look at zero flow valves
                end = True
                continue
            end = False
            minutes.append(minute - dist - 1) # -1 to open valve
            pressure.append(pres + minutes[-1] * rates[edge])
            q.append(path + [edge])
        if end:
            paths.append(path)
            pressures.append(pres)
    return pressures, paths


def main():
    graph = read_input(test=False)

    # part 1
    # let's think about this again
    # we can decide to find every path in 30 minutes and choose the one with the maximum pressure / DFS
    # -> this will take long because of all combinations

    # better approach:
    # calculate the minute distance from each node to each node
    # calculate all pressures in that can be obtained in time
    # -> build a complete graph with distances/minutes

    # first calculate distance from each to each -> use BFS for this??
    distances = {}
    for from_node in graph.nodes:
        distances[from_node] = {}
        distance_nodes = bfs(graph, from_node, graph.rates)
        for to_node in distance_nodes:
            if to_node != from_node:
                distances[from_node][to_node] = distance_nodes[to_node]
    # we have the distances from each node to each node now. nice. what next??
    # calculate all paths that can be reached in time
    # works on test but is slow in input -> remove valves thats have zero flow!
    pressures, paths = paths_in_time(distances, 30, graph.rates)
    print(max(pressures))
    print(len(paths))

    # part 2
    # comparing each path would take O(N**2) -> slow
    # let's do this: sort paths by pressure. Since I will open the best suitable valves,
    # the elephant will have a lower pressure number. 
    my_pressures, my_paths = paths_in_time(distances, 26, graph.rates)
    combined = []
    for idx, path in tqdm(enumerate(my_paths)):
        for el_idx, el_path in enumerate(my_paths):
            if set(path).intersection(set(el_path)) == {'AA'}:
                combined.append(my_pressures[idx]+my_pressures[el_idx])

    print(max(combined))

if __name__ == "__main__":
    main()
