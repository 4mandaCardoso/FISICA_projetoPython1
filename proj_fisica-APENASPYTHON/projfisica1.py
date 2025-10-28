import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import math
import os # usado apenas para limpar a tela


def limpar_tela(tipo):
    if tipo == 1:
        try:
         os.system('cls' if os.name == 'nt' else 'clear')
        except:
         pass
    else:
        print("\n")
        qualquertecla=input("Pressione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')

#------------------------------- VETORES --------------------------------

# Funções para Operações Vetoriais
def calcular_soma_vetorial(v1, v2):
     return [v1[0] + v2[0], v1[1] + v2[1]]
def calcular_subtracao_vetorial(v1, v2):
     return [v1[0] - v2[0], v1[1] - v2[1]]
def calcular_produto_escalar(v1, v2):
     return v1[0] * v2[0] + v1[1] * v2[1]
def calcular_modulo(v1):
     return math.sqrt(v1[0]**2 + v1[1]**2)
def calcular_produto_vetorial(v1, v2):
     return v1[0] * v2[1] - v1[1] * v2[0]
# Gráfico de Vetores
def plotar_vetores(v1, v2=None, v_resultante=None, titulo_grafico="Visualização de Vetores", is_3d=False):
    figura = plt.figure(figsize=(6, 6))
    if is_3d:
        eixos = figura.add_subplot(111, projection='3d')
        todos_componentes = v1 + v2 + (v_resultante if v_resultante else [])
        max_abs_val = max([abs(c) for c in todos_componentes] + [1]) * 1.2
        eixos.set_xlim([-max_abs_val, max_abs_val])
        eixos.set_ylim([-max_abs_val, max_abs_val])
        eixos.set_zlim([-max_abs_val, max_abs_val])
        eixos.set_xlabel('X')
        eixos.set_ylabel('Y')
        eixos.set_zlabel('Z')
        origem = [0, 0, 0]
        eixos.quiver(*origem, *v1, color='blue', arrow_length_ratio=0.1)
        eixos.quiver(*origem, *v2, color='green', arrow_length_ratio=0.1)
        if v_resultante:
            eixos.quiver(*origem, *v_resultante, color='red', arrow_length_ratio=0.1)
    else:
        eixos = figura.add_subplot(111)
        if v2 is not None:
            todos_componentes = v1 + v2 + (v_resultante if v_resultante else [])
        else:
            todos_componentes = v1 + (v_resultante if v_resultante else [])
        max_abs_val = max([abs(c) for c in todos_componentes] + [1]) * 1.2
        eixos.set_xlim([-max_abs_val, max_abs_val])
        eixos.set_ylim([-max_abs_val, max_abs_val])
        eixos.set_xlabel('X')
        eixos.set_ylabel('Y')
        eixos.axhline(0, color='gray', linewidth=0.5)
        eixos.axvline(0, color='gray', linewidth=0.5)
        eixos.set_aspect('equal', adjustable='box')
        eixos.arrow(0, 0, v1[0], v1[1], head_width=max_abs_val*0.05, head_length=max_abs_val*0.07, fc='blue', ec='blue', linewidth=1.5)
        if v2 is not None:
         eixos.arrow(0, 0, v2[0], v2[1], head_width=max_abs_val*0.05, head_length=max_abs_val*0.07, fc='green', ec='green', linewidth=1.5)
        if v_resultante:
            eixos.arrow(0, 0, v_resultante[0], v_resultante[1], head_width=max_abs_val*0.05, head_length=max_abs_val*0.07, fc='red', ec='red', linewidth=1.5)

    legendas = [
        mpatches.Patch(color='blue', label='Vetor 1'),
        mpatches.Patch(color='green', label='Vetor 2')
    ]
    if v_resultante:
        legendas.append(mpatches.Patch(color='red', label='Vetor Resultante'))
    eixos.legend(handles=legendas)

    eixos.set_title(titulo_grafico)
    eixos.grid(True)
    plt.show()

#--------------------------------------------------------------------------------------
#------------------------------- CONVERSÃO DE UNIDADES --------------------------------

#Dicionários de fatores de conversão para cada área
fatores_comprimento = {
    "km": 1000,
    "hm": 100,
    "dam": 10,  
    "m": 1,
    "dm": 0.1,
    "cm": 0.01,
    "mm": 0.001
}
fatores_massa = {
    "t": 1000,
    "kg": 1,
    "hg": 0.1,
    "dag": 0.01,
    "g": 0.001,
    "dg": 0.0001,
    "cg": 0.00001,
    "mg": 0.000001
}
fatores_tempo = {
    "h": 3600,
    "min": 60,
    "s": 1,
    "ms": 0.001
}
fatores_corrente = {
    "kA": 1000,
    "A": 1,
    "mA": 0.001,
    "µA": 0.000001
}
fatores_luz = {
    "kcd": 1000,
    "cd": 1,
    "mcd": 0.001
}
fatores_quantidade = {
    "kmol": 1000,
    "mol": 1,
    "mmol": 0.001
}

fatores_velocidade = {
    "m/s":1,
    "km/h": 1/3.6
}

fatores_temp = {
    "°C": 1,  # referência arbitrária
    "K": 1,   # lidaremos com temperatura de modo especial
    "°F": 1
}


fatores_lista = {
    1: fatores_comprimento,
    2: fatores_massa,
    3: fatores_tempo,
    4: fatores_corrente,
    5: fatores_luz,
    6: fatores_quantidade,
    7: fatores_temp,
    8: fatores_velocidade
}


# Funções para Conversão de Unidades
def escolha_unidade (tipo,ordem):
    fatores = fatores_lista [tipo]
    opcoes = list(fatores.keys())

    if ordem == 1:
        for i in range(1,len(fatores)+1):
            print(f" {i}. {list(fatores.keys())[i-1]}")
    else: 
        return opcoes



def converter (valor, unidade_de, unidade_para,tipo):
    if tipo == 7:  # Temperatura
        if unidade_de == "°C" and unidade_para == "K":
            return valor + 273.15
        elif unidade_de == "K" and unidade_para == "°C":
            return valor - 273.15
        elif unidade_de == "°C" and unidade_para == "°F":
            return (valor * 9/5) + 32
        elif unidade_de == "°F" and unidade_para == "°C":
            return (valor - 32) * 5/9
        elif unidade_de == "K" and unidade_para == "°F":
            return (valor - 273.15) * 9/5 + 32
        elif unidade_de == "°F" and unidade_para == "K":
            return (valor - 32) * 5/9 + 273.15
        else:
            return valor
    else:
        fatores = fatores_lista[tipo]

    valor_em_base = valor * fatores[unidade_de]
    valor_convertido = valor_em_base / fatores[unidade_para]
    return valor_convertido


#--------------------------------------------------------------------------------------
#------------------------------- FUNÇÃO PRINCIPAL -------------------------------------
escolha = 0
while escolha != '3':
    escolha = 0
    print("\n======================= Projeto 1 de Física =======================")
    print("Desenvolvido por: Amanda Cardoso, Hannah França e Mariana Assunção")
    print("-------------------------------------------------------------------")
    print("Selecione a funcionalidade desejada:")
    print("1. Operações Vetoriais")
    print("2. Conversão de Unidades")
    print("3. Sair\n")
    escolha = input(" - Digite o número da opção desejada: ")
    
    if escolha == '1':
        limpar_tela(1)
        print("-----------------------------------------------------------")
        print("=================== Operações Vetoriais ===================")
        print("Escolha a operação vetorial desejada:")
        print("1. Soma Vetorial")
        print("2. Subtração Vetorial")
        print("3. Produto Escalar")
        print("4. Módulo de um Vetor")
        print("5. Produto Vetorial\n")
        try: 
            operacao = input(" -        Digite o número da operação desejada: ")
            if operacao not in ['1','2','3','4','5']:
                 print("Operação inválida. Retornando ao menu principal.")
                 limpar_tela(2)
                 continue
        except ValueError:
            print("Entrada inválida. Retornando ao menu principal.")
            limpar_tela(2)
            continue
        if operacao == '4':
            limpar_tela(1)
            print("\n\nDigite os componentes de um vetor: \n")
            print("--------------------------------------------")
            x = float(input("Digite a componente X do vetor: "))
            y = float(input("Digite a componente Y do vetor: "))
            v1 = [x, y]
            print(f"O valor do módulo do vetor {v1} :\n {calcular_modulo(v1):.2f}")
            plotar_vetores(v1,None,None,"Módulo do Vetor",is_3d=False)
            limpar_tela(2)
        else:
            limpar_tela(1)
            print("\n\nDigite as componentes dos dois vetores:\n")
            print("--------------------------------------------")
            for i in range(2):
                x = float(input(f"Digite a componente X do vetor {i+1}: "))
                y = float(input(f"Digite a componente Y do vetor {i+1}: "))
                print(" - ")
                if i == 0:
                  v1 = [x, y]
                else:
                  v2 = [x, y]
            limpar_tela(1)
        if operacao == '1':
            vresultante = calcular_soma_vetorial(v1, v2)
            print(f"\nResultado da Soma Vetorial: {vresultante}")
            plotar_vetores(v1, v2, vresultante, "Soma Vetorial", is_3d=False)
            limpar_tela(2)
        elif operacao == '2':
            vresultante = calcular_subtracao_vetorial(v1, v2)
            print(f"\nResultado da Subtração Vetorial: {vresultante}")
            plotar_vetores(v1, v2, vresultante, "Subtração Vetorial", is_3d=False)
            limpar_tela(2)
        elif operacao == '3':
            resultado = calcular_produto_escalar(v1, v2)
            print(f"\nResultado do Produto Escalar: {resultado}")
            plotar_vetores(v1,v2,None,"Produto Escalar", is_3d=False)
            limpar_tela(2)
        elif operacao == '5':
            resultado = calcular_produto_vetorial(v1, v2)
            v1_3d = v1 + [0]
            v2_3d = v2 + [0]
            vresultante = [0,0,resultado]
            print(f"\nResultado do Produto Vetorial: {resultado}")
            plotar_vetores(v1_3d, v2_3d, vresultante, "Produto Vetorial", is_3d=True)
            limpar_tela(2)
        



    elif escolha == '2':
        limpar_tela(1)
        print("\n-------------------------------------------------------------")
        print("=================== Conversão de Unidades ===================")
        print("Selecione o tipo de unidade que deseja converter")
        print("1. Comprimento")
        print("2. Massa")
        print("3. Tempo")
        print("4. Corrente Elétrica")
        print("5. Intensidade Luminosa")
        print("6. Quantidade de Matéria")
        print("7. Temperatura")
        print("8. Velocidade\n")
        try:
            tipo = int(input(" - Digite o número do tipo de unidade desejada: "))
            if tipo not in range(1,9):
                print("Tipo inválido. Retornando ao menu principal.")
                limpar_tela(2)
                continue
        except ValueError:
            print("Entrada inválida. Retornando ao menu principal.")
            limpar_tela(2)
            continue
        limpar_tela(1)
        escolha_unidade(tipo, 1)
        opcoes = escolha_unidade(tipo, 2)
        print("\nDigite de qual unidade para qual unidade deseja converter:\n")

        ok = 0
        while ok == 0:
            unidade_de = int(input("Digite o número da unidade atual: ")) - 1
            if unidade_de < 0 or unidade_de >= len(opcoes):
                print("Opção não existente.")
                limpar_tela(2)
                escolha_unidade(tipo,1)
                print("\n")
            else:
                  ok = 1

        ok = 0
        while ok == 0:
             unidade_para = int(input("Digite o número da unidade para a qual deseja converter: ")) - 1
             if unidade_para < 0 or unidade_para >= len(opcoes):
                print("Opção não existente.")
                limpar_tela(2)
                escolha_unidade(tipo,1)
                print("\n")
             else:
                 ok = 1

        valor = float(input("Digite o valor a ser convertido: "))
        unidade_de = opcoes[unidade_de]
        unidade_para = opcoes[unidade_para]

        try:
            valor_convertido = converter(valor, unidade_de, unidade_para, tipo)
            limpar_tela(1)
            print(f"\n O valor digitado foi: {valor} {unidade_de}\n")
            print(f" valor convertido é: {valor_convertido:.2f} {unidade_para}\n")
            limpar_tela(2)
        except KeyError:
            print("Unidade inválida. Retornando ao menu principal.")
            continue
    elif escolha == '3':
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")