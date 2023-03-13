#VALIDAR JUGADAS 3 EN RAYA
archivo = open("C:/Users/cR1ss/Desktop/inf351/Validar/JugadasPrimeraParte_OK.csv")
linea = archivo.readline()
for linea in archivo:
    registro = linea.upper()
    if not(registro.find(";A")!=-1 or registro.find(";B")!=-1 or registro.find(";E")!=-1):
        num = registro.find(";")
        print("Linea Observada: " + registro[0:num])