
def multiply(num1, num2):
    numbers = num1*num2
    return numbers 

print(multiply(3, 4))

print (9%3)

def modulo(num1, num2):
    if (num1%num2==0):
        return num1, num2
    else: 
        return -1

print (modulo(8, 3))

def words():
    return "Hello World"

print(words())

def house():
    arr = ['a', 'e', 'i', 'o', 'u']
    h = input('Where do you live?')
    if (h[0].lower() in arr):
        return f'I live in an {h}.'
    else:
        return f'I live in a {h}'
    
print(house())

