## Programa de validacion de archivos.

#Librerias usadas
import argparse
from ast import arg
from asyncore import read
import sys
import os


#Definimos la clase main que será llamada para ejecutar las op.
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i',type=str,help="Ingresa el nombre de un archivo existente.")
    parser.add_argument('-o',type=str,help="Ingrese el nombre del archivo donde se copiará el contenido.")
    args = parser.parse_args()
    sys.stdout.write(str(copy(args)))


#Creamos la funcion de calculate para saber que operaiones se van a realizar.

def copy(args):
    args1 = args.i

    if os.path.exists(args1) == True:
        exist = open(args.i, "r")
        content = exist.read()
        print(content)

        with open(args.i, "r") as read_file:
            with open(args.o, "w") as write_file:
                for line in read_file:
                    write_file.write(line)
                    return "La copia se ha realizado correctamente!"
    else:
        print("El archivo no existe!")

if __name__=='__main__':
    main()

## bibliografia usada para verficar existencia: https://geekflare.com/es/check-if-file-folder-exists-in-python/
