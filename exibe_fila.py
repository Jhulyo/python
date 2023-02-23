from filaC import FilaCircular


# Função que exibi a fila e a média de todos os alunos, com o parâmetro de tipo fila circular.
def exibir_fila(FilaCircular):
    fila = FilaCircular
    for i in fila.data:
        if i is not None:
            print(f'{i}')
            nota = []
            nota.extend(i.notas)
            media = sum(nota) / 3
            print(f'Média do aluno: {media: .2f}')

