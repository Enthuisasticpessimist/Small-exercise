##data initialization
salary = int(input("Please enter your salary:"))
shop_re = []
o_date = [
    ['iphone-1',100],
    ['iphone-2',2200],
    ['iphone*3',3300],
    ['iphone4+',4400],
    ['iphone5plus',5500]
    ]
shopping_cart = enumerate(o_date,1)
shop_c = {}

##print product list 
print("shopping_cart".center(50,'-'))
for k,v in shopping_cart:
    shop_c.update({k:v})
    print('%d\t%s\t%d'%(k,v[0],v[1]))
print("".center(50,'-'))



##purchase
while True:
    select = input('''Select what you want to purchase by index or exit by 'q':''')
    
    if select == 'q':
        break
    elif select.isdigit():
        if shop_c.get(int(select)) != None:
            if salary >= shop_c.get(int(select))[1]:
                salary -= shop_c.get(int(select))[1]
                shop_re.append(shop_c.get(int(select)))
                print(shop_c.get(int(select))[0],"already added to the shopping cart.")
            else:
                print('Your money is not enough!')
        else:
            print("This commdity does not exist!")
            continue
    else:
        print('(Please enter a valid character!)\n')

##purchase end and print shopping list
print("Purchased List".center(50,'-'))
for k,v in enumerate(shop_re,1):
    print('%d\t%s\t%d'%(k,v[0],v[1]))
print("".center(50,'-'))
