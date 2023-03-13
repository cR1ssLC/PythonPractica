x=int(input('ingrese un numero'))
pila = []
for i in range(0,x):
    num=int(input('ingrese un numero a la pila'))
    if num % 2 == 0:
        pila.append(num)
print(pila)