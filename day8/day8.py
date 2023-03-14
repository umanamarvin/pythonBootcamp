
#  prime number checker

#function
def prime_checker(n):
    n = int(n)
    test1 = n % 2
    test2 = n % 3
    test3 = n % 5
    test4 = n % 7

    if n != 2 and n != 3 and n != 5 and n != 7:
        if test1 != 0 and test2 !=0 and test3 != 0 and test4 != 0:
            print (f"{n} is a prime number.")
        else:
            print (f"{n} is not a prime number.")
    else:
        print (f"{n} is a prime number.")

#main
number = input ("What is the number? ")
prime_checker(number)

    
