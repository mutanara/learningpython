# taking numbers fro 0 up to the one you want, if the number is divible by 3 print "Fizz",
#if the number is divisible by 5 print "Buzz", if it is divisible by both 3 and 5 print "FizzBuzz",
#print that number.

for x in range(1,100):
    if x % 3 == 0 and x % 5 == 0:  #the key is two start with bitwise condition before single one.The opposite would bring wrong results.
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)


  