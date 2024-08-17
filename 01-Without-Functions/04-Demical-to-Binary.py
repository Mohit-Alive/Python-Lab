num = int(input("Enter a number: "))
binary = ""
if num < 0:
    print("Binary does not exist for negative numbers")
elif num == 0:
    print("The binary of 0 is 0")
else:
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2
    print("The binary is", binary)

