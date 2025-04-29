def calculadora():

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        
        soma = num1 + num2
        subtracao = num1 - num2
        multiplicacao = num1 * num2

        
        if num2 == 0:
            divisao = "Não é possível dividir por zero."
        else:
            divisao = num1 / num2

        
        print(f"\nResultado das operações:")
        print(f"Soma: {num1} + {num2} = {soma}")
        print(f"Subtração: {num1} - {num2} = {subtracao}")
        print(f"Multiplicação: {num1} * {num2} = {multiplicacao}")
        print(f"Divisão: {num1} / {num2} = {divisao}")

    except ValueError:
        print("Erro: Por favor, insira apenas números válidos.")


calculadora()