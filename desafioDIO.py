import sys

def analise_vendas(vendas):
    # Calcular o total de vendas
    total_vendas = sum(vendas)
    
    # Calcular a média mensal de vendas
    media_vendas = total_vendas / len(vendas)
    
    # Retornar o total de vendas e a média formatados
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas(entrada):
    # Divide a string de entrada em uma lista de strings
    lista_strings = entrada.split(',')
    
    # Remove espaços em branco e converte a lista de strings em uma lista de inteiros
    lista_inteiros = list(map(int, [s.strip() for s in lista_strings]))
    
    return lista_inteiros

# Lendo a entrada do usuário com sys.stdin.readline()
entrada = sys.stdin.readline().strip()

# Obter a lista de vendas a partir da entrada
vendas = obter_entrada_vendas(entrada)

# Imprimir a análise de vendas
print(analise_vendas(vendas))
