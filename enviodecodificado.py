archivo=open("C:/Users/cR1ss/Desktop/INF-330/C2codifica.txt")
le0 = archivo.readline()
le1 = archivo.readline()
lee = archivo.readline()
if len(lee) % 2!= 0:
    lee=lee[:-1]
iporigen=lee[0:32]
npaquetes=lee.count(iporigen)
nroporfila=len(lee)//npaquetes

fila=[]
mensaje=lee
while mensaje != '':
    fila.append(mensaje[:nroporfila])
    mensaje=mensaje[nroporfila:]

ipo=[]
while iporigen != '':
    ipo.append(int(iporigen[:8],2))
    iporigen=iporigen[8:]


ipdestino=lee[-32:]
ipd=[]
while ipdestino !='':
    ipd.append(int(ipdestino[:8],2))
    ipdestino=ipdestino[8:]

dipo=repr(ipo[0])+'.'+repr(ipo[1])+'.'+repr(ipo[2])+'.'+repr(ipo[3])
dipd=repr(ipd[0])+'.'+repr(ipd[1])+'.'+repr(ipd[2])+'.'+repr(ipd[3])

print('IP ORIGEN:',dipo)
print('IP DESTINO:',dipd)

binario=''
for i in range(len(fila)):
    binario=binario+fila[i][40:-32]

binary_int = int(binario, 2)
byte_number = binary_int.bit_length() + 7 // 8
binary_array = binary_int.to_bytes(byte_number, "big")
ascii_text = binary_array.decode()
print('MENSAJE ORIGINAL:',ascii_text)