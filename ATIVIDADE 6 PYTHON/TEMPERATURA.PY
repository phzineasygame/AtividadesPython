def calcular_temperaturas():
    try:

        temp_maxima = float(input("Digite a temperatura máxima do dia: "))
        temp_minima = float(input("Digite a temperatura mínima do dia: "))


        media_temperatura = (temp_maxima + temp_minima) / 2
        variacao_temperatura = temp_maxima - temp_minima

        print(f"\nMédia entre a temperatura máxima e mínima: {media_temperatura:.2f}°C")
        print(f"Variação entre as temperaturas: {variacao_temperatura:.2f}°C")

    except ValueError:
        print("Valor informado inválido! Por favor, insira um número decimal ou inteiro.")

def somar_digitos():
    try:

        numero = input("Digite um número: ")


        if not numero.isdigit():
            raise ValueError("Valor informado não é um número inteiro.")


        soma_digitos = sum(int(digito) for digito in numero)

        print(f"A soma dos dígitos do número é: {soma_digitos}")

    except ValueError as e:
        print(e)


calcular_temperaturas()
somar_digitos()
