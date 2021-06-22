import threading

import threading

class NossaThr(threading.Thread):
    def __init__(self,idt,nome):
        threading.Thread.__init__(self)
        self.idt = idt
        self.nome = nome

    def run(self):
        print('Iniciando a Thread %s'%(self.nome))
        procThread(self.nome)
        print('Fim da thread %s'%(self.nome))


def procThread(nome):
    cont = 0
    while (cont<1000):
        print('Processo %s da thread %s' %(str(cont),nome))
        cont = cont + 1


Thread1 = NossaThr(1,'t1')
Thread2 = NossaThr(2,'t2')


ArrayThread = []
ArrayThread.append(Thread1)
ArrayThread.append(Thread2)


Thread1.start()
Thread2.start()

for t in ArrayThread:
    t.join()


print('Fim do Programa')


