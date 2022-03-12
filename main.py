from t1 import d


a=input('please write you want sign in or sign up in web site?  ')
if a=='sign up':
    us=input('please make a user name')
    ps=input('please make a password')
    d.update({us:ps})
    print('welcome to website')
    print(d)
i=0
if a=='sign in':
    while i<=5:
        us1=input('please write your user name')
        ps1=input('please write your password')
        if (us1,ps1) in d.items():
            print('welcome to website')
        else:
            print('user name or password is not deffind if you want try again to sign in write <y> else <n>')
            i+=1
            h=input('please write y or n')
            if h=='n':
                print('good bye ')
                break
    if i==5:
        print('you tried to sing in  5 times you cant sing in again ')
        print('good bye')
