import time

#Divisão de notas
nota1=float(input('primeira media:'))
nota2=float(input('segunda media:'))
nota3=float (input('terceira media:'))

#calculo das notas
c=(nota1 + nota2 + nota3)

#time
print('calculando...')
time.sleep(3)

#condicional
if c < 15:
    print('Estude para a recuperação')
else:
    print('Parabéns e boas ferias')