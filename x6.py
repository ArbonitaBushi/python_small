def helloyou():
    name = input ('What is your name?'.upper())
    greet = f'Hello {name}!'.upper()
    count = len(name)
    print(greet) 
    print(f'You have {count} letters in your name.'.upper())
print(helloyou())
