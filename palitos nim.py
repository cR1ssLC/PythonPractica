print('JUEGO DE LOS PALITOS NIM')
n = int(input('Numero de palitos'))
np = int(input('Cuantos palitos selecciona maximo'))
archivo = open("C:/Users/cR1ss/Desktop/inf351/base.txt")
linea = archivo.readline()
cp=0
while linea != '':
    registro = linea.split(",")
    if len(registro)>1:
        xn = int(registro[1][1:3])
        xnp = int(registro[2][1:2])
        if xn==n and xnp==np:
            print(registro[0],registro[1][1:3],registro[2][1:2],registro[3])
            cp += 1
    linea=archivo.readline()
print('numero de partidas ', cp)