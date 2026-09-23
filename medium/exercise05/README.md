# Exercício — Jogo de Craps

## Objetivo

Faça um programa que implemente o jogo de Craps. O jogador lança um par de dados de seis faces, obtendo uma soma entre 2 e 12.

## Regras do jogo

### Primeira jogada

- Se a soma for **7 ou 11**, o resultado é chamado de **natural**, e o jogador ganha.
- Se a soma for **2, 3 ou 12**, o resultado é chamado de **craps**, e o jogador perde.
- Se a soma for **4, 5, 6, 8, 9 ou 10**, esse número passa a ser o **Ponto** do jogador.

### Jogadas seguintes

Após estabelecer o Ponto, o jogador continua lançando o par de dados:

- Se tirar o **Ponto novamente**, ganha.
- Se tirar **7 antes de repetir o Ponto**, perde.
- Se tirar qualquer outro valor, continua jogando.

## Função de lançamento de dados

Implemente o lançamento dos dados com uma função genérica que:

- Permita lançar qualquer quantidade de dados.
- Permita utilizar dados com qualquer quantidade de faces.
- Tenha **6 faces como valor padrão** do parâmetro correspondente.
- Retorne a **soma total dos valores obtidos** nos dados lançados.

No jogo de Craps, utilize essa função para lançar **dois dados de seis faces**.

## Biblioteca a estudar

Estude e utilize a biblioteca **`random`** do Python para implementar a função de lançamento dos dados.
