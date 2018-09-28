
def count_digits(integer):
    counter = {}
    intstr = str(integer)
    for no in intstr:
        if no not in counter:
            counter[no] = 1
        else:
            counter[no] = counter[no] + 1
    return counter

print(count_digits(1212121))#{1: 4, 2: 3}
print(count_digits(1212333))#{1: 2, 2: 2, 3: 3}
print(count_digits(12345))#{1: 1, 2: 1, 3: 1, 4: 1, 5: 1}


def most_common_digit(integer):
    dic = count_digits(integer)
    everything = []
    for k,v in dic.items():
        everything.append((v,k))
    everything.sort(reverse=True)
    highestcount = everything[0][0]

    mostcommon = []
    for e in everything:
        if e[0] == highestcount:
            mostcommon.append(e[1])
    mostcommon.sort()
    return mostcommon

print(most_common_digit(1212121))#[1]
print(most_common_digit(12345))#[1, 2, 3, 4, 5]
print(most_common_digit(12586269025)) # fib(50) = 12586269025 [2]
print(most_common_digit(1548008755920)) # fib(60) = 1548008755920 [0, 5]
print(most_common_digit(190392490709135)) # fib(70) = 190392490709135 [9]
