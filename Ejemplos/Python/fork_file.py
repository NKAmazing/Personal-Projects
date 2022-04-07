import os, time

fd = open("/home/nk-nicolas/Documentos/Apuntes/Ejemplos/archivo.txt", "w+")

if not os.fork():
    fd.write("hijo escribiendo")
    fd.flush() # fuerzo el volcado de buffer
else:
    time.sleep(1)
    fd.seek(0) 
    # se pone seek porque sino no lee nada, lee desde el offset en adelante
    print("Padre leyendo: ", fd.read())


print("cerrando el archivo...")
fd.close() 
# si quiero que se ejecute algo en los dos procesos lo hago afuera del if
