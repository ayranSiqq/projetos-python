while True:
    n1 = float(input("Digite o primeiro termo:"))
    ope = input("Digite a operação desejada:")
    n2 = float(input("Digite o segundo termo:"))

    if ope == "+":
        R = n1 + n2
        print("O resultado é:", R)
    elif ope == "-":
        R = n1 - n2
        print("O resultado é:", R)
    elif ope == "*":
        R = n1 * n2
        print("O resultado é:", R)
    elif ope == "/":
        R = n1 / n2
        print("O resultado é:", R)
    else:    print("Operação inválida!")
 
    print("Obrigado por usar a calculadora! Deseja continuar a operação ou realizar outra? para continuar, digite 'sim', para realizar outra operação, digite 'outra'.")
    escolha = input("Digite sua escolha:")

    if escolha == "sim":
        while True:
            ope = input("Digite a operação desejada:")
            n3 = float(input("Digite o próximo termo:"))
            if ope == "+":
                R= R + n3
                print("O resultado é:", R)
            elif ope == "-":
                R = R - n3
                print("O resultado é:", R)
            elif ope == "*":
                R = R * n3
                print("O resultado é:", R) 
            elif ope == "/":
                R = R / n3
                print("O resultado é:", R) 
            elif input == "outra":
                continue