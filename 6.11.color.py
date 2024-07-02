def color(e, n, k):
     graph = [[] for _ in range(n)]
     for u, v in e:
        graph[u].append(v)
        graph[v].append(u)
     c  = {}
     a  = set(range(k))

     for r  in range(n):
        if r  not in c :
             a  = {c [adj] for adj in graph[r ] if adj in c }
             for color in range(k):
                if color not in a :
                    c [r ] = color
                    a .discard(color)
                    break
     return c 
e  = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
n = 4   
k = 3   
result = color(e , n, k)
print("Coloring:", result)