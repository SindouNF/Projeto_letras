""" Natanael Sindou Ferreira


"""

class Peça: #cria dicionario de chave(peça) e seu valor
    def __init__(self):
        self.Peça =  { 'A':1,  'E': 1, 'I': 1, 'O': 1, 'U': 1, 'N': 1, 'R': 1, 'T': 1, 'L': 1, 
    'S': 1, 'D': 2, 'G': 2, 'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F': 5, 'H': 5, 'V': 5,
    'J': 8, 'X': 8, 'Q': 13, 'Z': 13}

    def getTodasPeças(self):
        print(self.Peça)
    #informa o valor da letra
    def getPonto(self, pos):
        return self.Peça[pos.upper()]