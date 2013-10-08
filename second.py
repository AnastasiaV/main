import random

def main():
    a=input('Введите имя')
    f=open('list_names', '+')
    doubling=0

    for element in f:
        if a==element:
            doubling=1
            break


    if doubling == 1:
        random.shuffle(a, [rand])
        
    
        
        
              
    
        
if __name__ == '__main__':
    main()
    
