import mmap, os, time, signal

def handler_padre(s, f):
    leido = memoria.readline()
    print("Padre leyendo: ", leido.decode())

memoria = mmap.mmap(-1, 100)

pid = os.fork()

if pid == 0:
    # hijo
    memoria.write(b"hola que tal\n")
    os.kill(os.getppid(), signal.SIGUSR1)
    exit()

# padre
signal.signal(signal.SIGUSR1, handler_padre)
signal.pause()

os.wait()
