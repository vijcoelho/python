dias = int(input())
ano = dias // 365 
mes = dias % 365 / 30 
dia = dias % 365 % 30

print("%d ano (s)" %ano) 
print("%d mes (es)" %mes) 
print("%d dia (s)" %dia)