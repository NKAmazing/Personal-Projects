import string
import time

def main():
    fd = open("/home/nk-nicolas/Documentos/Apuntes/Personal-Projects/Ejemplos/Python/ejemplo.txt", "w+")
    fd.close()
    veces = 3
    lista = list(string.ascii_uppercase)
    lista_2 = [1234, 1235, 1236]
    dicc_proc = {}
    i = 0
    for g in range(len(lista_2)):
        dicc_proc[lista_2[g]] = lista[i]
        i += 1
    if veces >= 1:
        for g in range(veces):
            store_letter(dicc_proc)
        print("El proceso ha terminado de cargar los datos")
        print(dicc_proc)
    else:
        print("ERROR")

def store_letter(dicc_proc):
    for i in dicc_proc.values():
        with open("/home/nk-nicolas/Documentos/Apuntes/Personal-Projects/Ejemplos/Python/ejemplo.txt", "a") as fd:
            fd.write(str(i))
            fd.flush()
            time.sleep(1)
    
if __name__ == '__main__':
    main()
