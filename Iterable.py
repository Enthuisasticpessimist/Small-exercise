##-------------Fibonacci-----------
##def fib(max):
##    n,a,b = 0,0,1
##    while n < max:
##        print(b)
##        a,b = b,a+b
##        n += 1
##fib(15)

##-------------Iterable-----------
##def fib(max):
##    n,a,b = 0,0,1
##    while n < max:
##        yield b ##Freeze the function execution here,and return the value of 'b' to the outside 'for...'
##        a,b = b,a+b
##        n += 1
##    return 123 ##<-if yield:function has becomed a generator,return means generator ending
##for i in fib(15):
##    print(i)

####-------------Send-----------
##def fib(max):
##    n,a,b = 0,0,1
##    while n < max:
##        print(b)
##        a,b = b,a+b
##        n += 1
##        sign = yield b
##        if sign =='stop':
##            print('----sign--',sign)
##            break
##    
##temp = fib(15)
####n1 = next(temp)
####temp.send('stop')
##temp.send(None)
