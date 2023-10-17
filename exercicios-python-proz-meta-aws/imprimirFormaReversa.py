andares = [f"{andar}º andar" for andar in reversed(range(1, 21)) if andar != 13]
mensagem = '\n'.join(andares)
print(mensagem)

#Neste código, usei reversed(range(1, 21)) para criar uma sequência de números de 20 a 1 em ordem decrescente. 
# O restante do código é o mesmo que antes, gerando a lista de mensagens, 
# juntando-as com quebras de linha e imprimindo a saída desejada.