##initialization
name = 'a'
password = '1'
user_status = False

##decorator
def login(func):
    def inner():
        global name,password,user_status
        if user_status == True:
            pass
        else:
            n = input('name:')
            p = input('password:')
            if n == name and p == password:
                user_status = True
        if user_status:
            func()
    return inner

@login
def webpage1():
    print('webpage---1')
@login
def webpage2():
    print('webpage---2')

##webpage1 = login(webpage1)##original method1
##webpage2 = login(webpage2)##original method2
webpage1()
webpage2()
