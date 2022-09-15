"""
Referencia: 
1. Multiplicación de matrices:
    https://www.youtube.com/watch?v=IbzzK9PtFBE&ab_channel=ManuelGonzález

2. Suma de dos matrices.
"""

class Matriz(object): #Clase para las matrices.
    m1 = None;
    m2 = None;

    
    #Método para multiplicar dos matrices iguales.
    def multiplicar(self, m1, m2): 

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
        else: #Si las matrices no se pueden multiplicar, etnonces devolvemos un mensaje de error.
            return "Las matrices no se pueden multiplicar"
    
    def suma(self, m1, m2): #Método para sumar dos matrices iguales.
        
        if len(m1) == len(m2) and len(m1[0]) == len(m2[0]): #Si las matrices tienen las mismas filas y columnas.
            m3 = [] #Creamos una matriz vacía para el resultado.

            for i in range(len(m1)): #Se crea una matriz con las mismas dimensiones que m1 y m2.
                m3.append([])
                for j in range(len(m1[0])):
                    m3[i].append(0)
            
            #Se recorre la matriz m3 y se le asigna el resultado de la suma de las matrices m1 y m2.
            for i in range(len(m3)):
                for j in range(len(m3[0])): 
                    m3[i][j] = m1[i][j] + m2[i][j] #Se suman los elementos de las matrices.
            
            return m3 #Devolvemos el resultado.
        else: #Si las matrices no tienen las mismas dimensiones, entonces devolvemos un mensaje de error.
            return "Las matrices no tienen las mismas dimensiones"