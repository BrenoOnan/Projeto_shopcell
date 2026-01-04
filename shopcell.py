import time

celulares = {
    # iPhone XR
    "IPHONEXR": {"Codigo": "01", "Quantidade": 5, "Memória": "64GB", "Valor": 1200},
    "IPHONEXRPLUS": {"Codigo": "02", "Quantidade": 3, "Memória": "128GB", "Valor": 1400},

    # iPhone 11
    "IPHONE11": {"Codigo": "03", "Quantidade": 4, "Memória": "64GB", "Valor": 1500},
    "IPHONE11PRO": {"Codigo": "04", "Quantidade": 3, "Memória": "128GB", "Valor": 2000},
    "IPHONE11PROMAX": {"Codigo": "05", "Quantidade": 2, "Memória": "256GB", "Valor": 2500},

    # iPhone 12
    "IPHONE12": {"Codigo": "06", "Quantidade": 5, "Memória": "64GB", "Valor": 1600},
    "IPHONE12PRO": {"Codigo": "07", "Quantidade": 4, "Memória": "128GB", "Valor": 2400},
    "IPHONE12PROMAX": {"Codigo": "08", "Quantidade": 2, "Memória": "256GB", "Valor": 2800},

    # iPhone 13
    "IPHONE13": {"Codigo": "09", "Quantidade": 5, "Memória": "128GB", "Valor": 3000},
    "IPHONE13PRO": {"Codigo": "10", "Quantidade": 3, "Memória": "128GB", "Valor": 3500},
    "IPHONE13PROMAX": {"Codigo": "11", "Quantidade": 2, "Memória": "256GB", "Valor": 4000},

    # iPhone 14
    "IPHONE14": {"Codigo": "12", "Quantidade": 4, "Memória": "128GB", "Valor": 3500},
    "IPHONE14PRO": {"Codigo": "13", "Quantidade": 3, "Memória": "128GB", "Valor": 4500},
    "IPHONE14PROMAX": {"Codigo": "14", "Quantidade": 2, "Memória": "256GB", "Valor": 5000},

    # iPhone 15
    "IPHONE15": {"Codigo": "15", "Quantidade": 4, "Memória": "128GB", "Valor": 4000},
    "IPHONE15PRO": {"Codigo": "16", "Quantidade": 3, "Memória": "256GB", "Valor": 5000},
    "IPHONE15PROMAX": {"Codigo": "17", "Quantidade": 2, "Memória": "512GB", "Valor": 6000},

    # iPhone 16
    "IPHONE16": {"Codigo": "18", "Quantidade": 3, "Memória": "128GB", "Valor": 4500},
    "IPHONE16PRO": {"Codigo": "19", "Quantidade": 2, "Memória": "256GB", "Valor": 5500},
    "IPHONE16PROMAX": {"Codigo": "20", "Quantidade": 1, "Memória": "512GB", "Valor": 6500},

}


def catalogo():
    #Catalogo simples sem continuação de compra
    print("-" * 40)
    print("📱 CATALOGO DE CELULARES 📱")
    print("-" * 40)
    for nome, info in celulares.items():
        print(f"\033[30m📦 Modelo: {nome}\033[0m")
        print(f"\033[36mCODIGO:\033[0m {info['Codigo']}")
        print(f"\033[36m🔢 Quantidade:\033[0m {info['Quantidade']}")
        print(f"\033[36m💾 Memória:\033[0m {info['Memória']}")
        print(f"\033[31m💰 Valor: R$ {info['Valor']:.2f}\033[0m")
        print("-" * 40)
        time.sleep(1)


