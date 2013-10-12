import random

def TestForInclusion(name,namefile):
    file=open(namefile,'r+')
    doubling=0
    listname=file.readlines()
    file.close()

    changedname=name+'\n'
    for element in listname:
        if changedname==element:
            doubling=1
            break    

    return doubling


def NewNames(firstname,namefile):
    counter=0
    names=['0','0','0','0']
    while counter<4:
        number=random.randint(0,100)
        number=str(number)
        secondname=firstname+number
        doubling=TestForInclusion(secondname,namefile)
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
    doubling=TestForInclusion(firstname,namefile)
    print(doubling)
    doubling0=0

    if doubling==1:
        names=NewNames(firstname,namefile)
        print("Такое имя уже существует. Выберите из предложенных\n",names)
        firstname=input()
        for element in names:
            if firstname==element:

                doubling0=0
                break
            else:
                doubling0=1

    if doubling0==0:
        file=open('list_names.txt','a')
        firstname+='\n'
        file.write(firstname)
        file.close()
        print('Пользователь зарегистрирован')
    else:
        print('Пользователь НЕ зарегестрирован')
                
                  
        
if __name__ == '__main__':
    main()
    
