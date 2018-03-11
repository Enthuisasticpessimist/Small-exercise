file_name = ''
###load table (staff_table.db)
COLUMNS = ['staff_id','name','age','phone','dept','enroll_date']
loaded_table = {}
for temp in range(len(COLUMNS)):
    loaded_table[COLUMNS[temp]] = []
def load_table(name_db):
    global file_name
    file_name = name_db
    try:
        with open(name_db,'r') as f:
            for line in f:
                for temp in range(len(COLUMNS)):
                    loaded_table[COLUMNS[temp]].append(line.split(',')[temp].strip())
        # print(loaded_table)
        return(loaded_table)
    except (FileNotFoundError,OSError):
        print('<<',name_db,'>>','is not found!')
#-------------------------------------

###update loaded_table
def update_lt():
    update_list = []
    for i in range(len(loaded_table['staff_id'])):
        update_sublist = []
        for temp in COLUMNS:
            update_sublist.append(loaded_table[temp][i])
        update_list.append(update_sublist)
    return update_list
#-------------------------------------

###print loaded_table
def print_lt():
    print_list = update_lt()
    for line in print_list:
        print(line)
#-------------------------------------

###add    ([name,age,phone,dept,enroll_date])
def add(enter):
    if enter.strip().strip('[').strip(']').split(',')[2].split() not in loaded_table['phone']:
        loaded_table['staff_id'].append(str(int(loaded_table['staff_id'][-1]) + 1))
        for i in range(1,len(COLUMNS)):
            loaded_table[COLUMNS[i]].append(enter.strip().strip('[').strip(']').split(',')[i-1].split()[0])
        print_lt()
    else:
        sys_hints('There is the same phone already!','waring')
#-------------------------------------

###delete    [ staff_id ]
def delete(enter):
    if enter.strip() in loaded_table['staff_id']:
        i = loaded_table['staff_id'].index(enter.strip())
        for temp in range(i+1,len(loaded_table['staff_id'])):
            loaded_table['staff_id'][temp] = str(int(loaded_table['staff_id'][temp]) - 1)
        del loaded_table['staff_id'][i]
        for k in range(1, len(COLUMNS)):
            del loaded_table[COLUMNS[k]][i]
        print_lt()
    else:
        sys_hints('There is not the record!','waring')
#-------------------------------------

###update    [enter : ' set dept='Market' where dept='IT' ']
def update(enter):
    index = where_filter(enter.split('where')[1]) #can return index //
    for temp in index:
        loaded_table[enter.split('where')[0].split('set')[1].split('=')[0].strip()][temp] = enter.split('where')[0].split('set')[1].split('=')[0].strip().strip("'").strip()
    print_lt()
#-------------------------------------

###retrieve [enter : ' name,age where age > 22 ']
def retrieve(enter):
    index = where_filter(enter.split('where')[1]) #can return index //
    print_list = []
    for i in index:
        print_sublist = []
        if '*' in enter.strip().split(' ')[0]:
            for temp in COLUMNS:
                print_sublist.append(loaded_table[temp.strip()][i])
        else:
            for temp in enter.strip().split(' ')[0].split(','): # enter.strip().split(' ') :['name,age', 'where', 'age', '>', '22']
                print_sublist.append(loaded_table[temp.strip()][i])
        print_list.append(print_sublist)
    if print_list:
        for temp in print_list:
            print(temp)
    else:
        sys_hints('Sorry,no related content retrieved!')
#-------------------------------------

###operat ([' age ', ' 22 '])
def op_grater(enter):
    index = []
    for i,v in enumerate(loaded_table[enter[0].strip()]):
        if int(v) > int(enter[1]):
            index.append(i)
    return index

def op_less(enter):
    index = []
    for i,v in enumerate(loaded_table[enter[0].strip()]):
        if v < enter[1]:
            index.append(i)
    return index

def op_eq(enter):
    index = []
    for i,v in enumerate(loaded_table[enter[0].strip()]):
        if v == enter[1].strip("'").strip():
            index.append(i)
    return index

def op_like(enter): #parameter:[' enroll_date ',' "2013" ']
    index = []
    for i,v in enumerate(loaded_table[enter[0].strip()]):
        if enter[1].strip(' ').strip('"') in v.split('-'):
            index.append(i)
    return index
#-------------------------------------

###filter [ age > 22 ,enroll_date like "2013"]
operator = {
    '>':op_grater,
    '<':op_less,
    '=':op_eq,
    'like':op_like
}
def where_filter(enter):
    for temp in operator.keys():
        if temp in enter:
            index = operator[temp](enter.split(temp))
    return index
#-------------------------------------

###parse cmd(#update set dept='Market' where dept='IT'
#             retrieve name,age from staff_table where age > 22
#             retrieve * where enroll_date like "2013")
cmd_head = {
    'add': add,
    'delete':delete,
    'update':update,
    'retrieve':retrieve
}
def parse_cmd(enter):
    if enter.split(' ')[0] in cmd_head:
        cmd_head[enter.split(' ')[0]](enter.split(enter.split(' ')[0])[1])
    else:
        sys_hints("Invalid cmd,the system just support 'add/delete/update/retrieve'(you can input 'h' to get help)",
                  'error')
#-------------------------------------

###system hints
def sys_hints(notes,level='info'):
    print(level,':',notes)
#-------------------------------------

###select database
def sel_db():
    name_db = input('Input the name of database which you want to operate:')
    if load_table(name_db):return True
#-------------------------------------



###entry function
input_text = '-'.center(50,'-')+"\nInput what you want to do:(input 'e' to exit)\n>>>"
def main():
    while True:
        if sel_db():break
    while True:
        enter = input(input_text)
        if enter == 'e':break
        elif enter == 'h':sys_hints('\n\tretrieve name,age where age > 22\n'
                                  '\tretrieve * where age > 22\n'
                                  '\tretrieve * where enroll_date like "2013"\n'
                                  '\tadd [Roey,25,1335345649,IT,1993-08-08]\n'
                                  '\tdelete 2\n'
                                  "\tupdate set dept='Market' where dept='IT'",
                                  'legal syntax')
        else:parse_cmd(enter)
#-------------------------------------

###Run
main()
with open(file_name, 'w') as f:
    f.write('')
with open(file_name, 'a') as f:
    result_table = update_lt()
    for line in result_table:
        row = ''
        for arg in line:
            row += (arg+',')
        row = row.strip(',') + '\n'
        f.write(row)
# sel_db()
#-------------------------------------

