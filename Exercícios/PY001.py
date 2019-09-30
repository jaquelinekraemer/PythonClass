# 1. Leia uma frase digitada pelo usuário.
# 2. Leia uma letra digitada pelo usuário.
# 3. Informe para o usuário quantas vezes aparece na frase (passo 1) a letra (passo 2).
# 4. Informe para o usuário a posição em que a letra aparece a primeira vez na frase.
# 5. Informe para o usuário a posição em que a letra aparece pela última vez na frase.

print('='*60)

frase = input('{0}Digite uma frase: '.format(' '*5))
letra = input('{0}Digite uma letra: '.format(' '*5))
print('{}A letra {} aparece {} vezes na frase.'.format(' '*5, letra, frase.count(letra)))
print('{}A letra {} aparece pela primeira vez na posição {} da frase'.format(' '*5, letra, frase.find(letra)+1))
print('{}A letra {} aparece pela primeira vez na posição {} da frase'.format(' '*5, letra, frase.rfind(letra)+1))

print('='*60)