A, B, C = map(float, input().split())
D = (B ** 2) - (4 * A * C)
if D < 0 or A == 0:
    print("Impossivel calcular")
else:
    D = (D ** 0.5)
    R1 = (-B + D) / (2 * A)
    R2 = (-B - D) / (2 * A)
    print('R1 = %0.5f' % R1)
    print('R2 = %0.5f' % R2)