a = int(input("Digite o Primeiro nummero inteiro : "))
b = int(input("Digite o Segundo nummero inteiro : "))
c = int(input("Digite o Terceiro nummero inteiro : "))

if a > b  and  a > c:

    resposta = a % 2 ==0

elif b > a  and b > c :

    resposta = b % 2 == 0

else: 

    resposta = c % 2 ==0

print("resultado ", resposta)