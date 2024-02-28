# aula:  
# autor: Michel
# data 28/02/2024

# 2-  Escreva uma função que recebe um número n (inteiro) 
# como parâmetro e imprime a sequência de Fibonacci 
# até esse número, teste a função. 

# sem uso de função:
""" termo = int(input("informe um termo: "))
a, b = 0, 1
while a < termo:
  print(a, end=", ")
  a, b = b, a + b
  
print("fim") """

def fib(termo):
  a, b = 0, 1
  while a < termo:
    print(a, end=", ")
    a, b = b, a + b
    
    
termo = int(input("informe um termo: "))
fib(termo)