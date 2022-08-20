"""
Referencia: https://www.youtube.com/watch?v=IbzzK9PtFBE&ab_channel=ManuelGonzález
"""

class Matriz(object): #Clase para las matrices.

    def __init__(self, m1, m2): #Recibe dos matrices.
        self.m1 = m1 #Guardamos la primera matriz.
        self.m2 = m2 #Guardamos la segunda matriz.
    
    #Método para multiplicar dos matrices.
    def multiplicar(self, m1, m2): 

        if len(self.m1[0]) == len(self.m2): #Comprobamos que las matrices se puedan multiplicar.
            m3 = [] #Creamos una matriz vacía para el resultado.
            for i in range(len(m1)): #Recorremos la matriz m1.
                m3.append([])
                for j in range(len(self.m2[0])): #Recorremos la matriz m2.
                    m3[i].append(0) #Añadimos un elemento a la matriz m3.

            for i in range(len(self.m1)): #Recorremos la matriz m1.
                for j in range(len(self.m2[0])): #Recorremos la matriz m2.
                    for k in range(len(self.m2)): #Recorremos la matriz m2.
                        m3[i][j] += self.m1[i][k] * self.m2[k][j] #Multiplicamos las matrices.
                
            return m3 #Devolvemos el resultado.
        else: #Si las matrices no se pueden multiplicar. 
            return None


#Definiendo las matrices de 4x4.

#Primera matriz de 4x4.
a = [
        [1, 2, 3, 4], 
        [5, 6, 7, 8], 
        [9, 10, 11, 12], 
        [13, 14, 15, 16]
    ]

#Segunda matriz de 4x4.
b = [
        [1, 2, 3, 4], 
        [5, 6, 7, 8], 
        [9, 10, 11, 12], 
        [13, 14, 15, 16]
    ]

matriz = Matriz(a, b) #Creamos un objeto de la clase Matriz.
print("Resultado", matriz.multiplicar(a, b)) #Imprimimos el resultado de la multiplicación de las matrices.