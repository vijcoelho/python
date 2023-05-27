peca = (input())
peca_unitaria = int(input())
valor = float(input())

r = peca_unitaria * valor

peca2 = (input())
peca_unitaria2 = int(input())
valor2 = float(input())

r2 = peca_unitaria2 * valor2

t = r + r2
print("VALOR A PAGAR: R$ %0.2f"%(t))