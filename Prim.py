def prim(w,n,s):
    v=[]
    while(len(v) != n):
        v.append (0)
    v[s] = 1
    suma= 0
    E = []
    for i in range(0,n-1):
        minimo = 20
        agregar_vertice = 0
        e =[]
        for j in range(0,n):
            if(v[j] == 1):
                for k in range(0,n):
       
                    if(v[k]==0 and w[j][k] < minimo):
                        agregar_vertice = k
                        e = [j,k]
                        minimo = w[j][k]
        suma += w[e[0]][e[1]] 
        v[agregar_vertice] = 1
        E.append (e)
                            
    return [E, suma]

n=9
s=0
    #0  1  2  3  4  5 6  7  8
w =[#A, B, C, D, E, F,G, H, I #20 == no
    [20,6,20,10,20,20,8,20,20],#A
    [6,20,11,20,15,20,20,13,20],#B
    [20,11,20,20,20,20,20,4,20],#C
    [10,20,20,20,6,20,20,20,20],#D
    [20,15,20,6,20,2,20,20,20],#E
    [20,20,20,20,2,20,4,20,6],#F
    [8,20,20,20,20,4,20,5,5],#G
    [20,13,4,20,20,20,5,20,7],#H
    [20,20,20,20,20,6,5,7,20]]#I


print(prim(w,n,s))