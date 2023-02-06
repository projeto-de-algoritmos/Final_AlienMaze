# :alien: Closest Aliens

**Número da Lista**: Dupla 3<br>
**Conteúdo da Disciplina**: Final<br>

## Alunos 
|Matrícula | Aluno |
| -- | -- |
| 19/0089792  |  João Victor Correia de Oliveira |
| 19/0020601  |  Victor Buendia Cruz de Alvim |

## Sobre 
Berg é um quadradinho mágico que aceitou o desafio de ser o melhor corredor do mundo das matrizes, por isso ele precisa coletar a maior quantidade de moedas possíveis no mapa. Porém, como todo bom desafio Berg precisa passar pelas pedras no caminho, ou melhor, *evitá-las*, pois no mapa ele não pode correr sobre elas. Piorando sua situação, Berg possui dois inimigos que vão lhe atrapalhar: Bob, um quadrado rosa, que vai tentar roubar as moedas mais próximas e Bill, um quadrado roxo, que irá o perseguir pelo menor caminho e, caso consiga encostar, imobilizar. Sua missão como jogador é ajudar Berg nessa missão superando seus adversários. 

Algoritmos utilizados:
* Par de pontos mais próximos e distância manhattan: Para melhorar a estratégia de Bill, ele sempre verificará quais as duas moedas que estão mais próximas no plano, utilizando o algoritmo de par de pontos mais próximos, e pegará a mais próxima de si, de acordo com o algoritmo da distância de manhattan

* A-Star: Bob perseguirá Bill pelo menor caminho do grafo de células encontrado pelo algoritmo de programção dinâmica A-Star.    


## Screenshots


## Vídeo de Apresentação



## Instalação 
**Linguagem**: Python<br>
**Framework**: Pygame <br>
Necessário ter o [Python](https://www.python.org/downloads/) instalado 

## Uso 
Para rodar o projeto abra o terminal e execute o seguinte comandos:

```
python3 -m venv .pv && source .pv/bin/activate && pip3 install -r requirements.txt && python3 src/main.py
```

## Outros 
