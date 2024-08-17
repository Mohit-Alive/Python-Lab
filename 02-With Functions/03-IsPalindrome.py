def isPalindrome(num):
    if str(num) == str(num)[::-1]:
        print("Yes its a palindrome")
    else:
        print("No, its not a palindrome")

isPalindrome(10101)