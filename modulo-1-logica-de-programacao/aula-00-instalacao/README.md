# Aula 00 – Instalação

## Instalando o Python

1. Acesse [python.org/downloads](https://www.python.org/downloads/) e baixe a versão estável mais recente
   (este repositório exige **Python 3.12 ou superior**).
2. Execute o instalador e, **na primeira tela**, marque **"Add python.exe to PATH"**.
3. Clique em **Install Now**.

## Validando a instalação

Windows (Prompt de Comando ou PowerShell):

```bash
python --version
```

macOS / Linux:

```bash
python3 --version
```

> Nos slides originais o comando de Mac/Linux aparece com erro de digitação (`pyhton3`). O correto é `python3`.

## Ambiente virtual (boa prática moderna)

Para cada projeto, isole as dependências em um ambiente virtual:

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS / Linux
```

Só será necessário a partir do Módulo 3 (Django); os Módulos 1 e 2 usam apenas a biblioteca padrão.

## Sem instalar nada

É possível testar Python direto no navegador, por exemplo em [Replit](https://replit.com) ou no
[Python Tutor](https://pythontutor.com).
