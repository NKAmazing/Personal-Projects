import os, time

r, w = os.pipe() # creo un pipe con un archivo tipo lectura y escritura

# si forkeo se comparte con el hijo, porque puedo acceder con el pipe
ret = os.fork()

if not ret:
    os.write(w, b"hola mundo\n")
    os._exit(0)

time.sleep(1)
os.wait()
# espera a que termine el hijo y luego lo lee 
leido = os.read(r, 100) # el 100 es el tamaño que lee de ese read

print("Padre Leido: ", leido.decode())


# si el hijo leyera el w vacio, quedaria en bucle
# porque se quedaria esperando a que w tenga algo