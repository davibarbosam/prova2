#Aluno: Francisco David Barbosa Martins
#Matricula: 20162143000018

import random

print("*********************************")
print("***Bem vindo ao jogo da Forca!***")
print("*********************************")

# A funcao len vai servir para pegar o tamanho da minha palavra secreta
banco_secreto= ["redes","biologia","eletromecanica"]
forca=random.choice(banco_secreto)
rodada = 5

ganhou= False
enforcou= False

for x in range(0, len(banco_secreto)):

	while(rodada <= 5):

		while(not ganhou and not enforcou):
			# O index ele me informa a posição
			index=0
			# O strip elimina os espaços em brancos da esquerda e da direita
			palpite=input("Qual é a letra? ").lower().strip()
			
			#verificar o tamanho do palpite, se é apenas uma letra
			#if(srting_length('forca')>1):
				#print("Você deve digitar apenas uma letra!")
			#continue

			for x in forca:
				if(palpite == x):
					print("Letra {} encontrada na posicao {}".format(palpite,index))
					index +=1

		rodada = +1



print("Olha, você é phod@. Parabéns!")
print("Fim do jogo")

# O count conta a quantidade de ocorrencias 'X'
