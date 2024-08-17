num = int(input("Enter a number: "))
first = 0
second = 1

if num <= 0:
    print("Fibonacci does not exist for negative numbers")
elif num == 1:
    print("The Fibonacci series is:", first)
else:
    print("The Fibonacci series is:", first, second, end=" ")
    for i in range(2, num):
        next = first + second
        print(next, end=" ")
        first = second
        second = next
