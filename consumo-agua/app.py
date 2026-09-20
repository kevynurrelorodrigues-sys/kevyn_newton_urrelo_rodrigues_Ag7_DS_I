# obtendo dados 
imovel = input("qual o tipo do seu imovel? comercial, casa ou apartamento?: ").lower() 

consumo_mensal = input("qual o consumo mensal em m³(ex: 10.5m³)?: ")
# 1. Validação inicial usando 'not' para verificar se os campos estão vazios
if not imovel or not consumo_mensal:
    print("Por favor, preencha todos os campos.")

# 2. Validação para garantir que o tipo de imóvel digitado é válido
elif imovel not in ("comercial", "casa", "apartamento"):
    print("Tipo de imóvel inválido. Escolha entre comercial, casa ou apartamento.")
else:
   try:
        # Tenta limpar a string e convertê-la para número
        consumo_limpo = float(consumo_mensal.lower().replace('m³', '').replace('M³', '').strip())
        
        # O processamento e as condições ficam aqui dentro do try
        if imovel == "comercial":
            print("Tarifa comercial aplicada - consulte o plano corporativo.")
        elif imovel == "apartamento" and consumo_limpo <= 10:
            print("consumo economico - excelente consumo de agua.")
        elif (imovel == "apartamento" or imovel == "casa") and consumo_limpo <= 25:
            print("Consumo moderado - dentro do padrão residencial.")
        elif consumo_limpo > 25:  # consumo acima do limite residencial
            print("Consumo excessivo - adote medidas de economia e verifique vazamentos.")
            
   except ValueError:
        # Se o utilizador digitar letras (como 'hfttd'), o Python cai aqui em vez de crashar
        print("Erro: Por favor, insira um valor numérico válido para o consumo (ex: 10.5).")