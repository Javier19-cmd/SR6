"""
Referencia: https://www.youtube.com/watch?v=IbzzK9PtFBE&ab_channel=ManuelGonzález
"""
a = [
    [1, 2, 3],
    [4, 5, 6]
]

b = [
    [1, 2],
    [3, 4],
    [5, 6]
]

#Método para multiplicar dos matrices.
def multiplicar(m1, m2): 

    if len(m1[0]) == len(m2): #Comprobamos que las matrices se puedan multiplicar.
        m3 = [] #Creamos una matriz vacía para el resultado.
        for i in range(len(m1)): #Recorremos la matriz m1.
            m3.append([])
            for j in range(len(m2[0])): #Recorremos la matriz m2.
                m3[i].append(0) #Añadimos un elemento a la matriz m3.

        for i in range(len(m1)): #Recorremos la matriz m1.
            for j in range(len(m2[0])): #Recorremos la matriz m2.
                for k in range(len(m2)): #Recorremos la matriz m2.
                    m3[i][j] += m1[i][k] * m2[k][j] #Multiplicamos las matrices.
            
        return m3 #Devolvemos el resultado.
    else: #Si las matrices no se pueden multiplicar. 
        return None

c = multiplicar(a, b)

print("Resultado: ", c)