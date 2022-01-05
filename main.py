import random
import time
tamanhoCartela = 10
#--------------Funções---------------------------------

def inicio(enter):
  print(*'----INICIANDO LOTERIA----')
  time.sleep(2)
  print(*'----GERANDO CARTELAS----')
  time.sleep(2)
  print(*'----CARTELAS GERADAS-----')
  time.sleep(1)
  print(*'-------BOA SORTE-------')
  time.sleep(2)
  print('\033c')

#Função para preencher as cartelas com valores aleatorios, usando a biblioteca random
def geraCartela(cartelas,nCartelas):
	for i in range(nCartelas):
		cartelas[i] = random.sample(range(1, 26), 10)
	return cartelas

#Função responsavel pela execução da loteria
def executaLoteria(loteria,cartelas,nCartelas,pontos):
	#Primeiro FOR para fazer verificação dos numeros que serão sorteados por vez
	for i in range(len(loteria)):
		#Segundo FOR referente a todas as cartelas que foram  preenchidas
		for j in range(nCartelas):
			#Terceiro for referente aos 10 valores contidos em determinada cartela
			for k in range(tamanhoCartela):
				#Verificação de caso numero sorteado esteja dentro da cartela, sera adicionado 1 ponto
				if(loteria[i] == cartelas[j][k]):
					pontos[j] += 1
		print('-----------------------------------------------------')	
		print(f'O ultimo número sorteado foi {loteria[i]}\n')
		print('Os números que já foram sorteados são: ',end = '')
		#FOR que serve para que a impressão dos numeros ja sorteados, estejam ordenados e organizados, sem quebra de linha
		for l in range(0,i):
			print(loteria[l],end = ', ')
		#FOR referente a impressão de todas as cartelas, contendo seus valores, e os pontos referentes a cada cartela
		for p in range(nCartelas):
			if(p == 0):
				print('')
			print(f'\nCartela n°{p+1} :{cartelas[p]}')
			print(f'Pontos da cartela n°{p+1} :{pontos[p]}')
			if(p == nCartelas-1):
				print('---------------------------------------------------')
		#Sleep para segurar um pouco a tela, dando a impressão de que esta sendo sorteado o proximo numero
		time.sleep(3)
		#Limpa Tela
		print('\033c')
		#sistema de verificação e chamada da função VENCEDOR, para cara tenha um vencedor, sair do loop principal, assim terminando o programa
		auxVencedor = False
		auxVencedor = vencedor(pontos)
		if(auxVencedor == True):
			break

#Função para verificação de cartela alcançando valor maximo de pontos
def vencedor(pontos):
	verificaGanhador = 0
	for j in range(nCartelas):
		if(pontos[j] >= 10):
			print(f'\nA cartela numero {j+1} fez {pontos[j]} pontos.')
			print(f'\033[92m'+'\033[1;43m'+'PARABÉNS POR TER GANHO'+'\033[0;0m')
			verificaGanhador +=1
	if(verificaGanhador > 0):
		return True
		

#--------------------Main------------------------------

enter = input('Aperte ENTER para iniciar o jogo.')
nCartelas = int(input('Digite o numero de cartelas que participarão da loteria: '))

#---------Criação das Matrizes e Vetores---------------

cartelas = [[None]*tamanhoCartela for i in range(nCartelas)]
loteria = [None]*25
pontos = [0]*nCartelas

#-------------Chamada das funcoes----------------------
inicio(enter)
geraCartela(cartelas,nCartelas)
loteria = random.sample(range(1, 26), 25)
executaLoteria(loteria,cartelas,nCartelas,pontos)
