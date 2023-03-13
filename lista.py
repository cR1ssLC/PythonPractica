num=int(input('ingrese un numero'))
def f(x):
    return list(map(int, str(num)))
print('sin ordenar:',f(num))
orden=sorted(f(num))
print('con orden',orden)