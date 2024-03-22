from Ambiente import Ambiente

class Agente:
    def __init__(self, ambiente):
        self.ambiente = ambiente
        self.posicaoAtual = 0
        self.nivel = nivel

    def estaVazio(self):
        return self.nivel == 0

    def encher(self):
        self.nivel = self.capacidade

    def moverSentidoHorario(self):
        self.posicaoAtual = (self.posicaoAtual + 1) % len(self.ambiente)

    def agir(self):
        for _ in range(len(self.ambiente)):
            baldeAtual = self.ambiente[self.posicaoAtual]
            if baldeAtual.estaVazio():
                baldeAtual.encher()
                print(f"Encher balde na posicao {self.posicaoAtual + 1}")
                return
            self.moverSentidoHorario()
        print("balde vazio nao encontrado.")

  