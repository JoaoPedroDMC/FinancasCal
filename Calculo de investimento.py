def calcular_investimento(investimento_inicial, contribuicao_mensal, taxa_juros, meses):
    taxa_juros = taxa_juros / 100
    valor_total = investimento_inicial
    
    for mes in range(1, meses + 1):
        valor_total += valor_total * taxa_juros
        valor_total += contribuicao_mensal
    
    return valor_total

# Entradas do usuário
print("Calculo de investimento:")
investimento_inicial = float(input("Digite o valor inicial do investimento: R$ ").replace(',', '.'))
contribuicao_mensal = float(input("Digite o valor da contribuição mensal: R$ ").replace(',', '.'))
taxa_juros = float(input("Digite a taxa de juros mensais (%): ").replace(',', '.').replace('%', ''))
meses = int(input("Digite o número de meses: "))

# Calcula o valor total
valor_final = calcular_investimento(investimento_inicial, contribuicao_mensal, taxa_juros, meses)

# Exibe o resultado
print(f"O valor final do investimento após {meses} meses será de: R$ {valor_final:.2f}")

input()