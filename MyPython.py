def myName(name: str):
    print("Hello! My name is " + name + "!")

def executeScript1():
    if __name__ != "__main__": # Turn the logic of this line from Not Equals to Equals
        myName("Marc John Benamera")
    else:
        print("...is main")

def executeScript2(toggle: bool):
    if toggle == True:
        myName("Marc John Benamera")
    print("Toggle is " + str(toggle))

executeScript1()
executeScript2(True) # Turn this argument to False to switch the possible output
