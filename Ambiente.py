
import random

class Ambiente():
    def __init__(self, capacidade, nivel):
        self.estado = {
            'A': random.choice(['cheio','vazio']),
            'B': random.choice(['cheio','vazio']),
            'C': random.choice(['cheio','vazio'])
        }
        self.capacidade = capacidade
        self.nivel = nivel

    def esta_vazio(self):
        return self.nivel == 0

    def encher(self):
        self.nivel = self.capacidade
    
    def localizar(self):
        return random.choice(['A','B','C'])
    
    def percepcao(self, agente):
        return (agente.localizar, self.estado[agente.localizar])
    