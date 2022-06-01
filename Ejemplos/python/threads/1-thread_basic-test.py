import threading
import time

# funcion target del hilo
def thread_function(name):
    print(f"Starting thread: {name}")
    time.sleep(3)
    print(f"Ending thread: {name}")

# creo el hilo
x = threading.Thread(target=thread_function, args=(1,))

# lo inicio
x.start()

# espera a que termine
x.join()

print("We're done here.")