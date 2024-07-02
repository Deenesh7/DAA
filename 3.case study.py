class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
  
    def pagerank(self, damping_factor=0.85, max_iterations=100,    convergence_threshold=0.0001):
        nodes = list(self.graph.keys())
        N = len(nodes)
        pr = {node: 1 / N for node in nodes}
        out_degree = {node: len(self.graph[node]) for node in nodes}

        def incoming_neighbors(node):
            neighbors = []
            for u in self.graph:
                if node in self.graph[u]:
                    neighbors.append(u)
            return neighbors

        def converge(new_pr, old_pr, threshold):
            for node in new_pr:
                if abs(new_pr[node] - old_pr[node]) >= threshold:
                    return False
            return True

        for _ in range(max_iterations):
            new_pr = {}
            for node in nodes:
                new_rank = (1 - damping_factor) / N
                for neighbor in incoming_neighbors(node):
                    new_rank += damping_factor * pr[neighbor] / out_degree[neighbor]
                new_pr[node] = new_rank

            if converge(new_pr, pr, convergence_threshold):
                break

            pr = new_pr

        return pr
g = Graph()
g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.add_edge('C', 'A')
g.add_edge('D', 'A')
g.add_edge('D', 'C')

pagerank_scores = g.pagerank()
print("PageRank scores:", pagerank_scores)
