def myName(name: str):
    print("Hello! My name is " + name + "!")

def executeScript(name: str, toggle:bool=None):
    if __name__ != "__main__": # Turn the logic of this line from Not Equals to Equals
        myName("name")
    else:
        print("...logic steered here...")
    if (toggle!=None):
        print("The toggle is set to " + str(toggle))
    else:
        print("Toggle has not been set, because it is optional")
    print()

executeScript("Marc John Benamera")
executeScript("Marc John Benamera", True) # Turn this argument to False to switch the possible output
# Before sending your pull request, change the name inside the executeScript with your own name
