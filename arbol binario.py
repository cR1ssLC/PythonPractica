class Nodo:
    def __init__(self, valor = None, izq = None, der = None):
        self.valor=valor
        self.izq=izq
        self.der=der
    def __str__(self):
        return "Valor: {}".format(self.valor)
class Binario:
    def __init__(self):
        self.raiz = None
    def agregar(self, elemento):
        if self.raiz == None:
            self.raiz = elemento
        else:
            aux = self.raiz
            padre = None
            while aux != None:
                padre = aux
                if int(elemento.valor) > int(aux.valor):
                    aux=aux.der
                else:
                    aux=aux.izq
            if int(elemento.valor) > int(padre.valor):
                padre.der = elemento
            else:
                padre.izq = elemento
    def getRaiz(self):
        return self.raiz

def printInorder(nodo):
    if nodo: 
        printInorder(nodo.izq)
        print(nodo.valor),
        printInorder(nodo.der)

def printPostorder(nodo):
    if nodo:
        printPostorder(nodo.izq)
        printPostorder(nodo.der)
        print(nodo.valor),

def printPreorder(nodo):
    if nodo:
        print(nodo.valor),
        printPreorder(nodo.izq)
        printPreorder(nodo.der)

arbol = Binario()
a=Nodo(23)
b=Nodo(11)
c=Nodo(7)
f=Nodo(15)
x=Nodo(43)
y=Nodo(72)

arbol.agregar(a)
arbol.agregar(b)
arbol.agregar(c)
arbol.agregar(f)
arbol.agregar(x)
arbol.agregar(y)

print("Recorre Ala Izquierda:")
p=arbol.getRaiz()
while p!=None:
  print(p)
  p=p.izq

print("Recorre Ala Derecha:")
p=arbol.getRaiz()
while p!=None:
  print(p)
  p=p.der
print("Ok")

print("Recorrido PRE-ORDER")
p=arbol.getRaiz()
printPreorder(p)

print("Recorrido IN-ORDER")
p=arbol.getRaiz()
printInorder(p)

print("Recorrido POST-ORDER")
p=arbol.getRaiz()
printPostorder(p)