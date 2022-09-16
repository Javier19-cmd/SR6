"""
Referencias: 
 1. Acceder a una variable de una clase: https://www.codigopiton.com/variables-de-clase-y-de-instancia-en-python/#:~:text=Como%20puedes%20ver%2C%20para%20acceder,código%20definido%20en%20la%20clase.
 2. Acceder a un método de una clase: https://j2logo.com/python/tutorial/programacion-orientada-a-objetos/#:~:text=Para%20crear%20un%20objeto%20de,se%20llamara%20a%20una%20función).&text=El%20código%20anterior%20crea%20una,objeto%20a%20la%20variable%20obj%20.
 3. Inicializar una clase: https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=44&codigo=44&inicio=30
 4. Clases en Python: https://tutorial.recursospython.com/clases/#:~:text=Para%20crear%20una%20clase%20vamos,mayúscula%2C%20y%20sin%20guiones%20bajos.
"""
#Archivo que tendrá el método main del programa

from gl import * #Importando el archivo gl.py, para crear la imagen.
from textures import * #Importando los métodos del archivo textures.py.

def main():
    glCreateWindow(1024, 1024) #Creando la ventana.
    #glCreateWindow(5000, 5000) #Creando la ventana.
    glClearColor(1, 1, 1) #Color del fondo.
    glClear() #Limpiando el framebuffer con el color creado en glClearColor.
    
    glViewPort(0, 0, 300, 300) #Asignando el viewport.
    
    #glVertex(0.1, 0.3) #Dibujando el punto.

    #glColor(0.6, 0.1, 0.9) #Asignando el color del punto.

    #col1 = color(0.501, 0.501, 0.501) #Color gris.

    col1 = (0.6, 0.1, 0.9) #Otro color.

    #triangle(V3(10, 70), V3(50, 160), V3(70, 80), col1) #Llamando al método triangle para dibujar un triángulo.
    #triangle(V3(180, 50), V3(150, 1), V3(70, 180), col2) #Llamando al método triangle para dibujar un triángulo.
    #triangle(V3(180, 150), V3(120, 160), V3(130, 180), col3) #Llamando al método triangle para dibujar un triángulo.


    #modelo("./Pallet.obj", scale, translate, col1)

    # zBuffer() #Haciendo la copia del z-buffer.

    #Probando el lookat.
    lookAt(V3(0, 0, 5), V3(0, 0, 0), V3(0, 1, 0))

    scale = (1, 1, 1) #Escala para los bb8's.
    translate = (0.4, 0.4, 0) #Traslación para los bb8's.
    
    rotacion = (0, pi/12, 0) #Rotación para los bb8's.

    print("Rotación: ", rotacion)
    
    #Esta llamada puede no estar acá.
    loadModelMatrix(translate, scale, rotacion) #Se carga la matriz de transformación del modelo. Acá se recibe la traslación, la escala y la rotación.

    #Esta función ahora recibe primero el path del obj, luego el path del bmp, el color.
    modelo("./pumpkin.obj", "./pumpkin.bmp", col1) 


    #texturas("./model.obj", "./model.bmp", col1)

    #texturas("./Pallet.obj", "./Pallet.bmp", col1) #Llamando al método texturas.

    glFinish() #Escribiendo el framebuffer en la imagen y guardándola en un archivo.

main()