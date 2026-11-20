"""Extra moderno: match/case (Python 3.10+) para escolher entre vários valores."""

opcao = input("Escolha uma forma de pagamento (1-Crédito, 2-Débito, 3-PIX): ")

match opcao:
    case "1":
        print("Cartão de crédito")
    case "2":
        print("Cartão de débito")
    case "3":
        print("PIX")
    case _:  # equivalente ao else
        print("Opção inválida")

# Vários valores no mesmo case, com "|":
dia = input("\nDigite sábado, domingo ou outro dia: ").lower()
match dia:
    case "sábado" | "sabado" | "domingo":
        print("Fim de semana!")
    case _:
        print("Dia útil.")
