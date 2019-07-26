#Aluno: Francisco David Barbosa Martins
#Matricula: 20162143000018

#O random tem que ser importado pois não é uma função bult-in
import random
	
print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

#randrange serve para gerar um número aleatório dentre 1 e 101
num_secreto = random.randrange(1,101)
total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
	#O format cria uma string que contem campos entre chaves a serem substituídos pelos argumentos de format
	print("Tentativa {} de {}".format(rodada, total_de_tentativas))

	chute_str = input("Digite um número entre 1 e 100: ")
	print("Você digitou " , chute_str)
	chute = int(chute_str)

	if(chute < 1 or chute > 100):
		print("Você deve digitar um número entre 1 e 100!")
		continue

	acertou = chute == num_secreto
	maior   = chute > num_secreto
	menor   = chute < num_secreto

	if(acertou):
		print("Você acertou e fez {} pontos!".format(pontos))
		break
	else:
		if(maior):
			print("Não foi dessa vez... O seu chute foi maior do que o número secreto.")
		elif(menor):
			print("Não foi dessa vez... O seu chute foi menor do que o número secreto.")

print("Olha, o numero secreto era: ",num_secreto)
print("Fim do jogo")