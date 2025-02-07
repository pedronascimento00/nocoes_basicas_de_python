x = int(input("Digite um numero inteiro : "))

if x < 0:
    resp1 = "positivo"
else:
    resp1 = "negativo"

if x % 2 ==0:
    resp2 ="immpar"
else:
    resp2 = "par"

print("O numero {0} é {1}.".format(x,resp1,resp2))