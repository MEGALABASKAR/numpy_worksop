# find if the given number is a palindrome or not?
#solution
a=int(input())
 if a==a[::-1]:
  print(f"{a} is palindrome")
 else:
  print(f"{a} is not palindrome")
