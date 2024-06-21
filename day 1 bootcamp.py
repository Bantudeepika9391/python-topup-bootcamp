"""
#Day-1-topup Python
array:only single data type
list:diff data type
methods:
    a=[4,6,7,8]
    a.append(8)
    a.insert(index,number)
    a.pop(index)
    a.remove(number)
    a.sort()
    a[start:end:direction]
    x=list(map(int,input().split(' ')))
    .split()#list changes into str
    map:accpect the more paraments,it return object that y we should give the data type in the input
    
tuple:immutable(do not changes  )
t=(9) type=int
t=(9,) type=tuple
methods
len,count,index
set:
    unordered,{},no duplicates
    s={} type="dict"
    s.add()
    s.remove()
    s.intersection()
    s.different()
    s.union()
    set we cannt store list,dict
dict:
    d={"name":"deepika",
       "age":18
       }
    print(d(ages)) #error
    print(d.get(agess)) #none
    d.pop()
    del d()
1q) input a sent and print only those eords whose length is >2?

ans)
"""
"""
#code
t=[]
s=input().split()
for i in s:
    if len(i)>2:
        t.append(i)
print(t)
"""
"""
def unique(lst:list[str]):
    s=[]
    for x in lst:
        if lst.count(x):
            if lst.count(x)==1:
                s.append(x)
            else:
                retuen(x)
            return s
        """
     
    
    
