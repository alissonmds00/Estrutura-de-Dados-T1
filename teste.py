class No:
  def __init__(self, dado):
    self.dado = dado
    self.prox = None

class Lista:
  def __init__(self):
    self.prim = None

  def adicionar(self, palavra):
    if self.consulta(palavra)[0]:
      return False
    else:
      novo_No = No(palavra)
      if not self.prim or palavra < self.prim.dado:
        novo_No.prox = self.prim
        self.prim = novo_No
        return True
      atual = self.prim
      while (atual.prox and palavra > atual.prox.dado):
        atual = atual.prox
      novo_No.prox = atual.prox
      atual.prox = novo_No

  def consulta(self, palavra):
    if not self.prim:
      return False, -1
    atual = self.prim
    contador = 0
    while (atual.dado != palavra and atual.prox):
      atual = atual.prox
      contador += 1
    if (atual.dado == palavra):
      return True, contador
    else:
      return False, -1
    
  def display(self):
    atual = self.prim
    if atual:
      while(atual.prox):
        print(atual.dado, end=" ")
        atual = atual.prox
      print(atual.dado)

L1 = Lista()

lista.inserirPalavra("Isca")
lista.inserirPalavra("Alisson")
lista.inserirPalavra("Queijo")
lista.inserirPalavra("Aabrao")
lista.inserirPalavra("pork")
lista.inserirPalavra("Ratinho")
lista.inserirPalavra("Paper")
lista.inserirPalavra('tatu')
lista.inserirPalavra("rolinha")
lista.inserirPalavra("Roliman")
lista.inserirPalavra("urubu")
lista.inserirPalavra("tambor")
lista.inserirPalavra("vapor")
lista.inserirPalavra("vampiro")
lista.inserirPalavra("xuxa")
lista.inserirPalavra("xuxa")
lista.listaPalavras(4)
lista.removePalavra("xuxa")
lista.listaPalavras(4)
lista.removePalavra("paper")
lista.listaPalavras(4)
lista.removePalavra("aabrao")
lista.listaPalavras(4)
lista.removePalavra("pork")
lista.listaPalavras(4)
"""
lista.NumdeLetras(4)
lista.listaPalavras(3)
lista.listaPalavras(1)
lista.listaPalavras(2)
lista.NumdeLetras(5)
lista.listaPalavras(3)
lista.ListarIntervalo("z", "z")
lista.listaPalavras(4)
"""