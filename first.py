def Faring(a=0):
    return (a*9/5+32)

def Kelvin(a=0):
    return (a+273)

def main():
        try:
            a=float (input('Введите градусы'))
        except ValueError:
            print ('Число введи, пожалуйста')
        else:
          
            if a<-273:
                print ('Что ты ввел вообще? Просили же температуру.Слишком низкая')
            elif a>=273000000000000:
                 print ('Что ты ввел вообще? Просили же температуру. Слишком высокая')
            else:       
                 print ('По Фарингейту в целых числах - ', Faring(a), 'По Кельвину в целых числах - ', Kelvin(a))
        
if __name__ == '__main__':
    main()
    
