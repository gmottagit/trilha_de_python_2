# Desafio 2
Este programa tem como objetivo simular a lógica de um jogo de batalhas de cartas (TCG). Nele dois monstros lutam em turnos até que a vida de um seja igual a 0. Após cada rodada, o programa mostra o placar atual do combate com as respectivas vidas de cada monstro. Para testar o programa, você deve rodar o arquivo simulador_tcg.py em uma maquina que contenha o Python ou então através de uma ferramenta online como o Google Colab. Ao rodar o arquivo, o programa irá solicitar ao usuário os dados:

1. Nome do monstro 1.
2. Nome do monstro 2.
3. Ataque do monstro 1.
4. Ataque do monstro 2.
5. HP do monstro 1.
6. HP do monstro 2.

Depois disso, o duelo irá começar. O monstro 1 sempre realiza o primeiro ataque e, caso o monstro 2 sobreviva, ele contra-ataca. O combate continua em turnos até que a vida de um dos monstros chegue a 0.

Durante a batalha, o programa exibe:
- As ações de ataque realizadas;
- O dano causado em cada golpe;
- O placar atualizado após cada rodada;
- O vencedor final do duelo.

Possiveis melhorias:

- Uso de classes para a criação de diferentes tipos de monstros.
- Possibilidade de ataques críticos.
- Interface gráfica para o jogo.
- Adicionar diferentes possibilidades de ataques e passivas.


  Perguntas teóricas:
  
 ■ Qual é a principal diferença prática entre usar um laço for e um laço while em Python? Por que o while foi a melhor escolha para este duelo?
 - O laço For é um laço de repetição muito utilizado quando sabemos previamente quantas vezes um trecho de código deve ser repetido, já o laço While repete um trecho de código até uma condição ser atingida. Nesse programa o uso do While é mais útil pois não sabemos quantas vezes o duelo deve ser rodado, uma vez que depende da vida e do ataque dos monstros.
   
■ Para que serve a palavra-chave return dentro de uma função? O que acontece se uma função fizer um cálculo matemático mas não possuir o return?
- O return serve para devolver um valor que foi calculado dentro de uma função. Sem return, o cálculo matemático feito dentro da função poderá ser perdido e a função retornará o valor None.

■ O que é um "Loop Infinito" e como podemos evitá-lo ao construir uma estrutura while?
- O Loop Infinito acontece quando dentro de um laço de repetição a condição de parada nunca é atingida, o que faz com o que código seja repetido indefinidamente. Podemos evitar-lo fazendo com que a condição de parada do While eventualmente se torne falsa ou através de Breaks dentro do codigo.

---------------------
