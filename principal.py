
from filaC import FilaCircular
from aluno import Aluno
from exibe_fila import exibir_fila


"""Cria objetos alunos-------------------------------------"""
aluno1 = Aluno('Maria', '001')
aluno1.inseri_nota(1, 2, 0.5)
aluno2 = Aluno('João', '002')
aluno2.inseri_nota(1, 2, 1)
aluno3 = Aluno('Amanda', '003')
aluno3.inseri_nota(0.5, 1.5, 1)
aluno4 = Aluno('George', '004')
aluno4.inseri_nota(0, 1, 1)
aluno5 = Aluno('Paulo', '005')
aluno5.inseri_nota(1, 1, 1)
aluno6 = Aluno('Mateus', '006')
aluno6.inseri_nota(0, 2, 1)
aluno7 = Aluno('Marcos', '007')
aluno7.inseri_nota(1, 2, 1)
aluno8 = Aluno('Lucas', '008')
aluno8.inseri_nota(0, 1, 1)
aluno9 = Aluno('Thiago', '009')
aluno9.inseri_nota(1, 2, 1)
aluno10 = Aluno('Pedro', '010')
aluno10.inseri_nota(1, 1, 1)
aluno11 = Aluno('Nicolas', '011')
aluno11.inseri_nota(1, 2, 0)
aluno12 = Aluno('Juditi', '012')
aluno12.inseri_nota(1, 2, 1)
aluno13 = Aluno('Armando', '013')
aluno13.inseri_nota(0, 2, 1)
"""--------------------------------------------"""

fila = FilaCircular()   # Cria uma fila circular

# Inserindo os 10 primeiros elementos na fila
fila.enfileira(aluno1)
fila.enfileira(aluno2)
fila.enfileira(aluno3)
fila.enfileira(aluno4)
fila.enfileira(aluno5)
fila.enfileira(aluno6)
fila.enfileira(aluno7)
fila.enfileira(aluno8)
fila.enfileira(aluno9)
fila.enfileira(aluno10)
#################################################

exibir_fila(fila)            # Exibi todos os alunos seus atributos e a média total

"""fila.enfileira(aluno11)      # Ao tentar enfileirar outro elemento é gerado uma Exceção
exibir_fila(fila)"""
print('=-=-=-=-=-=-=-=--=-=-=-=-=-=-=\n')
fila.desenfileira()          # Desenfileira 3 elementos da fila
fila.desenfileira()
fila.desenfileira()
exibir_fila(fila)            # Exibi a fila novmente
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
fila.enfileira(aluno11)      # Enfileira os 3 ultimos elementos que restavam
fila.enfileira(aluno12)
fila.enfileira(aluno13)
exibir_fila(fila)            # Exibi a fila novamente

print('=-=-=-=-=-Primeiro da fila depois das operações=-=-=-=-=-=-=')
fila.primeiro()

