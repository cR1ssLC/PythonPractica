#MAQUINA DE TURING
archivo = open("C:/Users/cR1ss/Desktop/INF-330/entrada.txt")
lee = archivo.readline()
linea=lee[3:]
indice=linea[:8]
mensaje=linea[8:]
vector = []
while mensaje != '':
    vector.append(mensaje[:24])
    mensaje=mensaje[24:]
indiceaux=indice
binario=''
while int(indiceaux,2) != 0:
    for i in range(0, len(vector)):
        if indiceaux == vector[i][0:8]:
            binario = binario + vector[i][8:16]
            indiceaux = vector[i][16:24]

binary_int = int(binario, 2)
byte_number = binary_int.bit_length() + 7 // 8
binary_array = binary_int.to_bytes(byte_number, "big")
ascii_text = binary_array.decode()
print('el mensaje es :',ascii_text)