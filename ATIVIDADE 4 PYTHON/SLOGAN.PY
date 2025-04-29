def verificar_slogan(slogan, palavra_chave):
    if palavra_chave in slogan:
        print(f"Slogan adequado (palavra-chave {palavra_chave} está no slogan).")
    else:
        print(f"Slogan inadequado (palavra-chave {palavra_chave} não está no slogan).")
    num_palavras = len(slogan.split())

    if 7 <= num_palavras <= 10:
        print(f"Slogan adequado ({num_palavras} palavras).")
    else:
        print(f"Slogan inadequado ({num_palavras} palavras).")

    if slogan[0].isalpha() and slogan[-1].isalpha():
        print("Slogan adequado (início/fim com letra).")
    else:
        print("Slogan inadequado (início/fim com letra).")

    if palavra_chave in slogan and 7 <= num_palavras <= 10 and slogan[0].isalpha() and slogan[-1].isalpha():
        print(f'O slogan "{slogan}" cumpre os requisitos de slogan para o produto "bebida".')
    else:
        print("O slogan não cumpre os requisitos.")

slogan = "beba uma pepsi bem gelada e se refresque no calor!"
palavra_chave = "Pepsi"

verificar_slogan(slogan, palavra_chave)