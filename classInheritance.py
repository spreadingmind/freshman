'''This is a class for modelling class inheritance. The task was provided by Stepik Python Basics and Implementation course.
Task description: В первой строке входных данных содержится целое число n - число классов.

В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется i-й класс.
 Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется сам от себя
 (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.
В следующей строке содержится число q - количество запросов.
В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.

Input:
4
A
B : A
C : A
D : B C
4
A B
B D 
C D
D A
Output:
Yes
Yes 
Yes 
No

'''
____________________________________________________________________________________________________________________
class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []
 
    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.graph_dict:
            self.graph_dict[vertex1].append(vertex2)
        else:
            self.graph_dict[vertex1] = [vertex2]

    def generate_edges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self.graph_dict:
            for neighbour in self.graph_dict[vertex]:
                if (neighbour, vertex) not in edges:
                    edges.append((vertex, neighbour))
                    
        for pair in edges:
            for otherpair in edges:
                if pair[1] == otherpair[0]:
                    edges.append((pair[0],otherpair[1]))
        return edges

n = int(input())  
inp = [input() for i in range(n)]
g = {i.split()[0] : i.split()[2:] for i in inp }
#g = {'c': ['a'], 'b': ['a'], 'd': ['b', 'c'], 'a': []}

graph = Graph(g)
          
print (g)

print("Nodes of graph:")
print(graph.vertices())

print("Edges of graph:")
print(graph.edges())

n2  = int(input())
inp2 = [input() for i in range(n2)]
queryList = [(i.split()[1],i.split()[0]) for i in inp2]
#queryList = [('a', "a"), ('b', 'a'),('d', 'b'),('d','c'), ('a', 'd')]
print (queryList)

def isinherence(query):
        for pair in query:
            if pair in graph.edges():
                print ('Yes')
            elif pair[1] == pair[0]:
                print ("Yes") 
            
            else:
                print ('No')
    
isinherence(queryList)

