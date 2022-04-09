import os
import time

input_1 = int(input('Ingresar: '))
input_2 = str(input("Ingresar archivo: "))

fd = open(f"/home/nk-nicolas/Documentos/Apuntes/Personal-Projects/Ejemplos/Python/{input_2}.txt", "w+")
fd.close
PID_list = []
for i in range(input_1):
    ret = os.fork()
    if ret == 0:
        pid = os.getpid()
        with open(f"/home/nk-nicolas/Documentos/Apuntes/Personal-Projects/Ejemplos/Python/{input_2}.txt", "a") as fd:
            fd.write(str(pid) + ",")
        os._exit(0)

time.sleep(1)
with open(f"/home/nk-nicolas/Documentos/Apuntes/Personal-Projects/Ejemplos/Python/{input_2}.txt", "r") as fd:
    lines = fd.read().split(",")
    for line in lines:
        print(line)
        PID_list.append(line)
    PID_list.remove("")
    print(PID_list)

for i in range(input_1):
    os.wait()
print("soy el padre")

