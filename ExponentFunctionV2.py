
baseput = int(input("Enter the Number: "))
powput = int(input("Enter the Power: "))
def raise_to_power(baseput, powput):
    result = 1
    for index in range(powput):
        result = result * baseput
    return result

print("Here's your answer!: ")
print(raise_to_power(baseput, powput))