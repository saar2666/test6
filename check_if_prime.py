num = input("insert num: ")

a =[i for i in range (2,num) if num % i == 0]

def isPrime (n):
    if num > 1:
        if len(a) == 0:
            print 'prime'
        else :
            print 'not prime'
    else:
        print 'not prime'
        
isPrime(num)

