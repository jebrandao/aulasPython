"""Máscara de CPF. O CPF precisa ser str: um int perderia os zeros à esquerda."""


def formatar_cpf(cpf: str) -> str:
    """Completa com zeros à esquerda (zfill) e aplica a máscara 000.000.000-00."""
    cpf = cpf.zfill(11)
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


if __name__ == "__main__":
    cpf = "3655521304"  # 10 dígitos: faltou um zero à esquerda
    print(f"CPF inserido: {cpf}")
    print(f"CPF com zfill(11): {cpf.zfill(11)}")
    print(f"CPF formatado: {formatar_cpf(cpf)}")
