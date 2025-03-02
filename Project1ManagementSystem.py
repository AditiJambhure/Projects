db={101:{'name':'Aditi Jambhure','city':'yavatmal','email':'aditijambhure2001@gmail.com','course':'python','fee':40000}}

print('-'*100)
print('The Academy'.center(100,' '))
print('-'*100)

while True:
    print('''
    1.Admission Form
    2.Record
    3.Update
    4.Delete
    5.Filter
    6.Break      
    ''')

    ch=int(input('Enter your choice: '))
    if ch==1:
        reg_no=int(input('Enter student registration number: '))
        name=input('Enter your name: ')
        city=input('Enter your city: ')
        while True:
            email=input('Enter your email: ')
            if email.endswith('@gmail.com'):
                print(email)

            else:
                email=input('Enter your email: ')

            course=input('Enter course: ')
            fee=eval(input('Enter paid fee: '))

            db[reg_no]={'name':name,'city':city,'email':email,'course':course,'fee':fee}

            print(db)


    elif ch==2:
        print('-'*120)
        print('{:^15}|{:^20}|{:^20}|{:^25}|{:^20}|{:^20}'.format('reg_no','name','city','email','course','fee'))
        print('-'*120)

        for reg in db:
            print('{:^15}|{:^20}|{:^20}|{:^25}|{:^20}|{:^20}'.format(reg,db[reg]['name'],db[reg]['city'],db[reg]['email'],db[reg]['course'],db[reg]['fee']))
            print('-'*120)      


    elif ch==3:
        reg_no=int(input("enter registration number: "))
        print('''
              1.name
              2.email
              3.fee
              4.course
             ''')
        ch=int(input('enter your choice: '))
        if reg_no in db:
            if ch==1:
                uname=input('enter name : ')
                db[reg_no]['name']=uname
                print('updated successfully.........')
            elif ch==2:
                uemail=input('enter email: ')
                db[reg_no]['email']=uemail
                print('updated successfully...........')
            elif ch==3:
                ufee=input('enter fee:')
                db[reg_no]['fee']=ufee
                print('updated successfully............')
            elif ch==4:
                ucourse=input('enter course: ')
                db[reg_no]['course']=ucourse
                print('updated successfully............')
            else:
                print('invalid input........')
        else:
            print('invalid number........ ')

    elif ch==4:
        if reg in db:
            reg=int(input('enter reg number: '))
            del db[reg]
            print('Deleted successfully............')
        else:
            print('Invalid input.........')
                
    elif ch==5:
        if reg in db.values:
            reg=int(input('enter reg number: '))
    elif ch==6:
        break
    else:
        print("Invalid input....")

    