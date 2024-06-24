'''
-----oops------
----txt files---


f=open("D:\\python\\7daystopup\day3te.txt","r")
s=f.read()
print(s)

#reading the line
f=open("D:\\python\\7daystopup\day3te.txt","r")
s=f.readline() #for muplit line (lines) str fromt
#read lines are list of str
#for counting the line we can use lines
print(s) 


f=open("D:\\python\\7daystopup\day3te.txt","w")
s="hiiiiiiii"
f.write(s)
print(s)
print(f.write(s)) #9


f=open("D:\\python\\7daystopup\day3te.txt","a")
s=["i\n","am/n","manvii\n"]  # line by line))))))))))))))))))
f.writelines(s)
print(f)

--------json files------
like a dict ,key value pari
import json
f=open("D:\\python\\7daystopup\day3j.json","r")#reading
json.dump(student4,f,indent=4)
student4:{"name":"gayathri",
"age":18,
"clg":"iare"}

print(f.read())

read a json file which stroe a key as stud_rool and value in dict which store ite name, age,marks
creat a new file where only those stud data is stored whose agr <24

import json
f=open("D:\\python\\7daystopup\day3j.json","r")
f2=open("D:\\python\\7daystopup\day3j2.json","a")
if ["age"]<24:
    f2.append(age)

print(f2.read())

=====================================================================
import json
f=open("D:\\python\\7daystopup\day3j.json","r")
f2=open("D:\\python\\7daystopup\day3j2.json","a")
s=json.load(f)
for i in s:
    d=s[i]
    if d["age"]<24:
        result[i]=d
json.dump(result,f2,indent=4)
+++++++++++++++oops++++++++++++++++
object:general enteriree----ogjname=classname()
class:name Cap
inkdilist we use the class
const(__)=class name
'''
#class Car:
    #color="green"
    #type="electric"
    #mileage=250
  #function
def changeVlues(self,c,t,m):  #name such de____(const)
     self.color="c"
     self.type="t"
     self.mileage=m
c1=Car()
c1.changeValues("black","prt",2003)
c2=Car()
#c1.color="black"
print(c1.color)
print(c2.color)












