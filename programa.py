def calcular_btu(largura, comprimento, altura, pessoas, lampadas, equipamentos, isolamento, espessura, k_material, delta_t):
    volume = largura * comprimento * altura
    
    area_paredes = 2 * (largura * altura + comprimento * altura) 
    area_teto_piso = 2 * (largura * comprimento) 
    area_total = area_paredes + area_teto_piso

    conducao_calor = (k_material * area_paredes * delta_t) / espessura 

    carga_base = largura * comprimento * 600

    calor_pessoas = pessoas * 100

    calor_lampadas = lampadas * 70

    calor_equipamentos = equipamentos * 500

    if isolamento:
        fator_isolamento = 0.9 
    else:
        fator_isolamento = 1.2 

    capacidade_total = (carga_base + calor_pessoas + calor_lampadas + calor_equipamentos + conducao_calor) * fator_isolamento
    
    return capacidade_total, volume, area_total


def exibir_menu_principal():
    print("""
****************************************************
*        SISTEMA DE DIMENSIONAMENTO DE AR          *
*                CONDICIONADO                      *
****************************************************
""")

def menu_selecao_material():
    while True:
        print("""
****************************************************
*       SELEÇÃO DO MATERIAL DA PAREDE             *
****************************************************
1. Concreto (k = 1.7 W/m·K)
2. Tijolo (k = 0.7 W/m·K)
3. Madeira (k = 0.12 W/m·K)
****************************************************
""")
        try:
            opcao = int(input("Escolha o número correspondente ao material: "))
            if opcao == 1:
                return 1.7 
            elif opcao == 2:
                return 0.7  
            elif opcao == 3:
                return 0.12  
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print("Opção inválida! Tente novamente.")

def menu_selecao_lampadas():
    while True:
        print("""
****************************************************
*       SELEÇÃO DO TIPO DE LÂMPADA                *
****************************************************
1. Lâmpada Incandescente (70W)
2. Lâmpada Fluorescente (40W)
3. Lâmpada LED (15W)
****************************************************
""")
        try:
            opcao = int(input("Escolha o número correspondente ao tipo de lâmpada: "))
            if opcao == 1:
                return 70 
            elif opcao == 2:
                return 40  
            elif opcao == 3:
                return 15 
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print("Opção inválida! Tente novamente.")


exibir_menu_principal()

print("Por favor, insira as informações do ambiente:\n")

largura = float(input("Digite a largura do ambiente em metros: "))
comprimento = float(input("Digite o comprimento do ambiente em metros: "))
altura = float(input("Digite a altura do ambiente em metros: "))
pessoas = int(input("Digite o número de pessoas geralmente presentes no ambiente: "))
equipamentos = int(input("Digite o número de equipamentos no ambiente: "))
isolamento = input("O ambiente possui isolamento térmico? (sim/não): ").strip().lower() == "sim"
espessura = float(input("Digite a espessura das paredes em metros (exemplo: 0.3 para 30 cm): "))
delta_t = float(input("Digite a diferença de temperatura entre o ambiente interno e externo (em °C): "))

lampadas = int(input("Digite o número de lâmpadas no ambiente: "))
tipo_lampada = menu_selecao_lampadas()
lampadas *= tipo_lampada / 70 

k_material = menu_selecao_material()

btu_necessario, volume, area_total = calcular_btu(largura, comprimento, altura, pessoas, lampadas, equipamentos, isolamento, espessura, k_material, delta_t)

print(f"""
****************************************************
* A capacidade necessária do ar-condicionado é:    *
****************************************************      
*           {btu_necessario:.2f} BTUs              
* Volume do ambiente: {volume:.2f} m³              
* Área total do ambiente: {area_total:.2f} m²       
****************************************************
""")
