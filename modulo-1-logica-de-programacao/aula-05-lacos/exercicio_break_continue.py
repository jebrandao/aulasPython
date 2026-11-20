"""Exercício de fixação – Teste de adivinhação (break e continue).

O usuário tem 5 tentativas para acertar um número de 1 a 20.
- Número fora do intervalo: avisa, perde a tentativa e passa para a próxima (continue).
- Errou: dá a dica de maior/menor.
- Acertou: encerra as tentativas (break).
- Esgotou as tentativas sem acertar: revela o número oculto.

Upgrade do enunciado: o número oculto é sorteado a cada execução.
"""

import random

TENTATIVAS = 5
MINIMO, MAXIMO = 1, 20


def jogar(oculto: int) -> None:
    print("\n--- TESTE DE ADIVINHAÇÃO ---")
    print(f"Você terá {TENTATIVAS} tentativas para adivinhar o número oculto.")
    print(f"Só valem números entre {MINIMO} e {MAXIMO}. Boa sorte!")

    for tentativa in range(1, TENTATIVAS + 1):
        palpite = int(input(f"\nTentativa {tentativa} de {TENTATIVAS}: "))

        if not MINIMO <= palpite <= MAXIMO:
            print(
                f"ATENÇÃO: o número precisa estar entre {MINIMO} e {MAXIMO}. Você perdeu esta tentativa."
            )
            continue

        if palpite == oculto:
            print(f"PARABÉNS! Você acertou na tentativa {tentativa}. O número oculto é {oculto}.")
            break

        dica = "menor" if palpite > oculto else "maior"
        print(f"Você ERROU. O número oculto é {dica} que {palpite}.")
    else:
        # O else do for só executa quando o laço termina SEM break, ou seja, sem acerto.
        print(f"Fim das tentativas! O número oculto que você não encontrou é {oculto}.")

    print("\n--- FIM DO TESTE DE ADIVINHAÇÃO ---")


if __name__ == "__main__":
    jogar(random.randint(MINIMO, MAXIMO))
