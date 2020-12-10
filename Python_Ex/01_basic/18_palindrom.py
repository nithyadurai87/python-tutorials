"""power of python find number or string is palindrome or not"""
number = input("Enter any large value:")
if str(number)==str(number)[::-1]:
    print 'Palindrome'
else:
    print 'Not a Palindrome'
