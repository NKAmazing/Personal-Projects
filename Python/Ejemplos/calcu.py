## Calculadora con getopt 

import sys
import getopt

def calculate():
    operation = None
    n = None
    m = None
    total = None

    argv = sys.argv[1:]
    #printea argumentos

    opts, args = getopt.getopt(argv, 'o:n:m:')
    # print("Opciones: ", opt)
    # print("Argumentos: ",arg)


    for opt, arg in opts:
        if opt in ['-o']:
            operation = arg
        elif opt in ['-n']:
            n = int(arg)
        elif opt in ['-m']:
            m = int(arg)

    if operation == "*":
        total = n*m
    elif operation == "+":
        total = n+m
    elif operation == "-":
        total = n-m
    elif operation == "/":
        total = n/m
    print('operation:{}'.format(operation))
    print('n:{}'.format(n))
    print('m:{}'.format(m))

    print('El total es {}'.format(total))

calculate()
