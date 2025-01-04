Com o Natal se aproximando, os duendes decidiram seu reunir para entregar o melhor presente imaginável ao Papai Noel: um trenó mágico novinho em folha! Entretanto, construir esse trenó não será uma tarefa fácil, os duendes deverão explorar uma masmorra mágica e resolver seus dois grande enigmas para obter a matéria prima necessária. Por isso, eles pediram a sua ajuda, estudante de IP do Cin, para criar um algoritmo capaz de resolver tais enigmas utilizando apenas os conhecimentos de programação vistos até o momento.

![O natal tá chegando!!](https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExdjBraWhsMzByb3R0bjJtNmYxNjl6dGlodHZ6cmxmcHQzMGppajcxaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LBAv3HJDl2WwU/giphy.gif)

### **Enigmas**

**Materiais Mágicos**: Os materiais necessários para montar o trenó estão trancados em baús protegidos por senhas mágicas, para abri-los, os duendes precisam adivinhar as letras das senhas! Seu programa deverá simular um jogo de forca, em que será recebido o número de palavras a serem decifradas e, para cada uma delas, os duendes receberão um determinado número de tentativas, a depender do tamanho da string, incluindo espaços:

>tamanho <= 5: Limite de 7 tentativas
>

>5 < tamanho <= 10: Limite de 9 tentativas
>

>10 < tamanho <= 13: Limite de 13 tentativas
>

> tamanho > 13: Limite de 16 tentativas
>

**O código do trenó perdido**: Os duendes descobriram que cada parte do trenó possui um "código perdido" a ser decifrado. Tal código é representado por uma sequência de inteiros que aparecem desordenados. Seu programa deverá identificar o menor e o maior número da sequência e somá-los para decifrá-lo.

**OBS**: Os duendes terão um total de duas tentativas para advinhar o "código perdido"

A primeira entrada será um número inteiro > 0, que representa o número de itens mágicos que os duendes precisam recuperar para completar o enigma dos materiais mágicos.

> qtd_materiais
>

Então, o programa deverá receber uma nova entrada sobre o nome do item mágico em formato de string.

> nome_item
>

**OBS**: O programa deve receber inputs dos itens mágicos conforme o inteiro **qtd_materiais**, porém, ele só deve receber o próximo input de item após ter acertado o nome do item ou ter esgotado todas suas tentativas.

Em seguida, será recebida uma quantidade indeterminada de caracteres representando os chutes dos duendes, seu programa deverá continuar a receber esse input até que as senhas de todos os matériais sejam analisadas, isto é, forem advinhadas ou tenham suas tentativas esgotadas

> letra
>

---

Com o fim do primeiro enigma, será iniciado o segundo com mais um inteiro > 0, representando o número de partes do trenó.

> qtd_partes
>

Então, para cada peça do trenó, você deverá receber uma sequência com tamanho indeterminado de inteiros, cada um separado por um espaço

> N1 N2 N3... Nn
>

**OBS**: O programa deve receber inputs das sequências de números conforme o inteiro **qtd_partes**, porém, ele só deve receber a peóxima sequência após ter acertado o resultado ou ter esgotado todas suas tentativas.

Ao iniciar o programa, as seguinte mensagem deverão ser impressa em linhas distintas:

> Bem-vindo à missão dos duendes! Vamos construir o trenó mágico do Papai Noel!
>

>Quantos materiais mágicos estão trancados nos baús?
>

>Vamos começar desbloqueando os materiais!
>

Para cada material que deverá ser analisado, imprima:

> Material {ordem_material} de {qtd_materiais}
>

**OBS**: **ordem_material** deverá iniciar em 1

Quando seu programa receber um novo material, imprima seu nome substituindo quaisquer caracteres que não sejam espaços por "_", por exemplo:

>CARRINHO: ________
>
>CRISTAL MAGICO: _______ ______
>

Caso o programa receba uma letra que não esteja presente na senha e suas tentativas não tenham acabado, imprima:

> Erramos a letra! Porém ainda temos mais tentativas.
>

Caso o programa receba uma letra que esteja presente na senha uma vez e ainda não foi feito esse chute antes, imprima:

> Acertamos uma letra! Ela aparece um total de 1 vez na senha
>

Se a letra aparecer mais de uma vez e ainda não foi feito esse chute antes, imprima:

> Acertamos uma letra! Ela aparece um total de {n_vezes} vezes na senha
>

Se o número de tentativas se esgotaram **e** (o último chute não estava presente na senha **ou** foi um chute repetido), o programa deve imprimir o seguinte:

> Infelizmente não conseguimos descobrir a senha.
>

Caso os duendes tenham sido capazes de adivinhar o nome do material mágico, imprima:

> Parabéns! Você desbloqueou o material mágico '{material}'!
>

Caso contrário, o programa deverá imprimir:

> Você não conseguiu desbloquear o material. O nome correto era '{material}'.
>

Ao fim do primeiro enigma, imprima:

> Você desbloqueou {materiais_desbloqueados} de {qtd_materiais} materiais mágicos!
>

Então, ao iniciar o segundo enigma, imprima, em linhas separadas:

> Os duendes precisam decifrar os códigos perdidos para montar o trenó!
>

> Quantas partes o trenó possui?
>

Assim como para os materiais mágicos, imprima para cada nova parte do trenó analisada:

> Parte {ordem_parte} de {qtd_partes}
>

**OBS**: **ordem_parte** deverá iniciar em 1

Após descobrir qual o menor e maior número, o programa deve imprimir, em linhas separadas:

> Dica: O menor número é {menor} e o maior número é {maior}.
>

> Descubra o número mágico (soma de {menor} e {maior})
>

Se os duendes forem capazes de adivinhar o número mágico, imprima:

>Você decifrou o código da parte {ordem_parte}! O trenó está mais próximo de ficar completo!
>

Caso contrário, imprima:

> Número incorreto! Tente novamente.
>

Se o número de tentativas acabou sem os duendes acharem o número mágico, imprima:

> Você não conseguiu decifrar o código. O número mágico era {numero_magico}.
>

Ao final do segunda enigma, imprima a quantidade de partes que puderam ser montadas:

> Você montou {partes_montadas} de {qtd_partes} partes do trenó!
>

Caso todas as partes tenham sido montadas, imprima:

> Parabéns! O trenó está completo e pronto para voar!
>

Se não, caso o número de peças montadas seja maior ou igual a metade (divisão inteira) do número total de partes do trenó, imprima:

> Bom trabalho! O trenó quase ficou completo!
>

Caso contrário, imprima:

> Parece que o trenó ficou incompleto. Tente novamente na próxima missão!
>