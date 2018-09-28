def sum50odd():
    acc = 0
    i = 1
    for x in range(50):
        acc = acc + i
        i = i + 2
    return acc

print(sum50odd())
