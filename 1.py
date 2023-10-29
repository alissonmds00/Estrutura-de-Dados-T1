class No:
  def __init__(self, dado):
    self.dado = dado
    self.prox = None

class Lista:
  def __init__(self):
    self.prim = None

  def inserirPalavra(self, palavra):
    tamanho = len(palavra)
    if tamanho <= 5:
      Lista_1.adicionar(palavra)
    elif tamanho > 5 and tamanho <= 10:
      Lista_2.adicionar(palavra)
    else:
      Lista_3.adicionar(palavra)

  def adicionar(self, palavra):
    palavra = palavra.lower()
    if self.consulta(palavra)[0]:
      print(f"Palavra ja existente {palavra}".lower())
      return False
    
    novo_No = No(palavra)
    print(f"Palavra inserida: {palavra}".lower())
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
    palavra = palavra.lower()
    if not self.prim:
      return False, -1
    
    atual = self.prim
    contador = 0
    while (atual.dado.lower() != palavra and atual.prox):
      atual = atual.prox
      contador += 1
    if (atual.dado.lower() == palavra):
      return True, contador
    return False, -1
    
  def display(self):
    atual = self.prim
    if not atual:
      print("lista vazia")
      return False
    while(atual.prox):
      print(atual.dado.lower(), end=" ")
      atual = atual.prox
    print(atual.dado.lower())
    

Lista_1 = Lista()
Lista_2 = Lista()
Lista_3 = Lista()
Lista_4 = Lista()
lista = Lista()class No:
  def __init__(self, dado):
    self.dado = dado
    self.prox = None

class Lista:
  def __init__(self):
    self.prim = None

  def inserirPalavra(self, palavra):
    tamanho = len(palavra)
    if tamanho <= 5:
      Lista_1.adicionar(palavra)
    elif tamanho > 5 and tamanho <= 10:
      Lista_2.adicionar(palavra)
    else:
      Lista_3.adicionar(palavra)

  def adicionar(self, palavra):
    palavra = palavra.lower()
    if self.consulta(palavra)[0]:
      print(f"Palavra ja existente {palavra}".lower())
      return False
    
    novo_No = No(palavra)
    print(f"Palavra inserida: {palavra}".lower())
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
    palavra = palavra.lower()
    if not self.prim:
      return False, -1
    
    atual = self.prim
    contador = 0
    while (atual.dado.lower() != palavra and atual.prox):
      atual = atual.prox
      contador += 1
    if (atual.dado.lower() == palavra):
      return True, contador
    return False, -1
    
  def display(self):
    atual = self.prim
    if not atual:
      print("lista vazia")
      return False
    while(atual.prox):
      print(atual.dado.lower(), end=" ")
      atual = atual.prox
    print(atual.dado.lower())
    

Lista_1 = Lista()
Lista_2 = Lista()
Lista_3 = Lista()
Lista_4 = Lista()
lista = Lista()







