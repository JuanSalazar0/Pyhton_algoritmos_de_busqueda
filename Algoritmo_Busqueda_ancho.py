import networkx as nx 
import matplotlib.pyplot as plt

def busqueda_ancho(V,E,raiz):
    V = sorted(V)

    if raiz in V:
        S = [raiz]
        v = [raiz]
    else:
        print("El nodo raiz no existe, por favor ingresa un nodo raiz valido")
        return 0
    e = []

    
    while True:
        son = []
        aristas = False
        for x in S:
            for y in set(V)-set(v):
                if (x,y) in E:
                    e.append((x,y))
                    v.append(y)
                    aristas = True
                    son.append(y)
        if not aristas:
            return v,e
        S = son


if __name__== "__main__":

    G = nx.Graph([("a","b"),("a","c"),("a","g"),
                ("b","d"),("b","g"),
                ("d","f"),
                ("c","d"),("c","e"),
                ("e","f"),("e","g"),
                ("f","h")])

    v,e = busqueda_ancho(G.nodes,G.edges,"a")
    print(v)
    print(e)
