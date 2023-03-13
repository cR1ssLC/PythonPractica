archivo = open("C:/Users/cR1ss/Desktop/inf351/j100000.bc", "r")
nuevo = open("C:/Users/cR1ss/Desktop/inf351/t100000.bc", "w")

linea= archivo.readline()

lineas = [linea.replace('\n', ',') for linea in archivo]
nuevo.write("".join(lineas).replace(',,','\n').replace('*','').replace(' ',',').replace('TU:',';').replace('CP:',';').replace('=,',' '))

archivo.close()
nuevo.close()