def catalogo_celular():
    try:
        #Catalogo celular oferecendo a compra
        print("📱 CATALOGO DE CELULARES 📱")
        print("-" * 40)
        for nome, info in celulares.items():
            print(f"\033[30m📦 Modelo: {nome}\033[0m")
            print(f"\033[36mCODIGO:\033[0m {info['Codigo']}")
            print(f"\033[36m🔢 Quantidade:\033[0m {info['Quantidade']}")
            print(f"\033[36m💾 Memória:\033[0m {info['Memória']}")
            print(f"\033[31m💰 Valor: R$ {info['Valor']:.2f}\033[0m")
            print("-" * 40)
            time.sleep(1)

        print('\nA hora de escolher o seu aparelho é agora! 💥')
        resp = int(input("[1] Para comprar\n[2] Menu principal\nDigite a opção: "))

        if resp == 1:
            comprar_aparelho()
        elif resp == 2:
            menu_opcoes()
        else:
            print("\033[31mOpção inválida. Tente novamente.\033[0m")
    except:
        print('\033[31mErro!\033[0m❌')
        return


def comprar_aparelho():
    #Compra do aparelho
    opcao_compra = str(input('Qual o código aparelho do seu interesse[Ex: 01] ?')).strip().upper()

    # key {info['Memória']} selecionando a chave
    for nome, info in celulares.items():
        if info['Codigo'] == opcao_compra:
            print("\n📦 Aparelho encontrado:")
            print("-" * 28)
            print(f"\033[30mModelo:\033[0m {nome}")
            print(f"\033[36mMemória:\033[0m {info['Memória']}")
            print(f"\033[36mPreço:\033[0m R$ {info['Valor']:.2f}")
            print(f"\033[36mQuantidade disponível:\033[0m {info['Quantidade']}")
            print("-" * 28)

            resp = input("Confirmar compra [S/N]? ").strip().upper()
            if resp == "S":
                if info["Quantidade"] > 0:
                    info["Quantidade"] -= 1  # ✅ Reduz 1 unidade do estoque
                    print(f"\n✅ Compra realizada com sucesso! Agora restam {info['Quantidade']} unidades.")
                else:
                    print("\n❌ Produto esgotado!")
            elif resp == "N":
                print("\nVoltando ao menu...")
                menu_opcoes()
            else:
                print("\033[31mOpção inválida.\033[0m")
            return


def troca_aparelho():
    try:
        print("-" * 52)
        print("\033[36m✨ TROQUE O SEU APARELHO E SAIA COM UM NOVO ✨\033[0m".center(57))
        print("-" * 52)

        resp = input("\nQual o seu iPhone? ").strip().upper().replace(" ", "")
        # Exemplo: "iPhone 11 Pro Max" → "IPHONE11PROMAX"

        if resp in celulares:
            info = celulares[resp]
            desconto_usado = info['Valor'] * 0.40  # 40% do valor
            print(f"\033[36m\n📦 Aparelho usado:\033[0m {resp}")
            print(f"\033[36m💵 Valor pago pelo usado (40%):\033[0m R$ {desconto_usado:.2f}")
        else:
            print("\033[31m❌ Modelo não encontrado! Verifique o nome e tente novamente.\033[0m")
        print()
        opcao = str(input('Prosseguir com a compra de um novo aparelho?[S/N]')).upper().strip()
        if opcao == "S":
            catalogo()
            comprar_aparelho()
        if opcao == "N":
            print('OBRIGADO😄!\nVoltando ao menu principal...')
            time.sleep(1)
            menu_opcoes()
    except:
        print('\033[31mErro!\033[0m❌')
        return

def menu_opcoes():
    try:
        while True:
            print('-' * 44)
            print(f'\033[36mSEJAM BEM-VINDOS A SHOPPLACE\033[0m'.center(52))
            print('-' * 44)

            print('\033[36m[1]\033[0m - Ver celulares disponíveis:')
            print('\033[36m[2]\033[0m - Comprar aparelho:')
            print('\033[36m[3]\033[0m - Fazer UPGRADE :')
            print('\033[36m[4]\033[0m - Sair do sistema:')
            print()
            opcao = input("Qual das opções acima você deseja: ").strip()

            if opcao == "1":
                catalogo_celular()
            elif opcao == "2":
                catalogo()
                comprar_aparelho()
            elif opcao == "3":
                troca_aparelho()
            elif opcao == "4":
                print("Saindo do sistema...!")
                break
            else:
                print("\033[31mOpção inválida. Tente novamente. \033[0m")
    except:
        print('\033[31mErro!\033[0m❌')
        return

menu_opcoes()