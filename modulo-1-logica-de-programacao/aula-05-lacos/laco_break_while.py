"""break: interrompe o laço inteiro e segue para o código após o bloco."""

contador = 1
while contador < 20:
    print(contador)

    if contador == 10:
        print("--- INÍCIO DO BLOCO DO IF ---")
        print("Neste momento o contador vale 10")
        break
        # Qualquer instrução depois do break nunca é executada.

    contador += 1

print("--- Linha após o bloco do while ---")
print("--- FIM DO PROGRAMA ---")
