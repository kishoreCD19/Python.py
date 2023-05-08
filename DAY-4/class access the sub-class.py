class a:
    def __init__(self,x=3):
        self._x=x
        
class b(a):
    def __init__(self):
        super().__init__(5)
    def display(self):
        print(self._x)
def main():
    obj= b()
    obj.display()
main()


// output = 5 //
