import os

retorno = os.fork()

# hay dos procesos

print('PID = %d , PPID = %d , Retorno: %d' %(os.getpid(), os.getppid(), retorno))

if retorno == 0:
    print("este es el hijo")
    # os._exit(7) # ejecuta un exit con estado terminacion: 7
else:
    print("este es el padre")
    ret = os.wait() # usa un wait para esperar al proceso hijo
    print(ret)


