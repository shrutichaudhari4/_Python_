#TUPLES
#store any type or data type
#tuple are immutable i.e cannot change
#once tuple is created then you can't change it
#tuple are use when you knoow that data can't change
#e.g 7 week days, 12 month etc
#no append ,no insert ,no pop ,no remove
#tuples are faster then list
#()
#tuple me * operator use hota hai for unpacking of a tuple

#methods 
#count
#index
#len 
#slicing tuple

count
a=(1,2,2,3,4)
print(a.count(2))


#length
a=("apple", "banana", "cherry")
print(len(a))

#index
print(a[1])

#negative index
#-1 refers to the last item, -2 refers to the second last item etc.

a= ("apple", "banana", "cherry")
print(a[-1])

#One item tuple, remember the comma:
a=("apple",)
print(type(a))

#looping in tuple
a=(1,2,3,4.0)
for i in a:
    print(i)

#list inside tuple
a=('red',['yello','blue'],'black')
a[1].pop()
a[1].append(" beautiful colours ")
print(a)

#min(),max(),sum
a=(1,2,3,4.0)
print(min(a))
print(max(a))
print(sum(a))
