import random
from time import sleep

while True:
    pcEscolha = int(random.randint(0, 50)) #escolha do computador

    print('você tem 10 chances para acertar um número aleatório gerado pelo computador!')
    sleep(3) #faz o contador
    print('3..')
    sleep(1)
    print('2..')
    sleep(1)
    print('1...')
    sleep(1)

    #Teste:
    #print(pcEscolha)

    contador = 0 #variável original do contador
    listaPalpites = [] #cria uma lista do inicio do for até o fim dele com as entradas no terminal durante o loop

    for i in range(10): #repete o que está indentado abaixo 10 vezes

    #base do jogo

        contador += 1 #aumenta o valor da variável de acordo com quantas vezes o for se repetiu
        jogEscolha = int(input('------\nDigite um palpite de 0 a 50: '))
        listaPalpites.append(jogEscolha) #fecha o ciclo da lista, indica que terminou para poder montar a lista
        if (jogEscolha < 0 or jogEscolha > 50):
            print('❌ Este palpite é inválido... Digite um número entre 0 e 50\n------')
            continue #continua o código sem gastar a chance
        if(jogEscolha > pcEscolha):
                print('palpite alto!\n------')
        elif(jogEscolha < pcEscolha):
                print('palpite baixo!\n------')
        else:
            print("------\n🎉 Parabéns! Você acertou, o número era", pcEscolha)
            break #termina o loop

    else:
        print('------\n😢 Você perdeu!! O número secreto era {}'.format(pcEscolha))

    print('Você precisou de {} tentativas, seus palpites foram: {}\n-----------'.format(len(listaPalpites), listaPalpites))

    while True:
        retorno = str(input('🔥 Tentar novamente?\nDigite "S" para continuar ou "N" para parar: ').upper())
        if(retorno not in ['N', 'S']):
            print("❌ Resposta inválida")
            continue
        if(retorno == 'N'):
            print('👋 Adeus! Obrigado por jogar!')
            break