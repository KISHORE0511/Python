def add(value1,value2):
    return value1+value2
def sub(value1,value2):
    return value1-value2
def mul(value1,value2):
    return value1*value2
def divide(value1,value2):
    return value1/value2
def floordiv(value1,value2):
    return value1//value2
def power(value1,value2):
    return value1**value2
def modulus(value1,value2):
    return value1%value2==0

def main():
    symbol=input('select your symbol : ')
    value1=int(input('enter your first number : '))
    value2=int(input('enter your second number : '))
    
    if(symbol=='+'): print(add(value1,value2))
    elif(symbol=='-'): print(sub(value1,value2))
    elif(symbol=='*'): print(mul(value1,value2))
    elif(symbol=='/'): print(divide(value1,value2))
    elif(symbol=='//'): print(floordiv(value1,value2))
    elif(symbol=='**'): print(power(value1,value2))
    elif(symbol=='%'):print(modulus(value1,value2))
    else: print('your had entered a wrong one')
    

if __name__=='__main__':
    main()