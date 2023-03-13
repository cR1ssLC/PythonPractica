memoria=[]
memoria.append(0)
memoria.append(0)
memoria.append(0)
memoria.append(1)
memoria.append(1)
memoria.append(0)
memoria.append(0)
memoria.append(1)

memoria.append(0)
memoria.append(0)
memoria.append(1)
memoria.append(0)
memoria.append(0)
memoria.append(0)
memoria.append(0)
memoria.append(1)

memoria.append(0)
memoria.append(0)
memoria.append(1)
memoria.append(1)
memoria.append(1)
memoria.append(0)
memoria.append(1)
memoria.append(0)

def vcabezal(n):
    p=(n-1)*8
    for i in range(8):
        print(memoria[p+i],end='')
    print()

def vdcabezal(n):
  p=(n-1)*8
  d=0
  for i in range(8,0,-1):
    d=d+memoria[p+i-1]*(2**(8-i))
    #print(i,memoria[p+i-1])
  return d

def cabezal(n,m):
    texto=binario(m)
    p = (n - 1) * 8
    for i in range(8):
        memoria[p+i]=int(texto[i])

def binario(num):
    s=""
    while num >=2:
        r=num%2
        s=str(r)+s
        num=num//2
    s="00000000"+str(num)+s
    res=s[-8:]
    return res

#print(memoria)
#vcabezal(1)
#vcabezal(2)
#vcabezal(3)

vdcabezal(1)
vdcabezal(2)
vdcabezal(3)

cabezal(2,25)
print('nuevo')
vdcabezal(1)
vdcabezal(2)
vdcabezal(3)

memoria=[]
#numero a = 0
memoria.append(0)
memoria.append(0)
memoria.append(0)
memoria.append(0)
memoria.append(0)
memoria.append(0)
memoria.append(0)
memoria.append(0)
#numero b = 1
memoria.append(0)
memoria.append(0)
memoria.append(0)
memoria.append(0)
memoria.append(0)
memoria.append(0)
memoria.append(0)
memoria.append(1)
#memoria de 512
for i in range(496):
  memoria.append(0)

def vdcabezal(n):
  p=(n-1)*8
  d=0
  for i in range(8,0,-1):
    d=d+memoria[p+i-1]*(2**(8-i))
  return d

def cabezal(n,m):
    texto=binario(m)
    p = (n - 1) * 8
    for i in range(8):
        memoria[p+i]=int(texto[i])

def binario(num):
    s=""
    while num >=2:
        r=num%2
        s=str(r)+s
        num=num//2
    s="00000000"+str(num)+s
    res=s[-8:]
    return res

def fibonacci(n):
    for i in range(3,n+1):
        cabezal(i,vdcabezal(i-2)+vdcabezal(i-1))

def vfibonacci(n):
    fibonacci(n)
    for i in range(n):
        print(vdcabezal(i+1), end=',')

nro=int(input('Ingrese numero:'))
vfibonacci(nro)