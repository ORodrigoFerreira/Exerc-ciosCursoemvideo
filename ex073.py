times = ('Fla', 'Int', 'Cam', 'SP', 'Flu', 'Grê', 'Pal',
         'San', 'Cap', 'Bra', 'Cea', 'Cor', 'Acg', 'Bah',
         'Spt', 'For', 'Vas', 'Goi', 'Cor', 'Bot')
print(f'Os 5 primeiros colocados são {times[:5]}.')
print(f'Os quatro últimos colocados são {times[-4:]}.')
print(f'Em ordem alfabética os times são{sorted(times)}.')
print(f'O time Ceará está na {times.index("Cea")+1}ª posição')
