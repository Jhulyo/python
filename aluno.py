class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = [None] * 3

    def inseri_nota(self, n1, n2, n3):
        notas = self.notas
        notas[0] = n1
        notas[1] = n2
        notas[2] = n3

    def computar_media(self):
        media = sum(self.notas) / 3
        return print(f'Média do aluno: {media: .2f}')

    def __str__(self):
        return f'Nome: {self.nome}\nMatrícula: {self.matricula}\nNotas: {self.notas}'




