#algoritmo implementado em Python 3.11.4
class No:
  def __init__(self, dado):
    self.dado = dado
    self.prox = None

class Lista:
  def __init__(self):
    self.prim = None

  #Metodos principais

  def adicionar(self, palavra):
    palavra = palavra.lower()
    if self.consulta(palavra)[0]:
      print(f"Palavra ja existente {palavra}".lower())
      return False
    
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
    
  def display(self, num=0):
    num = int(num)
    atual = self.prim
    if not atual:
      print("lista vazia")
      return False
    
    if num != 0:
      cont = 0
      while(atual.prox):
        if (len(atual.dado) == num):
          print(atual.dado, end=" ")
          cont += 1
        atual = atual.prox
      if (len(atual.dado) == num):
        print(atual.dado)
        cont += 1
      else:
        print()
      if cont == 0:
        print("lista vazia")
      return True
    
    while(atual.prox):
      print(atual.dado.lower(), end=" ")
      atual = atual.prox
    print(atual.dado.lower())

  #Interfaces

  def inserirPalavra(self, palavra):
    palavra = palavra.lower()
    Lista_4.adicionar(palavra)
    print(f"Palavra inserida: {palavra}")
    tamanho = len(palavra)
    if tamanho <= 5:
      Lista_1.adicionar(palavra)
    elif tamanho > 5 and tamanho <= 10:
      Lista_2.adicionar(palavra)
    else:
      Lista_3.adicionar(palavra)

  def listaPalavras(self, lista):
    if int(lista) == 1:
      Lista_1.display()
    elif int(lista) == 2:
      Lista_2.display()
    elif int(lista) == 3:
      Lista_3.display()
    elif int(lista) == 4:
      Lista_4.display()

  def NumdeLetras(self, num=0):
    Lista_4.display(num)

  def ListarIntervalo(self, inicio, fim):
    atual = Lista_4.prim
    if not atual:
      print("lista vazia")
    while(atual.prox and fim >= atual.dado[0]):
      if atual.dado >= inicio:
        print(atual.dado, end=" ")
      atual = atual.prox
    if atual.dado[0] == fim:
      print(atual.dado)
    else:
      print()

Lista_1 = Lista()
Lista_2 = Lista()
Lista_3 = Lista()
Lista_4 = Lista()
lista = Lista()

"""lista.inserirPalavra("Isca")
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
lista.inserirPalavra("Xuxa")
lista.NumdeLetras(4)
lista.listaPalavras(3)
lista.listaPalavras(1)
lista.listaPalavras(2)
lista.NumdeLetras(5)
lista.listaPalavras(3)
lista.ListarIntervalo("b", "v")
lista.listaPalavras(4)"""







