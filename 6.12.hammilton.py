class Graph(): 
    def __init__(self, vertices): 
        self.graph = [[0 for column in range(vertices)]
                            for row in range(vertices)] 
        self.V = vertices 

    def isSafe(self, v, pos, path): 
        if self.graph[path[pos-1]][v] == 0: 
            return False

        for vertex in path: 
            if vertex == v: 
                return False

        return True

    def hamCycleUtil(self, path, pos): 
        if pos == self.V: 
            if self.graph[path[pos-1]][path[0]] == 1: 
                return True
            else: 
                return False

        for v in range(1, self.V): 
            if self.isSafe(v, pos, path): 
                path[pos] = v 
                if self.hamCycleUtil(path, pos+1): 
                    return True
                path[pos] = -1

        return False

    def hamCycle(self): 
        path = [-1] * self.V 
        path[0] = 0

        if not self.hamCycleUtil(path, 1): 
            print("Solution does not exist\n")
            return False

        self.printSolution(path) 
        return True

    def printSolution(self, path): 
        print("Solution Exists: Following is one Hamiltonian Cycle")
        for vertex in path: 
           print(vertex)

# Example 1
g1 = Graph(5) 
g1.graph = [[0, 1, 0, 1, 0],
            [1, 0, 1, 1, 1],
            [0, 1, 0, 0, 1],
            [1, 1, 0, 0, 1],
            [0, 1, 1, 1, 0]]

g1.hamCycle()

# Example 2
g2 = Graph(5) 
g2.graph = [[0, 1, 0, 1, 0],
            [1, 0, 1, 1, 1],
            [0, 1, 0, 0, 1],
            [1, 1, 0, 0, 0],
            [0, 1, 1, 0, 0]]

g2.hamCycle()
