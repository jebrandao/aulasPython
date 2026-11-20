"""Operadores ternários: escolher um valor em uma única linha."""

idade = int(input("Informe a sua idade: "))

# Forma 1 (curiosidade): tupla indexada por um booleano (False = 0, True = 1).
# Evite: as DUAS opções são avaliadas antes da escolha e a leitura é pouco clara.
resposta = ("menor de idade", "maior de idade")[idade >= 18]
print("Você é", resposta)

# Forma 2 (recomendada): valor_se_verdadeiro if condicao else valor_se_falso
resposta = "maior de idade" if idade >= 18 else "menor de idade"
print(f"Você é {resposta}")

# Pode ser usado direto dentro de uma f-string:
print(f"Você {'pode' if idade >= 18 else 'não pode'} tirar a carteira de habilitação.")
