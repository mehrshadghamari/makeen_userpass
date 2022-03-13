from t1 import d


a=input('please write you want sign in or sign up in web site?  ')
if a=='sign up':
    while True:#در صورت غلط بودن هر کدام از شرط ها دوباره نام کاربری دریافت کند
        us=input('please make a user name')
        if us[0] in ['0','1','2','3','4','5','6','7','8','9']:# شرط شروع نشدن نام کاربری با عدد
            print('user name dont start with number choose user name again')
            continue
        elif ' ' in us :# شرط نداشتن فاصله در نام کاربری
            print('user name dont include white space choose user name again')
            continue

        b=len(us)
        k=0
        for z in us:#کل نام کاربری نباید از عدد باشد
            if z in ['0','1','2','3','4','5','6','7','8','9']:
                k+=1
        if k==b:
            print('you shoudnt choose number for all of the user name')
            continue
            

        for j in us:# شرط نداشتن کارکتر خاص در نام گاربری
            if j in ['*','&','^','%','$','#','@','!']:
                print('user name dont include not even one special charectors')
            continue
        break
        

    while True:#در صورت غلط بودن هر کدام از شرط ها دوباره رمز عبور دریافت کند
        ps=input('please make a password')
        h=len(ps)
        if h<8:#شرط داشتن تعداد حداقل 8 کارکتر 
            print('password should have minimom 8 charactors')
            continue
#شرط شامل بودن حداقل یک حرف بزرگ و کوچک
        rules = [lambda ps: any(x.isupper() for x in ps),lambda ps: any(x.islower() for x in ps)]
        if not all(rule(ps) for rule in rules):
            print('password must have at least one uppercase and lowercase')
            continue
#شرط شامل بودن حداقل یک کارکتر خاص 
        if  not any(c in ['!','@','#','$','%','^','&','*',] for c in ps):
            print('password should contain special charector')
            continue

        
        break


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
        print('goodbye')