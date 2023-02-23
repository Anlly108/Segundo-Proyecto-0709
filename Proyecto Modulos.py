import time
from cryptography.fernet import fernet  
import numpy as np
print ("Proyecto\n")

print("--------------------")
print("* Menú de opciones *")
print("--------------------")

print("1. Modulo Validacion")
print("2. Modulo algebra")
print("3. Modulo cripto")


if numero == 1:
    def valInt(var1, var2=None):

      if var2 is None:
        if type(var1) != int:
          return False

        return True

      if type(var1) != int or not isinstance(var2, (list, tuple)) or var20>var2-1:
        raise ValueError

      if type(var20) != int or type(var2-1) != int:
        raise TypeError

      if var1 < var20 or var1 > var2-1:
        return False

      return True
        
    def valFloat(x,y=None):
        try: 
            if (y != None and type(y) != tuple):
                raise TypeError("El segundo argumento debe ser una tupla")
            elif (type(x) != float or (y != None and (len(y) < 2 or y0 > y1))):
                raise ValueError("El primer argumento no es float o la tupla no está ordenada de manera creciente")
            elif (y == None): 
                return True
            else : 
                return x >= y0 and x <= y1 

        except Exception as error: 
            print ("Ha ocurrido un error: ",error.args)

            
    def valComplex(variable): 
        if isinstance(variable, complex): 
            return True 
        else: 
            return False 

            
    def valList(variable): 
        if isinstance(variable, list): 
            return True                                                                                                                                                                                                         
            
    def valComplex(arg1, arg2=None): 
    if arg2 == None: 
        if type(arg1) == complex: 
            return True 
        else: 
            return False 

    if type(arg1) != complex or type(arg2) not in (list, tuple): 
        raise TypeError("Los argumentos deben ser de los tipos correctos")

    móduloarg1 = abs(complex.real + complex.imag*1j)

    if len (arg2) < 2 or móduloarg1 < min(arg2) or móduloarg1 > max(arg2):  
        raise ValueError("El segundo argumento no está ordenado de manera creciente o su tamaño es incorrecto.")

    return móduloarg1 in range (min (arg2), max ()+ 1)
            
elif numero == 2:
    
    print("1. Multiplicacion de matrices")
    print("2. Inversion de Matrices")
    print("3. Producto vectorial")
    print("4. Transposicion de matrices")
    print("5. Resolucion de sistema de ecuaciones lineales")
    
    if numero==1:
        def producto_matrices(a, b):
        filas_a = len(a)
        filas_b = len(b)
        columnas_a = len(a[0])
        columnas_b = len(b[0])
        if columnas_a != filas_b:
            return None
        producto = []
        for i in range(filas_b):
            producto.append([])
            for j in range(columnas_b):
                producto[i].append(None)
        for c in range(columnas_b):
            for i in range(filas_a):
                suma = 0
                for j in range(columnas_a):
                    suma += a[i][j]*b[j][c]
                producto[i][c] = suma
        return producto

    matriz_a = [
        [3, 2, 1],
        [1, 1, 3],
        [0, 2, 1],
    ]
    matriz_b = [
        [2, 1],
        [1, 0],
        [3, 2],
    ]
    producto = producto_matrices(matriz_a, matriz_b)
    if producto:
        for fila in producto:
            for valor in fila:
                print(valor, end=" ")
            print("")
    else:
        print("El número de columnas de A es distinto al número de filas de B")
    
    elif numero==2:
        A = np.array([[4,2,5],
                      [2,5,8],
                      [5,4,3]])

        B = np.array([[60.70],
                      [92.90],
                      [56.30]])

        casicero = 1e-15 

        A = np.array(A,dtype=float) 

        AB = np.concatenate((A,B),axis=1)
        AB0 = np.copy(AB)

        tamano = np.shape(AB)
        n = tamano[0]
        m = tamano[1]

        for i in range(0,n-1,1):
            columna = abs(AB[i:,i])
            dondemax = np.argmax(columna)
            
            if (dondemax !=0):
                temporal = np.copy(AB[i,:])
                AB[i,:] = AB[dondemax+i,:]
                AB[dondemax+i,:] = temporal
                
        AB1 = np.copy(AB)

        for i in range(0,n-1,1):
            pivote = AB[i,i]
            adelante = i + 1
            for k in range(adelante,n,1):
                factor = AB[k,i]/pivote
                AB[k,:] = AB[k,:] - AB[i,:]*factor
        AB2 = np.copy(AB)

        ultfila = n-1
        ultcolumna = m-1
        for i in range(ultfila,0-1,-1):
            pivote = AB[i,i]
            atras = i-1 
            for k in range(atras,0-1,-1):
                factor = AB[k,i]/pivote
                AB[k,:] = AB[k,:] - AB[i,:]*factor
            AB[i,:] = AB[i,:]/AB[i,i]
        X = np.copy(AB[:,ultcolumna])
        X = np.transpose([X])

        print('Matriz aumentada:')
        print(AB0)
        print('Pivoteo parcial por filas')
        print(AB1)
        print('eliminacion hacia adelante')
        print(AB2)
        print('eliminación hacia atrás')
        print(AB)
        print('solución de X: ')
        print(X)
    
    elif numero==3:
    
    elif numero==4:
    
        def transpose(matrix):
            if matrix == None or len(matrix) == 0:
                return []
                
            result = [[None for i in range(len(matrix))] for j in range(len(matrix[0]))]
            
            for i in range(len(matrix[0])):
                for j in range(len(matrix)):
                    result[i][j] = matrix[j][i]
                    
            return result
            
        def print_matrix(matrix):
            for row in matrix:
                print(*row)

        array = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15]
        ]
        result = transpose(array)
        print_matrix(result)
            
    elif numero==5:
    
    if np.linalg.det(A) == 0:
    x = None
    print("No se puede resolver")
else:
    x = (A**-1)*b
    
    else 
        print("La opción elegida no existe, vuelve a intentar.")

elif numero == 3:

    str1 = "Hola Mundo"
    key = Fernet.generate_key()
      
    fernet = Fernet(key)
      
    enctex = fernet.encrypt(str1.encode())
      
    dectex = fernet.decrypt(enctex).decode()

    print("Mensaje a encriptar: ", str1)
    print("Mensaje encriptado: ", enctex)
    print("Mensaje desencriptado: ", dectex)



else:
    print("La opción elegida no existe, vuelve a intentar.")