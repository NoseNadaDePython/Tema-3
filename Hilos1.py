import threading

#Clase hilo
class MiHilo(threading.Thread):
    def __init__(self,x):
        self.__x = x
        threading.Thread.__init__(self)
        
    def run(self): #run se utiliza para definir el comportamiento del hilo
        print(str(self.__x))
        
#inicando 10 hilos
for i in range(10):
    MiHilo(i).start()