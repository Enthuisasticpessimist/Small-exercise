import copy

menu = {'广州': {'天河': ['天河体育馆', '金山大夏'],
                '越秀': ['越秀公园', '光孝寺'],
                '番禺': ['长隆欢乐世界', '大夫山']},
         '深圳': {'福田': ['莲花山', '赛格'],
                '龙华': ['元山公园', '龙城广场'],
                '南山': ['世界之窗', '欢乐谷']},
         '佛山': {'禅城': ['梁园', '孔庙'],
                '南海': ['千灯湖', '南国桃园'],
                '顺德': ['清晖园', '西山庙']}
        }
level = 1
while True:
    print(menu.keys())
    ch = input("Chose the city:")

    if ch == e:
        break
    if ch == b:
        
    elif ch in menu:
        flag = copy.copy(ch)
        print(menu[flag].keys())
        level += 1
    elif ch in menu[flag]:
        flag = copy.copy(ch)
        print(menu[flag].keys())

print('Program ends!')
