def tabela_juros_simples(valor_emprestado, taxa_juros, num_meses):
    saldo_devedor = valor_emprestado / num_meses
    print(f"\nTabela de Pagamento - Juros Simples")
    print("Mês\tJuros\t\tSaldo Devedor")
    
    for mes in range(1, num_meses + 1):
        juros = valor_emprestado * (taxa_juros / 100) * mes
        saldo_devedor = valor_emprestado / num_meses + juros
        print(f"{mes}\tR$ {juros:.2f}\tR$ {saldo_devedor:.2f}")
    
    return saldo_devedor

def tabela_juros_compostos(valor_emprestado, taxa_juros, num_meses):
    saldo_devedor = valor_emprestado / num_meses
    print(f"\nTabela de Pagamento - Juros Compostos")
    print("Mês\tJuros\t\tSaldo Devedor")
    
    for mes in range(1, num_meses + 1):
        juros = saldo_devedor * (taxa_juros / 100)
        saldo_devedor += juros
        print(f"{mes}\tR$ {juros:.2f}\tR$ {saldo_devedor:.2f}")
    
    return saldo_devedor

def tabela_amortizacao(valor_emprestado, taxa_juros, num_meses):
    amortizacao = valor_emprestado / num_meses
    saldo_devedor = valor_emprestado
    print(f"\nTabela de Pagamento - Amortização")
    print("Mês\tAmortização\tJuros\t\tParcela\t\tSaldo Devedor")
    
    for mes in range(1, num_meses + 1):
        juros = saldo_devedor * (taxa_juros / 100)
        parcela = amortizacao + juros
        saldo_devedor -= amortizacao
        print(f"{mes}\tR$ {amortizacao:.2f}\t\tR$ {juros:.2f}\tR$ {parcela:.2f}\tR$ {saldo_devedor:.2f}")
    
    return saldo_devedor

def main():
    print("Escolha o tipo de cálculo para a tabela de pagamento de dívida:")
    print("1. Juros Simples")
    print("2. Juros Compostos")
    print("3. Amortização")
    
    opcao = int(input("Digite o número correspondente à sua escolha: "))
    
    valor_emprestado = float(input("Digite o valor emprestado: R$ ").replace(',', '.'))
    taxa_juros = float(input("Digite a taxa de juros mensal (%): ").replace(',', '.').replace('%', ''))
    num_meses = int(input("Digite o número de meses: "))
    
    if opcao == 1:
        tabela_juros_simples(valor_emprestado, taxa_juros, num_meses)
    elif opcao == 2:
        tabela_juros_compostos(valor_emprestado, taxa_juros, num_meses)
    elif opcao == 3:
        tabela_amortizacao(valor_emprestado, taxa_juros, num_meses)
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

# Executa o programa
main()

input()
