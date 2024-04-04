# Inicializa variáveis para armazenar a quantidade, soma e média
quantidade_numeros = 0
soma_numeros = 0

# Loop para ler os números do teclado
while True:
    # Lê o número do teclado
    numero = int(input("Digite um número inteiro (digite 0 para encerrar): "))
    
    # Verifica se o número é zero para encerrar o loop
    if numero == 0:
        break
    
    # Incrementa a quantidade de números
    quantidade_numeros += 1
    
    # Adiciona o número à soma
    soma_numeros += numero

# Verifica se foram digitados números
if quantidade_numeros > 0:
    # Calcula a média aritmética
    media = soma_numeros / quantidade_numeros
    # Exibe os resultados
    print("Quantidade de números digitados:", quantidade_numeros)
    print("Soma dos números:", soma_numeros)
    print("Média aritmética dos números:", media)
else:
    print("Nenhum número foi digitado.")
