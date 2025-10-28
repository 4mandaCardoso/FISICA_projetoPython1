import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from js import document, window
from pyodide.ffi import create_proxy
from io import BytesIO
import base64

def obter_componentes_vetor(prefixo, as_3d=False):
    valor_x = document.getElementById(f"{prefixo}-x").value
    valor_y = document.getElementById(f"{prefixo}-y").value
    if valor_x == "" or valor_y == "":
        window.alert("Por favor, preencha todos os campos dos vetores.")
        return None

    try:
        x = float(valor_x)
        y = float(valor_y)
        return [x, y, 0.0] if as_3d else [x, y]
    except ValueError:
        window.alert("Por favor, insira valores numéricos válidos.")
        return None

def calcular_modulo(vetor):
    return sum(comp**2 for comp in vetor) ** 0.5

def exibir_resultado(texto):
    document.getElementById("resultado-vetores").innerHTML = texto

def calcular_soma_vetorial(evento):
    v1 = obter_componentes_vetor("vetor-0")
    v2 = obter_componentes_vetor("vetor-1")
    if v1 is None or v2 is None: return
    resultado = [v1[i] + v2[i] for i in range(len(v1))]
    exibir_resultado(
        f"Soma Vetorial: {tuple(resultado)}<br>"
        f"Módulos: |V1|={calcular_modulo(v1):.2f}, |V2|={calcular_modulo(v2):.2f}, |V1+V2|={calcular_modulo(resultado):.2f}"
    )
    plotar_vetores(v1, v2, resultado, "Soma Vetorial", is_3d=False)

def calcular_subtracao_vetorial(evento):
    v1 = obter_componentes_vetor("vetor-0")
    v2 = obter_componentes_vetor("vetor-1")
    if v1 is None or v2 is None: return
    resultado = [v1[i] - v2[i] for i in range(len(v1))]
    exibir_resultado(
        f"Subtração Vetorial (V1 - V2): {tuple(resultado)}<br>"
        f"Módulos: |V1|={calcular_modulo(v1):.2f}, |V2|={calcular_modulo(v2):.2f}, |V1-V2|={calcular_modulo(resultado):.2f}"
    )
    plotar_vetores(v1, v2, resultado, "Subtração Vetorial", is_3d=False)

def calcular_produto_escalar(evento):
    v1 = obter_componentes_vetor("vetor-0")
    v2 = obter_componentes_vetor("vetor-1")
    if v1 is None or v2 is None: return
    resultado = sum(v1[i] * v2[i] for i in range(len(v1)))
    exibir_resultado(
        f"Produto Escalar: {resultado}<br>"
        f"Módulos: |V1|={calcular_modulo(v1):.2f}, |V2|={calcular_modulo(v2):.2f}"
    )
    plotar_vetores(v1, v2, None, "Produto Escalar", is_3d=False)

def calcular_produto_vetorial(evento):
    v1 = obter_componentes_vetor("vetor-0", as_3d=True)
    v2 = obter_componentes_vetor("vetor-1", as_3d=True)
    if v1 is None or v2 is None: return
    resultado_3d = [
        v1[1]*v2[2] - v1[2]*v2[1],
        v1[2]*v2[0] - v1[0]*v2[2],
        v1[0]*v2[1] - v1[1]*v2[0]
    ]
    componente_z = resultado_3d[2]
    exibir_resultado(
        f"Produto Vetorial (V1 x V2): {tuple(resultado_3d)}<br>"
        f"Componente Z: {componente_z:.2f}<br>"
        f"Módulos: |V1|={calcular_modulo(v1):.2f}, |V2|={calcular_modulo(v2):.2f}, |V1 x V2|={calcular_modulo(resultado_3d):.2f}"
    )
    plotar_vetores(v1, v2, resultado_3d, "Produto Vetorial", is_3d=True)

def plotar_vetores(v1, v2, v_resultante=None, titulo_grafico="Visualização de Vetores", is_3d=False):
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
        todos_componentes = v1 + v2 + (v_resultante if v_resultante else [])
        max_abs_val = max([abs(c) for c in todos_componentes] + [1]) * 1.2
        eixos.set_xlim([-max_abs_val, max_abs_val])
        eixos.set_ylim([-max_abs_val, max_abs_val])
        eixos.set_xlabel('X')
        eixos.set_ylabel('Y')
        eixos.axhline(0, color='gray', linewidth=0.5)
        eixos.axvline(0, color='gray', linewidth=0.5)
        eixos.set_aspect('equal', adjustable='box')
        eixos.arrow(0, 0, v1[0], v1[1], head_width=max_abs_val*0.05, head_length=max_abs_val*0.07, fc='blue', ec='blue', linewidth=1.5)
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

    buf = BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    plt.close(figura)
    image_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    data_url = f"data:image/png;base64,{image_base64}"
    div_grafico = document.getElementById("grafico")
    div_grafico.innerHTML = ""
    img_tag = document.createElement("img")
    img_tag.src = data_url
    img_tag.style.maxWidth = "100%"
    img_tag.style.height = "auto"
    div_grafico.appendChild(img_tag)

document.getElementById("botao-soma").addEventListener("click", create_proxy(calcular_soma_vetorial))
document.getElementById("botao-subtracao").addEventListener("click", create_proxy(calcular_subtracao_vetorial))
document.getElementById("botao-produto-escalar").addEventListener("click", create_proxy(calcular_produto_escalar))
document.getElementById("botao-produto-vetorial").addEventListener("click", create_proxy(calcular_produto_vetorial))
