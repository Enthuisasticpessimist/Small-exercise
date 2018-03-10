data = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'Google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            }
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{}
            },
            '天通苑':{},
            '回龙观':{}
        },
        '朝阳':{},
        '东城':{}
    },
    '上海':{},
    '湖北':{},
    '广东':{}
}
##print(list(data.keys()))
##current = []
##lom = 1 #level of menu
##while True:
##    entr = input('Input the option you want to get into:')
##    if entr == 'e':
##        break
##    elif entr == 'p':
##        lom -= 1
##        if lom == 0:
##            lom = 1
##        if lom == 1 and data.keys() :
##            print(list(data.keys()),'\n')
##            current = list(data.keys())
##        elif lom == 2 and flpm in data and data[flpm].keys():
##            print(list(data[flpm].keys()),'\n')
##            current = list(data[flpm].keys())
##        elif lom == 3 and slpm in data[flpm] and data[flpm][slpm].keys():
##            print(list(data[flpm][slpm].keys()),'\n')
##            current = list(data[flpm][slpm].keys())
##    elif lom == 1 and entr in data and data[entr].keys():
##        print(list(data[entr].keys()),'\n')
##        current = list(data[entr].keys())
##        flpm = entr #First level parent menu
##        lom += 1
##    elif lom == 2 and entr in data[flpm] and data[flpm][entr].keys():
##        print(list(data[flpm][entr].keys()),'\n')
##        current = list(data[flpm][entr].keys())
##        slpm = entr #second level parent menu
##        lom += 1
##    elif lom == 3 and entr in data[flpm][slpm] and data[flpm][slpm][entr].keys():
##        print(list(data[flpm][slpm][entr].keys()),'\n')
##        current = list(data[flpm][slpm][entr].keys())
##        tlpm = entr  # third level parent menu
##        lom += 1
##    else:
##        print("Invalid input！".center(50,'*'),'\n')
##        print(current)
##print('\n','Bye!'.center(50,'*'),'\n')
current_layer = data
layers = []
while True:
    print(list(current_layer.keys()))
    entr = input('Input the option you want to get into:')
    if entr in current_layer and current_layer[entr].keys():
        layers.append(current_layer) # save current layer before getting into next layer
        current_layer = current_layer[entr]
    elif entr == 'b'and layers:
        current_layer = layers.pop()
    elif entr == 'e':
        break
print('Bye!'.center(50,'*'))
