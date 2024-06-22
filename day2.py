'''#Day-2-Module
*predefined
*any python file


a=10
def greet():
    print("Hello world")


#packages:
collection of modules
 __init__.py
 folder--files
package is a folder with many files
we import only module not packages
we import:
    import package1.test1 as p
    p.greetings()
if two module are not same path(error)
we have to set a path of abs from the directary


package=> p1-f1.py
        p2-f2.py
f2.py code:
    import f1
    f1.test()
    (f1 not found beacuse diff dict)
    we should set path by using import os,sys
    os.jion(add the path)


code------------------
import os
import sys
module_path=os.path.abspath(os.path.join("..\p1")
            sys.path.append(module_path)
            import f1
            f1.test
            --------------------------

libary:
    collections of modules and packages
---------------------

txt files--
1)open
2)read(r)
3)append(a) --add the end of the file
4)write(w)--write
5)remove(import os)delete
6)creat-(X)
f=open("path","mode")


code h/w:------
1q)

f=open("D:\\python\\7daystopup\day2fle.txt","r")
print(f.read())

import os
import sys
from day2fle import h
f=open("D:\\python\\7daystopup\day2cret.txt","x")
f=open("D:\\python\\7daystopup\day2cret.txt","a")
f=open("D:\\python\\7daystopup\day2cret.txt","r")
print(f.read())


-----------cvs---
common seperated values in excel sheet

with(close the file handle the expection)

1) open("path","mode")
2) close()
3) with open(--)

import csv
f=open("student.csv","r")
csvreader=csv.reader(f)
headers=next(csvreader)
for i in csvreader:
    print(i)



csv===list
the outpout in list from if we use the next function the header will not print

-------------
import csv
f=open("std.csv","r")
csvreader=csv.reader(f)
headers=next(cvsreader)
print("header::",header)
print("data::")
for i in cvsreader:
    print(i)

--------------------
a=["deep",138,90]
import csv
f=open("std.csv","w")
csvwriter=csv.writer(f)
csvwriter.writerrow(a)   ---rows'''
----------------------







    
