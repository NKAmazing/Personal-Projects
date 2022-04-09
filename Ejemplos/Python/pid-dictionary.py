import os

input_1 = int(input('Ingresar: '))

PID_list = []
for i in range(input_1):
    ret = os.fork()
    pid = os.getpid()
    PID_list.append(pid)
    if ret == 0:
        print(PID_list)
        os._exit(0)
for i in range(input_1):
    os.wait()
print(" soy el padre ")

