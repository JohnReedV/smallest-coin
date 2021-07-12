input_string = input("Enter three numbers: ")
coins = input_string.split()
coins = list(map(int, coins))
coins.sort(reverse=True)
data = int(input('''Enter a number, I will find the minimum amount of the previously entered values it will take in order to add them to this number: '''))
final = 0
add = 0

for number in coins:
    while final <= data:
        if final + number <= data:
            final += number
            add = add + 1
        else:
            break
    while final <= data:
        if final + number <= data:
            final += number
            add = add + 1
        else:
            break
    while final <= data:
        if final + number <= data:
            final += number
            add = add + 1
        else:
            break
print(add)