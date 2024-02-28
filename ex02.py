# aula: função recursiva 
# autor: Michel
# data 28/02/2024

# 1 -  Escreva uma função (faça uso do while) 
# que recebe um parâmetros e imprime o fatorial. 
# teste a função.

def fatorial(n):
  fat = 1
  while n > 0:
    print(f"{fat}*{n}",end=', ') # print para visualizar os passos
    fat = fat * n
    n = n - 1
  print()
  return fat


numero = int(input("informe um valor: "))
print(f"{numero}! = {fatorial(numero)}")
