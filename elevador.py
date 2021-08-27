from regras import regras
import time

class Elevador():
    def __init__(self):
        self.andar = 1
        self.destino = None
        self.deslocamento = False
        self.fila = []
    
    def chamadaElevador(self, andar):
        self.fila.extend(andar.strip().split(' '))
    
    def statusElevador(self):
        return regras(str(self.andar), str(self.destino))

    def funcoes(self):
        while self.fila:
            self.destino = int(self.fila.pop(0))
            print('Status do elevador: {}\n'.format(self.statusElevador()))

            if self.andar != self.destino:
                print('Elevador em movimento...')
                self.deslocamento = True
                time.sleep(2)
                self.andar = self.destino
                print('Andar atual do elevador: {}\n'.format(self.andar))