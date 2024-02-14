from io import open 


archivo_texto=open('nombres.txt','r')

# archivo_texto.write('datos en el archivo')
# archivo_texto.close()

for lineas in archivo_texto.readlines():
    print(lineas.rstrip())


archivo_texto.close()