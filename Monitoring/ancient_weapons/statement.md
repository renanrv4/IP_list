Você foi convidado a desenvolver um sistema de gerenciamento de equipamentos para personagens no Adventure Quest Worlds. Cada jogador pode equipar diferentes itens (como armas, armaduras e acessórios), e cada item fornece bônus específicos que aumentam o "Poder de Batalha" (PB) do jogador. Sua missão é calcular o PB total considerando tanto os bônus dos itens quanto às habilidades do jogador, de acordo com o tipo de arma que ele carrega.

![Imagem do jogo Adventure Quest World](https://pbs.twimg.com/media/FquysbYX0AEzcUp.jpg)

### Dados de Entrada
- itens: uma lista de dicionários, onde cada dicionário representa um item equipado pelo jogador. 
  - Cada dicionário contém: "nome": o nome do item (string).
  - "tipo": o tipo de item (string, pode ser "arma", "armadura", ou "acessorio"). Se o tipo for "arma", inclui também um campo "tipo_ataque", que pode ser:
    - "corpo a corpo"
    - "à distância"
    - "mágico"
  - "bonus": o valor do bônus que o item fornece ao PB (inteiro). 
- habilidades: um dicionário onde as chaves são habilidades que o jogador possui (strings, como "força", "agilidade", "inteligência", etc.) e os valores são inteiros que indicam o nível dessas habilidades.
- Facção: uma tupla que deve possuir a facção (“Good”, “Evil”) a qual o jogador pertence e sua posição dentro da facção, podendo ser “soldado”, e “general”.

### Regras para Calcular o Poder de Batalha
> Observação: Siga a ordem predefinida para a realização dos cálculos dos PBs.

#### Bônus de Itens:
   - O PB inicial é a soma de todos os valores de "bonus" nos itens equipados.
#### Bônus de Habilidades para Armas:
  - Habilidades influenciam apenas o PB de itens de tipo "arma" e de acordo com seu "tipo_ataque":
    - "força" aumenta o PB das armas de corpo a corpo em 5 pontos para cada nível.
    - "agilidade" aumenta o PB de todas as armas de corpo a corpo ou à distância em 3 pontos para cada nível.
    - "inteligência" aumenta o PB das armas de tipo mágico em 5 pontos para cada nível.
   - Itens que não sejam do tipo "arma" não recebem bônus das habilidades.
#### Bônus de Conjunto:
  - Se o jogador equipar uma combinação específica de itens, ele ganha um bônus extra no PB:
    - Se houver pelo menos uma "arma" e uma "armadura", o jogador recebe um bônus de 15 no PB.
    - Se houver pelo menos uma "arma", uma "armadura" e um "acessorio", o jogador recebe um bônus adicional de 20 (somando 35 no total).
#### Penalidade de Peso:
  - Se o número total de itens for maior que 4, o jogador perde 5% dos pontos de PB para cada item acima do quarto.
#### Posição dentro da facção:
  - Se o jogador for um soldado, os seus pontos de poder aumentam em 10.
  - Se o jogador for um general, os seus pontos de poder aumentam em 5% dos seus PBs atuais.

### Armas Especiais:
>  Arco de Catende, Cajado da Morte do Ibura, Espada do Sol do Piauí, Arco do Tupã, Livro das Canções, Tridente das Águas de Aracaju, Manoplas Elementais da terra e água.

> Observação: se as armas representam a mesma facção do jogador, o jogador que possuir a arma deverá receber 10% (Caso o jogador tenha duas das armas, ele receberá 20% de bônus, e assim em diante. Além disso, ele deve imprimir os textos relacionados a cada arma especial na ordem na qual as armas foram dadas.) de bônus em seus PBs após o cálculo de todos os bônus.

**Objetivo: Implemente o código utilizando os conhecimentos obtidos nas aulas de tuplas e dicionários para resolver o problema, retornando o poder de batalha final do jogador, considerando todos os bônus e penalidades conforme as regras dadas.**

#### Primeiramente você receberá uma série de inputs, com cada arma do jogador, até que “FIM DA LISTA” seja recebido. O formato de cada entrada é registrada da seguinte forma:
> item_nome | tipo_item | bonus_pb  
**item_nome** (string), **tipo_item** (string), **bonus_pb** (int)
#### Se o tipo do item for arma, você receberá uma nova entrada:
> tipo_ataque  
**tipo_ataque** (string)
#### Após todas as entradas dos itens, você receberá uma nova entrada, indicando os atributos do jogador. A entrada das habilidades do jogador fica da seguinte maneira:
> forca | agilidade | inteligencia  
**Todos os atributos devem ser maiores ou iguais a 0**
#### Por fim, temos a entrada da facção e posição do jogador, o modelo de entrada é:
> Facção: faccao | posicao  
**faccao** (string), **posicao** (string)

Para toda execução do programa, imprima:
> "Bem vindo ao mundo de AQW!!"
#### Caso o jogador tenha em posse, alguma arma especial deve ser impresso o seguinte (Na ordem em que foram adicionadas ao inventário):

**1. Arco de Catende:** Se o jogador possuir essa arma (e o jogador pertencer a facção Good) o programa deverá imprimir o seguinte: 
>“Catende será vitoriosa, Joab nos levará a glória!!!”
* Caso contrário o programa deve imprimir o seguinte:
>“Esse arco foi utilizado pelos guerreiros de Catende, melhor jogar essa arma nas profundezas.”

**2. Cajado da Morte do Ibura:** Se o jogador possuir esse cajado (e o jogador for da facção Good) o programa deverá imprimir o seguinte: 
  
>“Esse cajado possui a energia da morte consigo, melhor prendê-la no mundo dos espelhos.” 
* Caso contrário, o programa deve imprimir o seguinte: 
>“As sombras vão dominar Recife, Lavoisier trará a escuridão!!!”

**3. Espada do Sol de Piauí:** Se o jogador possuir essa espada (e o jogador for da facção Good) o programa deverá imprimir o seguinte: 
>“Essa espada é abençoada pelo Sol, essa espada pertenceu ao guerreiro Luis, devemos usá-la para derrotar as forças do mal.” 
* Caso contrário, o programa deverá imprimir o seguinte: 
>“Essa espada possui o poder das chamas divinas, devemos prender essa arma na fenda dimensional.”

**4. Arco do Tupã:** Se o jogador possuir esse cajado (e o jogador for da facção Good) o programa deverá imprimir o seguinte: 
>“Essa arma é abençoada pela aldeia do trovão, comandada por Júlia, uma arma sagrada podemos usá-la para derrotar o exército de Lavoisier.” 
* Caso contrário, o programa deverá imprimir o seguinte:
>"O arco de tupã é uma arma sagrada, devemos selá-lo na tumba dos campeões."

**5. Livro das Canções:** Se o jogador possuir esse livro (independente de facção) o programa deverá imprimir: 
>“Esse livro possui todos os cânticos da terra longínqua de Tabira, o livro foi escrito pelo bardo Renan, com eles podemos tornar o nosso exército mais poderoso.” 

**6. Tridente das Águas de Aracaju:** Se o jogador possuir essa arma (e for da facção Good) o programa deverá imprimir:  
>“Essa arma pertenceu ao general dos Mares, Renato, ele foi responsável pela derrota de muitos povos. Precisamos nos livrar dessa arma.” 
* Caso contrário, o programa deverá imprimir o seguinte: 
>“Com essa arma podemos ter o mar como aliado, devemos usar essa arma para dominar as águas de Recife e suas feras (os tubarões).”

**7. Manoplas elementais da terra e água:** Se o jogador possuir as luvas (e for da facção Good) o programa deverá imprimir o seguinte: 
>“Essa arma possui a alma de vários povos antigos, o possuidor dessa arma quebrou diversos tabus. Valter foi o dono dela, ele possui vidas inocentes em suas mãos.” 
* Caso contrário, o programa deverá imprimir o seguinte: 
>“As manoplas de Valter são ótimas para causar catástrofes naturais, devemos usá-las para atormentar vilas inimigas.” 

#### Por fim, é retornado o poder de batalha final do jogador (utilize a função round() para o valor final dos PBs), considerando todos os bônus e penalidades conforme as regras dadas.
> Pontos de Batalha: **pontos_de_batalha**

