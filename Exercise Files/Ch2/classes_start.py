#
# Example file for working with classes
#

class myClass():
    def method1(self):
        print("class1")

    def method2(self, str):
        print("class2" + str)

# inherit a class
class anotherClass(myClass):
    def method1(self):
        # inherits myClass#method1
        myClass.method1(self)
        print("another1")

        # overwrites myClass#method2
    def method2(self, str):
        print("another2")


def main():
    # instantiate object instance
    c = myClass()
    c.method1() #class1
    c.method2("string") #class2string

    c2 = anotherClass()
    c2.method1() #class1 / another1
    c2.method2("string") #another2

if __name__ == "__main__":
    main()
