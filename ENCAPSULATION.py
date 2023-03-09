#protected
class encap:
    _a=10
    c=20
    def encapfunction(self):
        _b=200
        print("encap function-accessing protected")
        print(self._a+10)
obj=encap()
print(obj._a)
obj.encapfunction()
print(obj.c)
o/p=
10
encap function-accessing protected
20
20

#private
class encap:
    __a=10
    print(__a)
    def encapfunction(self):
        print("encap function")
        print(self.__a)
obj=encap()
obj.encapfunction()
print(obj.__a)
#it will through error bcs a is a private cant
#acessed outside class
o/p=
10
encap function
10
