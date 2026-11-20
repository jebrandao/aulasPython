"""continue: interrompe só o ciclo atual e inicia a próxima volta do laço.

ARMADILHA: se o incremento do contador ficasse DEPOIS do continue, o contador pararia
de avançar no valor 10 e o laço viraria infinito. Por isso o incremento vem ANTES do if.
"""

contador = 0
while contador < 19:
    contador += 1  # incremento antes de qualquer continue

    if contador == 10:
        print("--- INÍCIO DO BLOCO DO IF ---")
        print("Neste momento o contador vale 10 (este número não será exibido)")
        continue  # volta ao while sem executar o print abaixo

    print(contador)

print("--- Linha após o bloco do while ---")
print("--- FIM DO PROGRAMA ---")
