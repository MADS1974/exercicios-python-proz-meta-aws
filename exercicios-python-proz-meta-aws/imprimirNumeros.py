andares = [f"{andar}º andar" for andar in range(1, 21) if andar != 13]
mensagem = '\n'.join(andares)
print(mensagem)

#Neste código, criei a lista de mensagens para cada andar da mesma forma, pulando o 13º andar. 
# Em seguida, usei a função join para unir essas mensagens em uma única string, 
# separando-as por quebras de linha (\n). 
# Por fim, imprimimos a string, resultando na impressão dos andares um abaixo do outro. 
