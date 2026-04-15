seu_peso = float(input("digite seu peso: "))
sua_altura = float(input("digite sua altura: "))

#MENU
while True:
    print("1- o valor do seu IMC")
    print("2- quanto de agua voce deve beber diariamente")
    print("3- estimativa de gasto calorico de atividades fisicas")
    print("4- Se sua meta diaria de exercicios foi concluida")
    print("5- apresentar resumo diario de tudo")
    print("6- escolher de novo uma opção do menu")

    opcoes = int(input("digite qual opcao vc quer: "))
    #calculo de IMC
    if opcoes == 1:
        calculo_de_imc = seu_peso / (sua_altura * sua_altura)
        print(f"o seu IMC é {calculo_de_imc: .2f}")

    #meta diaria de hidrataçao
    elif opcoes == 2:
        calculo_de_hidra = seu_peso * 35
        print("beber ", calculo_de_hidra, "ml")


    #estimativa de gasto calorico de  ativi. fisica -met(intensidade de atividade)
    elif opcoes == 3:
        print("esses sao os valores de intensidade media de cada atividade fisica")
        print("1-descanso")
        print("2-caminhada")
        print("3-caminhada rapida")
        print("7-esportes")
        print("10-corrida")
        met = int(input("digite o valor de intensidade da sua atividade: "))
        tempo_em_horas = int(input("digite por quanto tempo você irá praticar a atividade em horas: "))
        tempo_em_min = int(input("digite os minutos que você praticou: "))
        tempo_para_calculo = tempo_em_min/60 + tempo_em_horas
        calculo_gasto_atividade = met * seu_peso * tempo_para_calculo
        print("estimativa de gasto calorico ", calculo_gasto_atividade, "kcal")



    #meta diaria de exercicios(tempo)
    elif opcoes == 4:
        meta_diaria = float(input("digite a meta diaria de tempo de exercicios: "))
        tempo_feito = float(input("digite o tempo que voce praticou o exercicio: "))
        calculo_de_meta = tempo_feito - meta_diaria
        if calculo_de_meta < 0:
                print("voce nao concluiu sua meta diaria")

        else:
            print("voce concluiu sua meta diaria")


    #seu resumo diario
    elif opcoes == 5:
        calculo_de_imc = seu_peso / (sua_altura * sua_altura)
        calculo_de_hidra = seu_peso * 35
        print("esses sao os valores de intensidade media de cada atividade fisica")
        print("1-descanso")
        print("2-caminhada")
        print("3-caminhada rapida")
        print("7-esportes")
        print("10-corrida")
        met = int(input("digite o valor de intensidade da sua atividade: "))
        tempo_em_horas = int(input("digite por quanto tempo você irá praticar a atividade em horas: "))
        tempo_em_min = int(input("digite os minutos que você praticou: "))
        tempo_para_calculo = tempo_em_min / 60 + tempo_em_horas
        calculo_gasto_atividade = met * seu_peso * tempo_para_calculo
        print("o seu indicie de massa corporal é ", calculo_de_imc, "e você deve beber diáriamente ", calculo_de_hidra, "ml, e seu gasto de caloria em atividaes físicas é ", calculo_gasto_atividade, "kcal")
    elif opcoes == 6:
        print("Finalizando programa...")
        break
    else:
        print("invalido")
