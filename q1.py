#Aluno: Francisco David Barbosa Martins
#Matricula: 20162143000018

import random

print("**********BEM VINDO AO JOGO DO DADO**********")

valor=True

while valor==1:
	dado=random.randint(1,6)
	print("Valor do dado: ", dado)
	num=int(input("Digite 1 para continuar ou 0 para encerrar: "))

	if (num == 1):
		print("Vamos mais uma rodada")
		continue
	else:
		print("Jogo finalizado")
		break

print("Fim do jogo")