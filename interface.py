import classes
lista = classes.lista

escolha = ""
while(escolha != "e"):
  escolha = input().lower()
  if escolha == "i":
    valor = input()
    lista.inserirPalavra(valor)
  if escolha == "l":
    valor = int(input())
    lista.listaPalavras(valor)
  if escolha == "x": 
    valor = int(input())
    lista.NumdeLetras(valor)
  if escolha == "o":
    inicio = input()
    fim = input()
    lista.ListarIntervalo(inicio, fim)
  if escolha =="r":
    valor = input()
    lista.removePalavra(valor)
  if escolha == "e":
    break