from time import sleep
import emoji
print(emoji.emojize(':fireworks:'))
for c in range(10, 0, -1):
    print(c)
    sleep(1)

print(emoji.emojize(':fireworks:'*10))
print('\033[31;40m Feliz Ano Novo!!!\033[m')
print(emoji.emojize(':fireworks:'*10))
