# aula: recursivo
# autor: Michel
# data 28/02/2024

# 0! = 1
# 1! = 1
# 2! = 1! * 2 = 2
# 3! = 2! * 3 = 6
# 4! = 3! * 4 = 24
# 5! = 4! * 5 = 120
# 6! = 5! * 6 = 720
# n! = (n-1)! * n

def fatorial(n):
  if n == 0:
    return 1
  return fatorial(n-1) * n

valor = int(input("informe um valor: "))
print(f"{valor}! = {fatorial(valor)}")