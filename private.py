class myclass:
    __privateVar =27;
    
    def __priMeth(self):
        print("I'm in the classroom")

    def hello(self):
        print("Private valiable value:",myclass.__privateVar)

foo=myclass()
foo.hello()
foo.__priMeth
