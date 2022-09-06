import networkx as nx
import matplotlib.pyplot as plt

class Vertice:
    def __init__(self, i):
        self.id = i
        self.vecinos = []
        self.nivel = -1
        self.visitado = False
        self.anterior = None

    def agrVecino(self, v):
        if v not in self.vecinos:
            self.vecinos.append(v)
            self.vecinos.sort()


class Grafo:
    def __init__(self):
        self.vertices = {} #Se crea un diccionario donde más adelante se van a guardar objetos tipo Vertice

    def agrVertice(self,id):
        if id not in self.vertices:
            self.vertices[id] = Vertice(id) #Se guarda un objeto tipo vertice con su id correspondiente

    def agrArista(self, a, b):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agrVecino(b) #Agrega el vecino 'b' en el diccionario con el id 'a'
            self.vertices[b].agrVecino(a)

    def busq_prof(self, raiz):
        if raiz in self.vertices:
            vp = [raiz]
            w = raiz
            self.vertices[raiz].visitado = True
            print("Raíz: " + str(raiz))
        else:
            print("El nodo raiz no existe.")
            return 0
        ep = []
        lista = list(self.vertices.keys())
        while True:
            for vert in self.vertices[w].vecinos:
                while self.vertices[vert].visitado == False:
                    ep.append((w, vert))
                    vp.append(vert)
                    self.vertices[vert].visitado = True
                    self.vertices[vert].anterior = w
                    w= vert
                    print("Vertice: " + str(vert) + " Padre: " + str(self.vertices[vert].anterior))
                    lista.remove(vert)

            if len(lista) == 1:
                return ep,vp

g = Grafo()

g.agrVertice('A') 
g.agrVertice('B') 
g.agrVertice('C') 
g.agrVertice('D') 
g.agrVertice('E')
g.agrVertice('F') 
g.agrVertice('G') 
g.agrVertice('H')
g.agrVertice('I')
g.agrArista('A', 'B')
g.agrArista('A', 'D')
g.agrArista('A', 'G')
g.agrArista('B', 'C')
g.agrArista('B', 'H')
g.agrArista('B', 'E')
g.agrArista('C', 'H')
g.agrArista('D', 'E')
g.agrArista('E', 'F')
g.agrArista('F', 'G')
g.agrArista('F', 'I')
g.agrArista('G', 'I')
g.agrArista('G', 'H')
g.agrArista('H', 'I')

ep,vp = g.busq_prof('C')

G = nx.Graph([('A', 'B'),('A', 'D'),('A', 'G'),('B', 'C'),('B', 'H'),
                ('B', 'E'),('C', 'H'),('D', 'E'),('E', 'F'),
                ('F', 'G'), ('F', 'I'),('G', 'I'),('G', 'H'),('H', 'I')])
nx.draw(G,with_labels=True,font_color='white')
plt.show()

G2 = nx.DiGraph(ep)
nx.draw(G2,with_labels=True,font_color='white')
plt.show()