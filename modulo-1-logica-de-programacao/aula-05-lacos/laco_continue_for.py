"""continue: interrompe só o ciclo atual e inicia a próxima volta do laço."""

for contador in range(1, 20):
    if contador == 10:
        print("--- INÍCIO DO BLOCO DO IF ---")
        print("Neste momento o contador vale 10 (este número não será exibido)")
        continue  # o for avança sozinho: não há risco de laço infinito

    print(contador)

print("--- Linha após o bloco do for ---")
print("--- FIM DO PROGRAMA ---")
