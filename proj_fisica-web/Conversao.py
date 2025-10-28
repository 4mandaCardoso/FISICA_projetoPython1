from js import document, window
from pyodide.ffi import create_proxy

# Definição das unidades de medida para cada área - PÁGINA DE CONVERSÃO
comprimento = ["km", "hm", "dam", "m", "dm", "cm", "mm"]
massa = ["t", "kg", "hg", "dag", "g", "dg", "cg", "mg"]
temperatura = ["°C", "K", "°F"]
tempo = ["h", "min", "s", "ms"]
corrente = ["kA", "A", "mA", "µA"]
luz = ["kcd", "cd", "mcd"]
quantidade = ["kmol", "mol", "mmol"]
velocidade = ["m/s","km/h"]

area_unidades = {
    "Comprimento": comprimento,
    "Massa": massa,
    "Temperatura": temperatura,
    "Tempo": tempo,
    "Corrente Elétrica": corrente,
    "Intensidade Luminosa": luz,
    "Quantidade de Substância": quantidade,
    "Velocidade": velocidade
}
# Função para atualizar as unidades disponíveis com base no tipo selecionado - PÁGINA DE CONVERSÃO
def atualizar_unidades(event):
    # Obtém o tipo selecionado
    tipo = document.getElementById("tipo").value
    unidade_de = document.getElementById("unidade-de")
    unidade_para = document.getElementById("unidade-para")
    # Limpa as opções atuais
    unidade_de.innerHTML = ""
    unidade_para.innerHTML = ""
    # Adiciona as novas opções com base no tipo selecionado
    for unidade in area_unidades[tipo]:
        # Cria e adiciona a opção para "De"
        option_de = document.createElement("option")
        option_de.value = unidade
        option_de.text = unidade
        unidade_de.add(option_de)
        # Cria e adiciona a opção para "Para"
        option_para = document.createElement("option")
        option_para.value = unidade
        option_para.text = unidade
        unidade_para.add(option_para)
# Faz com que as unidades sejam atualizadas ao carregar a página
atualizar_unidades(None)
tipo_element = document.getElementById("tipo")
#faz com que o evento de mudança chame a função de atualização
tipo_element.addEventListener("change", create_proxy(atualizar_unidades))

#Todas essas funções são unicamente para definir o que o usuário irá escolher na tela. Elas não fazem cálculos.
# Vale dizer que "document.getElementById" pega o valor escolhido no HTML e manda para o python.
#---------------------------------------------------

#Dicionários de fatores de conversão para cada área - PÁGINA DE CONVERSÃO
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
    "m/s": 1,
    "km/h": 1/3.6
}

# Função para realizar a conversão - PÁGINA DE CONVERSÃO
def converter(event):
    tipo = document.getElementById("tipo").value
    unidade_de = document.getElementById("unidade-de").value
    unidade_para = document.getElementById("unidade-para").value
    valor_input = document.getElementById("valor").value

    try:
        valor = float(valor_input)
    except ValueError:
        window.alert("Por favor, insira um valor numérico válido.")
        return

    if tipo == "Temperatura":
        if unidade_de == "°C":
            if unidade_para == "K":
                resultado = valor + 273.15
            elif unidade_para == "°F":
                resultado = (valor * 9/5) + 32
            else:
                resultado = valor
        elif unidade_de == "K":
            if unidade_para == "°C":
                resultado = valor - 273.15
            elif unidade_para == "°F":
                resultado = (valor - 273.15) * 9/5 + 32
            else:
                resultado = valor
        elif unidade_de == "°F":
            if unidade_para == "°C":
                resultado = (valor - 32) * 5/9
            elif unidade_para == "K":
                resultado = (valor - 32) * 5/9 + 273.15
            else:
                resultado = valor
    else:
        if tipo == "Comprimento":
            fatores = fatores_comprimento
        elif tipo == "Massa":
            fatores = fatores_massa
        elif tipo == "Tempo":
            fatores = fatores_tempo
        elif tipo == "Corrente Elétrica":
            fatores = fatores_corrente
        elif tipo == "Intensidade Luminosa":
            fatores = fatores_luz
        elif tipo == "Quantidade de Substância":
            fatores = fatores_quantidade
        elif tipo == "Velocidade":
            fatores = fatores_velocidade

        valor_em_base = valor * fatores[unidade_de]
        resultado = valor_em_base / fatores[unidade_para]

    resultado_element = document.getElementById("resultado-texto")
    resultado_element.innerHTML = f"{valor} {unidade_de} é igual a {resultado:.2f} {unidade_para}"
# Adiciona o evento ao botão de conversão - PÁGINA DE CONVERSÃO
botao_converter = document.getElementById("botao-converter")
botao_converter.addEventListener("click", create_proxy(converter))
#---------------------------------------------------
# O código acima é responsável por realizar conversões de unidades de medida em todas as áreas citadas
# em Halliday Resnick - Física - Volume 1  em seu capitulo sobre conversão de unidades.