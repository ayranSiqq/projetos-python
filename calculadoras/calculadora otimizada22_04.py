import math
print("potenciação: **, raiz quadrada: r")
Novo = True
while True:
    if Novo:
        try:
            n1 = float(input("Digite o primeiro termo:"))
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")
            continue
    ope = input("Digite a operação desejada, ou 'não' para sair: ")
    if ope == "não":
        Novo = True
        continue
    if ope != "r":
        try:
            n2 = float(input("Digite o segundo termo:"))
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")
            continue

    if ope == "+":
        R = n1 + n2
        print("O resultado é:", R)
    elif ope == "%":
        R = n1 * (n2 / 100)
        print("O resultado é:", R)
    elif ope == "-":
        R = n1 - n2
        print("O resultado é:", R)
    elif ope == "*":
        R = n1 * n2
        print("O resultado é:", R)
    elif ope == "/":
        if n2 == 0:
            print("Erro: divisão por zero!")
            continue
        R = n1 / n2
        print("O resultado é:", R)
    elif ope == "**":
        R = n1 ** n2
        print("O resultado é:", R)
    elif ope == "r":
        R = n1 ** 0.5   
        print("O resultado é:", R) 
    elif ope == "log":
        if n1 <= 0:
            print("Erro: logaritmo inválido!")
            continue
        R = math.log10(n1)
        print("O resultado é:", R)
    else:
        print("Operação inválida!")
        continue
    n1 = R
    Novo = False
