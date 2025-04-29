def dolares_para_float(d):
    return float(d.replace("$", ""))
def percentual_para_float(p):
    return float(p.replace("%", "")) / 100
dolares = dolares_para_float(input("Quanto que custou a comida? "))
percentual = percentual_para_float(input("Quantos % você gostaria de deixar de gorjeta? "))
gorjeta = dolares * percentual
print(f"Deixe ${gorjeta:.2f}")
