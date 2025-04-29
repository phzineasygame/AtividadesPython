def verificar_par_ou_impar(valor):
    try:

        numero = int(valor)


        if numero % 2 == 0:
            return True
        else:
            return False
    except ValueError:

        return ()"Valor inválido. Informe um número inteiro.")

