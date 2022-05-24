import os, signal

print(os.getpid())

# si mando esta señal, lo ignora
signal.signal(signal.SIGUSR1, signal.SIG_IGN)
# se queda colgado hasta que le doy enter y despues lee
os.read(0, 100)


