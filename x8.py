weekdays = {'Sunday': 0, 'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thurday': 4, 'Friday': 5, 'Saturday': 6}
def day():
    while True:
        my_day = input('What is your favorite day?')
        try:
            print(weekdays[my_day])
        except: 
            print('I\'m not sure what your mean.')
print(day())
