"""Tratamento de exceções com try / except / else / finally."""

nomes = ["Carlos", "Matheus", "Maria", "Jéssica", "Ana"]

try:  # tentar
    numero = int(input("Informe um número para que seja exibido o nome correspondente na lista: "))
    print(f"Nome encontrado na posição {numero} da lista: {nomes[numero]}")

except IndexError as erro:  # exceto
    print("Este número não corresponde a um item da lista de nomes...")
    print(f"Detalhe técnico: {erro}")

except ValueError:
    print("Você deve digitar um NÚMERO inteiro!")

else:  # OPCIONAL: só executa se não ocorreu nenhum erro
    print("Execução concluída sem erros!!!")

finally:  # OPCIONAL: executa SEMPRE, com ou sem erro
    print("Fim do programa!")
