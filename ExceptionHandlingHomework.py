for i in ['a','b','c']:
    try:
        print(i**2)
    except:
        print("Cannot raise that to the power of 2.")
x=5
y=0
try:
    z = x/y
except ZeroDivisionError:
    print("Nothing can be divided by 0.")
except:
    print("An unknown error has occured.")
finally:
    print("All Done!")
def ask_for_int():
    while True:
        try:
            integer = int(input("Input an integer: "))
        except:
            print("An error occured!")
        else:
            print(f'Thank you, your number squared is {integer**2}')
            break
ask_for_int()
