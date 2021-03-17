#-*- coding:utf-8 -*-
""" Natanael Sindou Ferreira


"""
import unicodedata
import io
from Peça import * 

class Palavras:
    def __init__(self):
        self.arq = io.open('Banco de palavras.txt','r', encoding='utf8')
        self.total = 0

    #tratamento de acentuação
    def acentuação(self, letra):
        try:
            self.letra = unicode(letra, 'utf-8')
        except NameError:
            pass
        self.letra = unicodedata.normalize('NFD', letra)\
            .encode('ascii', 'ignore')\
            .decode("utf-8")
        return str(self.letra)

    #informa o valor total de pontos: desenvolvido devido aos Pontos extras de multiplas palavras   
    def setTotal(self, ponto):
        self.total = self.total + ponto

    #altera o valor total de pontos da jogada de acordo com as palavras possiveis
    def getTotal(self):
        return self.total

    #compara a palavras com as peças disponiveis
    def compare(self, peça, p, bonus):
        self.ponto = Peça()
        self.pontos = 0
        self.pos_aux = {}
        self.palavra_aux = ""

        for c in range(len(p)):
            self.letra = self.acentuação(p[c]).upper()
            for l in range(len(peça)):

                self.chaves = [self.chave
                                for self.chave, presente in self.pos_aux.items()
                                if l in presente]

                if (peça[l].upper() == self.letra and not (self.letra in self.pos_aux) and not (self.chaves)) :
                    self.pos_aux[self.letra] = [l]
                    if((bonus-1) == c and bonus !=0):    
                        self.pontos = self.pontos + (self.ponto.getPonto(self.letra)*2)
                    else:
                        self.pontos = self.pontos + self.ponto.getPonto(self.letra)
                    self.palavra_aux = self.palavra_aux + self.letra
                    break

                elif (peça[l].upper() == self.letra and (self.letra in self.pos_aux) and not (self.chaves)):
                    self.pos_aux[self.letra].append(l)
                    if((bonus-1) == c and bonus!=0):    
                        self.pontos = self.pontos + (self.ponto.getPonto(self.letra)*2)
                    else:
                        self.pontos = self.pontos + self.ponto.getPonto(self.letra)
                    self.palavra_aux = self.palavra_aux + self.letra
                    break

            if self.palavra_aux == p.upper():
                return self.palavra_aux , self.pontos
        return "Nenhuma palavra encontrada", 0

    #verifica quais letras sobraram após a jogada
    def sobraram(self, resposta, entrada):
        self.sobrou = []
        self.sobrou[:0] = entrada.upper()
        for r in range(len(resposta)):
            for e in self.sobrou:
                if(resposta[r] == e):
                    self.sobrou.remove(e)
                    break
        self.saida = self.sobrou
        return self.saida

    #chamada do método do problema proposto
    def melhor_jogada(self,peça,bonus):
        self.resposta = {}
        for p in self.arq:
            p = p.rstrip('\n')
            self.chave, self.valor = self.compare(peça,p,bonus)
            self.resposta[self.chave] = self.valor
        self.maior_chave = max(self.resposta, key=self.resposta.get)
        self.maior_chave = self.menor_palavra(self.resposta, self.maior_chave)
        self.setTotal(self.resposta[self.maior_chave])
        print(self.maior_chave, end="")
        if(self.maior_chave != 'Nenhuma palavra encontrada'):
            print(", palavra de",self.resposta[self.maior_chave],"pontos")  
        self.sobra = self.sobraram(self.maior_chave, peça)
        print()

        self.continua = True
        while(self.continua):
            self.sobra2 = self.mult_palavra(bonus,self.sobra)
            if self.sobra2 == self.sobra:
                self.continua = False
            else:
                self.sobra = self.sobra2
        if self.getTotal() > 0:
            print("Total de pontos:",self.getTotal())
            print()
        if len(self.sobra):
            print("Sobraram:",self.sobra)
            print()

    #definir a palarva menor com maior valor
    def menor_palavra(self,resposta, melhor):
        for p in resposta:
            #verifica se a palavra nao está se auto comparando
            if resposta[p] == resposta[melhor] and (p != melhor):
                if len(p) < len(melhor):
                    return p
                    break
                elif p < melhor:
                    return p
        return melhor

    #Pontos extras, método de leitura de multipplas palavras
    def mult_palavra(self,bonus,restos):
        #reinicia a leitura das palavras do arquivo
        self.arq.seek(0)
        self.peça = ""
        for index in restos:
            self.peça = self.peça + index
        self.resposta = {}
        for p in self.arq:
            p = p.rstrip('\n')
            self.chave, self.valor = self.compare(self.peça,p,bonus)
            self.resposta[self.chave] = self.valor
        self.maior_chave = max(self.resposta, key=self.resposta.get)
        self.maior_chave = self.menor_palavra(self.resposta, self.maior_chave)
        
        if(self.maior_chave != 'Nenhuma palavra encontrada'):
            print(self.maior_chave, end="")
            print(", palavra de",self.resposta[self.maior_chave],"pontos")
            print()
            self.setTotal(self.resposta[self.maior_chave]) 
            return (self.sobraram(self.maior_chave, self.peça))
        else:
            return restos