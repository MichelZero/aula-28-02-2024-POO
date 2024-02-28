# aula:  
# autor: Michel
# data 28/02/2024

# 0! = 1
# 1! = 1
# 2! = 1 * 2 = 2
# 3! = 1 * 2 * 3 = 6
# 4! = 1 * 2 * 3 * 4 = 24
# 5! = 1 * 2 * 3 * 4 * 5 = 120
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720

numero = int(input("informe um valor: "))

fat = 1
while numero > 0:
  fat = fat * numero
  numero = numero - 1


print(f"{fat}")