"""problema No.3: 
verificar si el ultimo digito de unn 
numero par """

print("----------------------------")
print("------ULTIMO DIGITO PAR?----")
print("----------------------------")

# input 
x = int(input("Digite el valor de x: "))

# processign 
ultimo_digito = x % 10 
r = ultimo_digito % 2

if r == 0:
    print("El ultimo digito de " + str(x) + "es PAR")
    