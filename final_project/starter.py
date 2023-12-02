# creates adjancy list given a file name
# Ex. Input 
# A -> [(B,5),(C,7)]
# B -> [(C,7),(A,10)] // store it as a list of lists. 
# Returns list of list containing the graph
import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
    def add_edge(self,start,end,distance):
        self.edges[start].append((end,distance))
        self.edges[end].append((start,distance))
    def add_node(self,node):
        if node not in self.nodes:
            self.nodes.add(node)
            self.edges[node]=[]  
    def get_cities(self):
        return self.nodes   
    def get_graph(self):
        return self.edges

def create_graph(file):
    graph = Graph()
    with open(file) as f:
        next(f)
        for line in f:
            start, end, distance = line.split(",")
            graph.add_node(start.strip())
            graph.add_node(end.strip())
            graph.add_edge(start.strip(), end.strip() ,distance.strip())
    return graph
# run dijikstras algorithm passing the graph from create_graph and the starter, end location. 
def dijikstras(graph, start, end):
    queue = [(0,start,[])]
    visited= set()
    while queue:
        if not queue:
            print("FAIL: NO PATH")
            return
        next_city = heapq.heappop(queue)
        if next_city[1] == end:
            return (next_city[0], next_city[2] + [next_city[1]])
        visited.add(next_city[1])
        for city in graph[next_city[1]]:
            if city[0] not in visited:
                print(city)
                print(next_city)
                heapq.heappush(queue, (next_city[0] + int(city[1]), city[0], next_city[2] + [next_city[1]]))
    return

if __name__ == "__main__":
    # here you will create the graph first, then prompt the user for start and end 
    # and then give them the shortest path   
    graph_ = create_graph("cities.csv")
    cities = graph_.get_cities()
    graph = graph_.get_graph()
    print(graph)
    user_start=input("Enter starting city: ")
    user_end=input("Enter Ending City: ")
    print(dijikstras(graph, user_start, user_end))
    # print(graph[user_start]) example of how to go into dictionary

    #user_start=input("Enter Starting City: ")
    #user_end=input("Enter Ending City: ")
    #shortest_path=input("The fastest way to reach your destination is through   ")
    #Queue : Input : A, B, C / Output: A, B, C PQ: Input: A, 830 . B, 730 . C, 300 / C, 300 . B, 730 A, 830
