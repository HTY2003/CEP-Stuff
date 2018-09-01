from collections import defaultdict
import itertools

class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list) #dictionary containing adjacency list
        self.V = vertices #No. of vertices


    def addEdge(self,u,v):
        self.graph[u].append(v)

    def __str__(self):
        output = ""
        for vertex, connectedto in self.graph.items():
            output += str(vertex) + ":" + str(connectedto) + "\n"
        return output

    def topsort(self):
        anslist, sortlist = [], {}
        for i in list(set([i[0] for i in self.graph.items()] + list(itertools.chain.from_iterable(list(i[1] for i in self.graph.items()))))): sortlist[i] = 0
        for x in list(itertools.chain.from_iterable(list(i[1] for i in self.graph.items()))): sortlist[x] += 1
        while sum(sortlist.values()) > 0:
            for k, i in sortlist.items():
                if i == 0:
                    if k not in anslist: anslist.append(k)
                    for v in self.graph[k]: sortlist[v] -= 1
            for i in set(anslist).intersection(set(sortlist.keys())): del sortlist[i]
        return anslist + list(sortlist.keys())

if __name__ == "__main__":
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    print(g) #print out the adjacency list
    print(g.topsort())
