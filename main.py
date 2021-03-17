#-*- coding:utf-8 -*-
""" Natanael Sindou Ferreira

obs: o código foi feito com tratamento utf-8, ou seja, ele aceita acentuação nas variaveis, isso foi decidido, pois, na leitura do 'Banco de palavras.txt'
fazer o tratamento da acentuação não seria suficiente, uma vez que a leitura já haveria sido prejudicada, por exemplo, a palavra último, se tornava
áltimo, fazendo o tratamento virava altima, o que não condiz com a leitura desejada

A logica do programa se baseia na criação de objetos dentro da classe BanacoPalavras que opera todas as funções da nossa estrutura enquanto a classe
Peça simula um dataset, com uma estrutura de dicionário, tuplas, onde a chave é nossa letra/peça e o valor da chave é correspondente ao valor da peça
assim, a comparação e chamada se torna muito mais simplificada quando feito dentro do BancoPalavras que cria um objeto da classe Peça para poder acessar
seu método "getPonto".

Dentro da classe banco temos vários métodos, cada um com uma função delimitada para saber onde cada trecho funciona e o que ele opera, como por exemplo
a classe acentuação, que serve para tratar as palavras com acentuação deixandoas normais. 
O problema se resolve da seguinte forma: na main é feito a instancia de um objeto da classe BancoPalavras que ao ser inicializada faz a abertura do arquivo,
após isto, a leitura das peça e da pontuação bonus, que é passado pela "melhor_jogada", é feita e portanto, dentro deste nosso metodo eh feito a chamada
do nosso arquivo sendo lido linha por linha do "Banco de palavra.txt", e, para cada iteração deste nosso laço é feito a chamada da classe compare, que
compara a palavra passada por parametro letra por letra, com as letras/peças, dadas pelo jogador, assim, ele verifica se a letra é igual, se sim ele
armazena numa lista, feito com uma string, a letra utilizada E verifica chamadno o "getPonto" de Peça o valor dessa letra se houver a ocorrência, após 
isto é feito a soma do valor atual com o anterior e ele pula para a próxima letra da palavra do arquivo, utilizando o break, assim é feito uma nova repetição
do laço de peças passadas, porém, para não haver um conflito de aceitar a mesma letra já utilizada, ele apresenta uma condicional que verifica se a letra 
sendo lida não tem sua posição salva na lista dicionário e então ele segue adiante até verificar todas as letras, as letras não utilizadas, no final é verificada
com as utlizada e subtraídas da lista de palavras.
Para calcular qual foi a palavra montada com a maior pontuação é dado a chamada do metodo max() dando como "key=" o valor do nosso dicionario e em caso de empate
é verificado se eles tem o mesmo tamanho, se sim , o que for alfabeticamente "menor" é retornado, senão o que tiver menos letras.

Para resolver o problema de multipalavras, foi implementado o metodo "mult_palavra", que executa após a verificação da palavra de maior valor e, desta vez
é chamada passando como parametro de Peças disponizeis, a lista de peças que sobraram, isto se repete até que, o maior valor encontrado pela função seja
"nenhuma palavra encontrada"/0, o que significa que das letras que restaram não é possível formar mais nenhuma palavra. Uma observação que este método poderia
ser executado de forma recursiva chamando o "melhor_jogada" novamentre, porém, como python "fica pesado/superaquece" em chamadas de recursão, por escolha pessoal
foi desenvolvido um novo método com 90% identico somente criando a condicional de parada/retorno
"""
from BancoPalavras import *

class Main():
    def main():
        while(True):
            palavra = Palavras()
            pontuação = 0
            print("Digite as letras disponíveis nesta jogada:", end=" ")
            peças_da_jogada = input()
            print("Digite a posição bônus:", end=" ")
            posição_bonus = int(input())
            print()
            palavra.melhor_jogada(peças_da_jogada, posição_bonus)
        
    if __name__ == "__main__":
        main()