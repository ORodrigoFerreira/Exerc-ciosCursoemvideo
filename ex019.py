import random

n1 = input('Aluno 1:')
n2 = input('Aluno 2:')
n3 = input('Aluno 3:')
n4 = input('Aluno 4:')

alunos = [n1, n2, n3, n4]

print('O aluno {} irá apagar o quadro.'.format(random.choice(alunos)))
