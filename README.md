# Verificador de Força de Senhas

Script em Python que avalia a força de uma senha de duas formas:

1. **Entropia estimada**: calcula os bits de entropia com base no tamanho e nos tipos de caracteres usados.
2. **Checagem de vazamentos**: consulta a API do Have I Been Pwned para saber se a senha já apareceu em vazamentos de dados.

## Como funciona o k-anonimato

A senha **nunca sai do seu computador**. O script:

1. Gera o hash SHA-1 da senha localmente.
2. Envia à API apenas os **5 primeiros caracteres** do hash.
3. Recebe uma lista de hashes que começam com esse prefixo.
4. Compara o restante do hash localmente.

Assim, a API não consegue descobrir qual senha foi verificada.

## Instalação


## Uso

A senha digitada não aparece na tela (uso do `getpass`).

## Limitações

- A entropia é apenas uma estimativa e não detecta padrões como `qwerty` ou `abc123`.
- Requer conexão com a internet para a checagem de vazamentos.

## Aviso

Nunca digite senhas reais em ferramentas em que você não confia. Leia o código antes de usar.
