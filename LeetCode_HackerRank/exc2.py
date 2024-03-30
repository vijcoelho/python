def simpleArraySum(ar):
    sum = 0
    for i in range(0, len(ar)):
        sum += ar[i]
    return sum

ar = [1,2,3,4,5]
print(simpleArraySum(ar))
