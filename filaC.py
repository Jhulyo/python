from aluno import Aluno


class FilaCircular:
    def __init__(self, ):
        self.data = [None] * 10
        self.size = 0
        self.frente = 0

    def __len__(self):
        return self.size

    def estaVazia(self):
        return self.size == 0

    def primeiro(self):
        if self.estaVazia():
            return 'Fila vazia!'
        return print(self.data[self.frente])

    def enfileira(self, aluno):
        if self.size == len(self.data):
            raise Exception("Limite da Fila!")
        posicao = (self.frente + self.size) % len(self.data)
        self.data[posicao] = aluno
        self.size += 1

    def desenfileira(self):
        if self.estaVazia():
            return 'Fila vazia!'
        elemento = self.data[self.frente]
        self.data[self.frente] = None
        self.frente = (self.frente + 1) % len(self.data)
        self.size -= 1
        print(f'{elemento.nome} foi removido(a) da fila')
