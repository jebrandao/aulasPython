"""Testes com os parâmetros sep (separador) e end (final de linha) do print()."""

print("Região Sudeste", 4, "Estados")
print("Região Sudeste", 4, "Estados", sep="-")
print("Região Sudeste", 4, "Estados", sep=",")
print("Região Sudeste", 4, "Estados", sep="0")
print("Região Sudeste", 4, "Estados", sep="")
print("Região Sudeste", 4, "Estados", sep=" - ")
print("Região Sudeste", 4, "Estados", sep=" - ", end="\n")
print("Região Sudeste", 4, "Estados", sep=" - ", end="")
print("Região Sudeste", 4, "Estados", sep=" - ", end="FIM")
print()  # linha em branco para não "colar" a próxima saída no FIM
