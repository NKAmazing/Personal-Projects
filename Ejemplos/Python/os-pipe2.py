import os, time, sys

r, w = os.pipe()

ret = os.fork()

if not ret:
    while True:
        leido = os.read(r, 100)
        print("Hijo leido: ", leido.decode().upper())
    
for i in sys.stdin:
    os.write(w, bytes(i.encode()))


