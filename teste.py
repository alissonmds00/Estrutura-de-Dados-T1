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

L1.adicionar("Isca")
L1.adicionar("Alisson")
L1.adicionar("Queijo")
L1.adicionar("Aabrao")
L1.adicionar("Ratinho")
L1.adicionar("Paper")


L1.display()