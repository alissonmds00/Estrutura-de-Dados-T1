import classes
lista = classes.lista

escolha = input().lower()
while(escolha != "e"):
  escolha = input().lower()
  if escolha == "i":
    valor = input()
    lista.inserirPalavra(valor)
    break
  if escolha == "l":
    valor = int(input())
    lista.listaPalavras(valor)
    break
  if escolha == "x": 
    valor = int(input())
    lista.listaPalavras(valor)
    break
  if escolha == "o":
    inicio = input()
    fim = input()
    lista.ListarIntervalo(inicio, fim)
    break
  if escolha =="r":
    valor = input()
    lista.removePalavra(valor)
    break
  if escolha == "e":
    break