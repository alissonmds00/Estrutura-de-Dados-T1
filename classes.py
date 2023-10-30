#algoritmo implementado em Python 3.11.4
class No:
  def __init__(self, dado):
    self.dado = dado
    self.prox = None

class Lista:
  def __init__(self):
    self.prim = None

  #Metodos principais

  #Palavras sao convertidas para lowercase e verifica se ja estao na lista
  def adicionar(self, palavra):
    palavra = palavra.lower()
    if self.consulta(palavra)[0]:
      print(f"palavra ja existente: {palavra}")
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
    anterior = None
    while (atual.dado != palavra and atual.prox):
      anterior = atual
      atual = atual.prox
    if (atual.dado == palavra):
      return True, atual, anterior
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
          print(atual.dado)
          cont += 1
        atual = atual.prox
      if (len(atual.dado) == num):
        print(atual.dado)
        cont += 1
      if cont == 0:
        print("lista vazia")
      return True
    
    while(atual.prox):
      print(atual.dado.lower())
      atual = atual.prox
    print(atual.dado.lower())

  def removePalavra(self, palavra):
    if len(palavra) <= 5:
      lista_alvo = Lista_1
    elif 5 < len(palavra) <= 10:
      lista_alvo = Lista_2
    else:
      lista_alvo = Lista_3
    if not Lista_4.consulta(palavra):
      print(f"palavra inexistente: {palavra}")
      return False, -1
    print(f"palavra removida: {palavra}")
    anteriorL4 = Lista_4.consulta(palavra)[2]
    anteriorLA = lista_alvo.consulta(palavra)[2]
    alvo = Lista_4.consulta(palavra)[1]
    alvoLA = lista_alvo.consulta(palavra)[1]
    if Lista_4.consulta(palavra)[1] == Lista_4.prim:
      Lista_4.prim = alvo.prox
      alvo.prox = None
      return True
    anteriorL4.prox = alvo.prox
    alvo.prox = None

    if lista_alvo.consulta(palavra)[1] == lista_alvo.prim:
      lista_alvo.prim = alvoLA.prox
      alvoLA.prox = None
      return True
    anteriorLA.prox = alvoLA.prox
    alvoLA.prox = None

  #Interfaces

  def inserirPalavra(self, palavra):
    palavra = palavra.lower()
    Lista_4.adicionar(palavra)
    print(f"palavra inserida: {palavra}")
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
    contador = 0
    if not atual:
      print("lista vazia")
    while(atual.prox and fim >= atual.dado[0]):
      if atual.dado >= inicio:
        contador += 1
        print(atual.dado)
      atual = atual.prox
    if fim == atual.dado[0] or inicio == atual.dado[0]:
      contador += 1
      print(atual.dado)
    if contador == 0:
      print("lista vazia")

Lista_1 = Lista()
Lista_2 = Lista()
Lista_3 = Lista()
Lista_4 = Lista()
lista = Lista()








