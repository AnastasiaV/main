import random

def test_for_inclusion(name,namefile):
    name+='\n'
    with open(namefile,'r') as myfile:
        for element in myfile:
            if name==element:
                return 1
    return 0


def new_names(firstname,namefile):
    counter=0
    names=['0','0','0','0']
    while counter<4: 
        number=random.randint(0,100)
        secondname=firstname+str(number)
        doubling=test_for_inclusion(secondname,namefile)
        if doubling==0:
            doubling0=0
            for element in names:
                if secondname==element:
                    doubling0=1
            if doubling0==0:
                names[counter]=secondname
                counter+=1
    return names


def main():
    firstname=input('Введите имя\n')
    namefile='list_names.txt'
    doubling=test_for_inclusion(firstname,namefile)
    print(doubling)
    doubling0=0

    if doubling==1:
        names=new_names(firstname,namefile)
        print("Такое имя уже существует. Выберите из предложенных\n",names)
        firstname=input()
        for element in names:
            if firstname==element:
                doubling0=0
                break
            else:
                doubling0=1

    if doubling0==0:
        with open('list_names.txt','a') as myfile:
            print (firstname, file=myfile)
        print('Пользователь зарегистрирован')
    else:
        print('Пользователь НЕ зарегестрирован')
                

if __name__=='__main__':
    main()
    
