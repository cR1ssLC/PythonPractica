import random
from collections import deque
cola = deque([])
x=int(input('ingrese tamaño de la cola'))
for i in range(0,x):
    num=random.randint(0,100)
    if num % 3 == 0 or num%5==0:
        cola.append(num)
print(cola)