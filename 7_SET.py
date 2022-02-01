#unorder collection of unique order items
#set doesnt store tuple,list
#index nahi hota hai
s={1,2,3,4,4}
print(s)
l=[1,1,2,3,4,5,5,5,5]
print(list(set(l)))  #remove duplicates

#set methods
#add #remove// #discard
s={1,2,3}
s.add(4)
print(s)

s.remove(3)
print(s)

s.discard(2)
print(s)

s.clear()
print(s)

s.copy()
print(s)

#in keyword in sets and for loop
s={'a','b','c'}
#in keyword to check if item is present or not in set
if 'a'  in s:
    print('p')
else:
    print('np')

#for loop
for item  in s:
    print(item)        

#set math
s1={1,2,3,4}
s2={3,4,5,6}


#<<union>>
c=s1|s2
print(c)


#<<intersion>>
c=s1 & s2
print(c)

#symmetric difference 
a=[10, 20, 30]
a1=[10, 20, 40]
print(set(a).symmetric_difference(set(a1)))
