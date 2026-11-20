# Aula 11 – POO: métodos

Métodos são as funções de uma classe: definem os **comportamentos** dos objetos. O primeiro parâmetro
(`self`) é o próprio objeto sobre o qual o método foi chamado.

| Arquivo | Assunto |
| --- | --- |
| [`metodos.py`](metodos.py) | Classe `Usuario` com o método `efetuar_login()` |

## O que foi modernizado

- Método em `snake_case` (`efetuar_login`), conforme PEP 8. O slide usa `efetuarLogin` (estilo Java).
- O método **retorna** `bool` e quem chama decide o que exibir; misturar regra e `print` dificulta reuso e testes.
- Comparação de senha com `hmac.compare_digest`. **Em sistemas reais nunca se guarda senha em texto puro**;
  usa-se hash (por exemplo `hashlib.scrypt` ou bibliotecas como `argon2-cffi`). Aqui a senha fixa é só didática.
