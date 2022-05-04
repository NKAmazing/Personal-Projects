import multiprocessing as mp
import os
import time

# defino una funcion
def funcion():
    print("esto es lo que ejecuta el hijo", os.getpid())
    time.sleep(5)

# lo igualo a un mp process y le tengo que pasar un target
hijo = mp.Process(target=funcion)
# starteo el hijo y se crea el proceso
hijo.start()
# libera al hijo, es como un os.wait() a nivel practico
hijo.join()
