import subprocess as sp

fd = open("/home/nk-nicolas/Documentos/Apuntes/Ejemplos/sp-file.txt", "w+")

# Uso el pipe para pasarle la salida del proceso anterior a la entrada del siguiente
proc1 = sp.Popen(["ip a"], shell=True, stdout=sp.PIPE)
proc2 = sp.Popen(["grep inet"], shell=True, stdin=proc1.stdout, stdout=sp.PIPE)
proc3 = sp.Popen(["awk '{print $2}'"], shell=True, stdin=proc2.stdout, stdout=fd)
# Me imprime por salida en una archivo el ultimo comando
fd.flush() # si quiero usar flush para cargarlo al buffer, no necesitamos cerrarlo