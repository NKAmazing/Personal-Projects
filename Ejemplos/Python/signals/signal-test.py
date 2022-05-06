import signal
import os

pid = os.getpid()
print(pid)

# si le mando un sigusr1, en este caso, no haria nada
# signal.signal(signal.SIGUSR1, signal.SIG_IGN)

def funcion(s, f):
    # el s es el numero de señal que esta recibiendo
    print("hola mundo (%d) - (%s)" % (s, f))

# funcion(1, 2)

signal.signal(signal.SIGUSR1, funcion)
