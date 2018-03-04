##-----------Non parametric decorator----------------
####initialization
##name = 'a'
##password = '1'
##user_status = False
##
####decorator
##def login(func):
##    def inner():
##        global name,password,user_status
##        if user_status == True:
##            pass
##        else:
##            n = input('name:')
##            p = input('password:')
##            if n == name and p == password:
##                user_status = True
##        if user_status:
##            func()
##    return inner
##
##@login
##def webpage1():
##    print('webpage---1')
##@login
##def webpage2():
##    print('webpage---2')
##
####webpage1 = login(webpage1)##original method1
####webpage2 = login(webpage2)##original method2
##webpage1()
##webpage2()
##-----------Non parametric decorator----------------

####-----------Parametric decorator--------------------
####initialization
##name = 'a'
##password = '1'
##user_status = False
##
####decorator
##def login(func):
##    def inner(*args,**kwargs):##arbitrary parameters can be passed in 
##        global name,password,user_status
##        if user_status == True:
##            pass
##        else:
##            n = input('name:')
##            p = input('password:')
##            if n == name and p == password:
##                user_status = True
##        if user_status:
##            func(*args,**kwargs)##arbitrary parameters can be passed in 
##    return inner
##
##@login
##def webpage1(arg):
##    print('webpage---1',arg)
##@login
##def webpage2():
##    print('webpage---2')
##
####webpage1 = login(webpage1)##original method1
####webpage2 = login(webpage2)##original method2
##webpage1('111')
##webpage2()
####-----------Parametric decorator--------------------

##-----------Multi-layer decorator--------------------
##initialization
name = 'a'
password = '1'
user_status = False

##decorator
def login(auth_type):
    def outer(func):
        def inner(*args,**kwargs):##arbitrary parameters can be passed in 
            global name,password,user_status
            if auth_type == 'qq':
                if user_status == True:
                    pass
                else:
                    n = input('name:')
                    p = input('password:')
                    if n == name and p == password:
                        user_status = True
                if user_status:
                    func(*args,**kwargs)##arbitrary parameters can be passed in
            else:
                print('auth_type is wrong!')
        return inner
    return outer

@login('qq')
def webpage1(arg):
    print('webpage---1',arg)
@login('weixin')
def webpage2():
    print('webpage---2')

##temp = login("qq")##original method1
##webpage1 = temp(webpage1)
webpage1('111')
##-----------Multi-layer decorator--------------------
