"""Exibe todos os números de 1 a 500 com while.

O while exige atenção a 3 itens separados no código:
1) valor inicial do contador; 2) teste lógico (valor final); 3) incremento.
"""

contador = 1  # 1) valor inicial
while contador <= 500:  # 2) enquanto contador for menor ou igual a 500...
    print(contador)
    contador += 1  # 3) incremento (sem ele o laço seria infinito)
