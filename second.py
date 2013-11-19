import random
import sys
import os


def test_for_inclusion(name, namefile):
    with open(namefile, 'r') as myfile:
        for element in myfile:
            if name == element.rstrip():
                return 1
    return 0


def new_names(firstname, namefile):
    counter = 0
    names = ['0', '0', '0', '0']
    while counter < 4:
        number = random.randint(0, 100)
        secondname = firstname + str(number)
        doubling = test_for_inclusion(secondname, namefile)
        if doubling == 0:
            doubling0 = 0
            for element in names:
                if secondname == element:
                    doubling0 = 1
            if doubling0 == 0:
                names[counter] = secondname
                counter += 1
    return names


def new_names2(firstname, namefile):
    doubling = test_for_inclusion(firstname, namefile)
    if doubling == 1:
        names = new_names(firstname, namefile)
        print("Такое имя уже существует. Выберите из предложенных\n",
              ', '.join(names))
        firstname = input()
        new_names2(firstname, namefile)
    if doubling == 0:
        return firstname


def main():
    if len(sys.argv) == 1:
        namefile = 'list_names.txt'
    else:
        namefile = sys.argv[1]
    if not os.path.exists(namefile):
        myfile = open(namefile, 'w')
        myfile.close()
    firstname = input('Введите имя\n')
    firstname = new_names2(firstname, namefile)

    with open(namefile, 'a') as myfile:
        print(firstname, file=myfile)
    print('Пользователь зарегистрирован')

if __name__ == '__main__':
    main()
