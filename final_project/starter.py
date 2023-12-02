# creates adjancy list given a file name
# Ex. Input 
# A -> [(B,5),(C,7)]
# B -> [(C,7),(A,10)] // store it as a list of lists. 
# Returns list of list containing the graph
class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
    def add_edge(self,start,end,distance):
        self.edges[start].append((end,distance))
        self.edges[end].append((start,distance))
    def add_node(self,node):
        self.nodes.add(node)
        self.edges[node]=[]  
    def print_graph(self):
        print(self.edges)
    def print_cities(self):
        print(self.nodes)      

def create_graph(file):
    graph = Graph()
    with open(file) as f:
        next(f)
        for line in f:
            start, end, distance = line.split(",")
            graph.add_node(start.strip())
            graph.add_node(end.strip())
            graph.add_edge(start.strip(),end.strip(),distance.strip())

    return graph
# run dijikstras algorithm passing the graph from create_graph and the starter, end location. 
def dijikstras(graph, start, end):
    return

if __name__ == "__main__":
    # here you will create the graph first, then prompt the user for start and end 
    # and then give them the shortest path   
    graph = create_graph("cities.csv")
    graph.print_cities()
#user_start=input("Enter starting city: ")
user_start=input("Enter Starting City: ")
user_end=input("Enter Ending City: ")
shortest_path=input("The fastest way to reach your destination is through   ")
