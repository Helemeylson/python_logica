while True:
    nome = input("informe seu nome")
    idade = int(input("informe sua idade:"))
    result = "é maior de idade." if idade >= 18 else "é menor de idade"
    print(f"{nome} {result}")

    repetir= input("deseja vrificar de novo? (s/n) ").lower().strip()
    match repetir:
        case "s":
            continue
        case "n":
            break
        case _:
            print("opção invalida.")
            break 