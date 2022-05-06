import mmap, os, time, signal

memoria = mmap.mmap(-1, 100)

pid = os.fork()

if pid == 0:
    # hijo
    memoria.write(b"hola papa que tal\n")
    print("offset hijo: ", memoria.tell())
    time.sleep(2)
    memoria.seek(0)
    leido = memoria.readline().decode()
    print("leido en el hijo: ", leido)
    exit()

# padre
time.sleep(1)
print("offset en el padre: ", memoria.tell())
# memoria.seek(0)
leido = memoria.readline()
print("Padre leyendo: ", leido.decode())
memoria.seek(0)
memoria.write(b"hola hijo que tal\n")

os.wait()

print("antes de irme: ")
memoria.seek(0)
print(memoria.read().decode())
