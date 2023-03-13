from collections import deque
colaReglas = deque([])
colaAn = deque([])
colaCo = deque([])

nr=int(input('ingrese el numero de reglas: '))

def reglas(x,antecedente, concecuente):
    regla = 'R' + str(x) + ' ' + antecedente + '-->' + concecuente
    colaReglas.append(regla)


for i in range(1,nr+1):
    antecedente=str(input('ingrese antecedente: '))
    concecuente=str(input('ingrese concecuente: '))
    colaAn.append(antecedente)
    colaCo.append(concecuente)
    reglas(i,antecedente,concecuente)

print(colaReglas)