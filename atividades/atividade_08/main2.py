import os

def quadrado():
    a = 1**2
    return a

def retangulo(b, h):
    a = b*h
    return a

def triangulo(b,h):
    a= (b*h)/2
    return a

def trapezio(B,b,h):
    a = ((B+b)*h)/2
    return a


while True:
    try:
        print("menu")
        print("1 calcular_área_de_um_quadrado")
        print("2 calcular_área_de_um_retangulo")
        print("3 calcular_área_de_um_triangulo")
        print("4 calcular_área_de_um_trapezio")
        print("5 sair do programa")

        opcao = input("informe a opção desejada: ").strip()
        match opcao:
            case "1":
                1 = float(input("informe o valor do lado do quadrado").replace(",",".)"))
                os.system("cls" if os.name== "nt" else "clear")
                area = quadrado(1)
                print(f"a área do quadrado é {area}")
            case "2":
                b = float(input("informe o valor da base do retangulo: ")).replace(",",".")
                h = float(input("informe o valor da altura do retângulo: ")).replace(",",".")
                area = retangulo(b,h)
                print(f"a area do retangulo é {area}.")
                continue
            case "3":
                b = float(input("informe o valor da base do triangulo")).replace(",",".")
                h = float(input("informe o valor da altura do triangulo")).replace(",",".")
                area = triangulo(b, h)
                print(f"area do triangulo é {area}.")
                continue
                
            case "4":
                b = float(input("informe o valor da base menor do trapezio")).replace(",",".")
                B = float(input("informe o valor da base maior do trapezio")).replace(",",".")
                h = float(input("informe o valor da altura do trapezio")).replace(",",".")
                area = trapezio(B, b,h)
                print(f"a area do trapezio é {area}")
                continue

            case "5":
                print("programa encerrado.")
                break
            case _:
                print("Opção inválida.")
                continue
    except Exception as e:
        print(f"nao foi possível calcular. {e}")
        continue
          
        
        