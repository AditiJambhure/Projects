item_db={1:{'name':'poha','rate':20},2:{'name':'Tea','rate':10},3:{'name':'Coffee','rate':20},4:{'name':'Dosa','rate':30}}
items=[]
q=[]

print('-'*100)
print('Garibowala Taj Hotel'.center(100,' '))
print('-'*100)

while True:
    print(''' 
    1.poha
    2.Tea
    3.Coffee
    4.Dosa      

    ''')

    it=int(input('Enter Your choice: '))
    qun=int(input('enter quntity: '))
    items.append(it)
    q.append(qun)
    ch=input('Do you want to continou(y/n): ')
    if ch=='n':
        print('-'*80)
        print('|{:^20}|{:^20}|{:^20}|{:^20}|'.format('item_name','Quntity','Rate','Amount'))
        print('-'*80)
        sum=0
        for i in range(0,len(items)):
            print('|{:^20}|{:^20}|{:^20}|{:^20}|'.format(item_db[items[i]]['name'],q[i],item_db[items[i]]['rate'],q[i]*item_db[items[i]]['rate']))
            sum=sum+q[i]*item_db[items[i]]['rate']
        print()
        print('Total Amount: ',sum) 
        print()
        print('Thank You \n Visit Again...')   
        break

