import time
from funcoeshelp import clean, letrasacertadas, letrasvazias, checkletra, dieguy

clean()

print("Jogo da Forca\n")
while True:
    print("(1) Jogar")
    print("(2) Sair")
    comando = str(input("-> "))

    if comando == "1":
        clean()
        desafiante = input("\nEscreva seu nome Desafiante :")
        competidor = input("\nEscreva seu nome Competidor :")
        clean()

        palavra = str(input("Diga Deesafiante qual será a Palavra :"))
        palavra = checkletra(palavra)

        help1 = input("\nDiga a 1 dica: ")
        help2 = input("Diga a 2 dica: ")
        help3 = input("Diga a 3 dica: ")

        clean()

        listChave = []
        dicas = [help1, help2, help3]
        letrasTentadas = []
        dicasPedidas = 0
        erros = int(0)
        for letra in palavra:
            listChave.append(letra)
        letras_acertadas = letrasacertadas(palavra)

        while True:
            print('   '.join(letras_acertadas)+"\n")
            if ("_" not in letras_acertadas):
                clean()
                print('   '.join(letras_acertadas)+"\n")
                vitorioso = (f"Palavra: {palavra} > Vencedor: Competidor {competidor}, Desafiante: {desafiante}")
                print(vitorioso)
                input("Pressione enter para continuar: ")
                clean()
                break
            if erros == 5:
                clean()
                print('  '.join(letras_acertadas)+"\n")
                vitorioso = (f"Palavra: {palavra} > Vencedor : Desafiante: {desafiante}, Competidor {competidor}")
                print(vitorioso)
                input("Pressione enter para continuar: ")
                clean()
                break

            print("\nEscolha uma das opções:")
            print("(1) Jogar")
            print("(2) Pedir um Help\n")
            escolha = str(input("-> "))
            clean()
            print('  '.join(letras_acertadas)+"\n")

            if escolha == "1":
                while True:
                    print("Tente alguma Letra: ")
                    tentativa = input("->")
                    tentativa = letrasvazias(tentativa)
                    if not tentativa in letrasTentadas:
                        if tentativa.isalpha():
                            letrasTentadas.append(tentativa)
                            if (tentativa in listChave):
                                index = 0 
                                for letra in listChave:
                                    if (tentativa == letra):
                                        letras_acertadas[index] = letra
                                    index +=1
                                clean()
                                break
                            else:
                                erros = erros + 1
                                dieguy(erros)
                                break
                        else:print("Hein! isso Não é uma Letra!\n")
                    else:
                        print("Já se esqueceu ?? , Você já usou essa Letra !!!!!\n")

            elif escolha == "2":
                if dicasPedidas < 3:
                    print(f"Dica {dicasPedidas+1}: {dicas[dicasPedidas]}\n")
                    dicasPedidas +=1
                    while True:
                        tentativa = (input("Tente alguma Letra: "))
                        tentativa = letrasvazias(tentativa)
                        if not tentativa in letrasTentadas:
                            if tentativa.isalpha():
                                letrasTentadas.append(tentativa)
                                if (tentativa in listChave):
                                    index = 0
                                    for letra in listChave:
                                        if (tentativa == letra):
                                            letras_acertadas[index] = letra
                                        index += 1
                                    clean()
                                    break
                                else:
                                    erros = erros + 1
                                    dieguy(erros)
                                    break
                            else: print("Hein! isso Não é uma Letra!\n")
                        else: print("Já se esqueceu ?? , Você já usou essa Letra !!!!!\n")
                else:
                    clean()
                    print("Você não pode mais pedir um 'HELP' :\n")
            else:
                letrasvazias()
                print("Você sabe que tem que escolher alguma opção né ??\n")
                
        while True:
            clean()
            try:
                print("\n")
                historico = open('Histórico.txt','w')
                historico.write(vitorioso + "\n")
                historico.close()

                historico = open('Histórico.txt','r')
                clean()
                print("Histórico de Jogos:\n")
                for linha in historico:
                    linha = linha.rstrip()
                    print (linha)
                historico.close()
                print()
                break
            except:
                historico = open('Histórico.txt','w')
                historico.close()

    elif(comando == "2"):
        print("Vai sair tão cedo ??")
        time.sleep(2)
        break

    else:
        clean()
        print("Escolha uma Opção para começar!! \n")



    

       
       
       
    



