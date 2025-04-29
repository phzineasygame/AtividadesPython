def comentar_idade(idade):
    try:
        
        idade = int(idade)

        if idade < 0:
            return "Valor inválido. A idade não pode ser negativa."

        if idade < 18:
            return "Você é menor de idade."
        elif 18 <= idade <= 59:
            return "Você é adulto."
        else:
            return "Você é idoso."
    except ValueError:
        return "Valor inválido. Por favor, insira um número válido para a idade."

idade_usuario = input("Digite sua idade: ")

resultado = comentar_idade(idade_usuario)
print(resultado)