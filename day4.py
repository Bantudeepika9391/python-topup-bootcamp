''' ======day--4
inheritance :
in java we use extend to take the class
in py we ()
==========
code:
class A :
 var1=10;
 def test(self):
  print("iam in a")
classB(A):
var2=50;
def run(self):
print("iam runnings")
a1=A()
b1=B()
b1.test()
a1.run()
class c(b):
var3=89
def stop(self):
 print("i am stopped")

=======MR0(method of re.... order)====='''
class A:
 college="Iare"
  def __init(self,name,age):
    slef.name=nameslef.age=age
a1=A("deep",45)
a2=A("manvi",12)
a3=A("dharu",13)
a1.college
A.college
A.college="ABCD"
print(a1,college)


=======Decotors==(inst=static)
it function take the function change the function return function
*static method
*it take the instance var
class B:
    var2=5010
    @Staticmethod
    def test():
        print("iam runing")
        @classmethod
        def run(cls):
            cls.var2=80
            print("runing")
        B.run()
        b1=B()
        b1.test()



============dunder==
class Student:
    def __init__(self,name,phy,chem):
        self.name=name
        self.phy=phy
        self.chem=chem
s1=student("rita",56,78)
s2=student("deep",45,78)
s1.findsum(self)
def finddum(self):
    s=self.phy+self.chem+ob.phy+ob.chem
    return s
print("function called", s1.__add__(s2))
print(s1+s2)
print(s1-s2)

=========
class Csr:
    def __init__(self,type=none,name=none):
        if type in none and name=none:
            peinr(no srg pass)
        elif name is none:
            self.typ=type
        else:
            self,type=type
            self.name=name
    c1=car()
    c2=car("electic")
    c3=car("petrol")
    c1.test(1,8,9)
    c1.test(name="rahul",age=24,school="sr")

    def test(self,*args)#tuple  #pass the argments #if ** are dict
      print(args)
                        


