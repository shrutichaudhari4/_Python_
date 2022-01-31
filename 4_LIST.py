# #set of values which contain value of any data type
#list=["kundra","luthra",55,48,0.99,false]
lst = input("Enter the numbers in list seperated by comma: ").split("/")
print(lst)

# Append, concatenation, extend function in list:
l1 = [1,2,3,4,5]
l2 = [6,7,8,9]
# Append:
l1.append(l2)
print(l1)
# # Extend :
l2.extend(l1)
print(l2)
# # concetation:
l1 = l1+l2
print(l1)

# Sort , reverse
l = [2,43,6,3,6,3,64,32,435,32]
l.sort()
print(l)

# l.reverse()
# print(l)

# Insert , index , remove, overwrite element
l = [1, 2, 3, 4, 5, 6]
l.insert(2,0)
print(l)
print(l.index(3))
l.remove(5)
print(l)

l[0] = 10
print(l)

l1[1,2,3]
l1.insert(3,6)
printl1

# clear, copy, count

a = [1, 1, 1, 12, 2, 2, 2, 24, 3, 3, 2, 26, 5, 4, 3, 2, 2, 2, 2]
b = a.copy()
print(b)

print(a.count(2))

a.clear()
print(a)

# Slicing In list :
lst = [1, 2, 3, 4, 5, 6, 7, 8]
print(lst[2:5]) #output = [3,4,5]
print(lst[::-1])  # output = [8, 7, 6, 5, 4, 3, 2, 1]

l = [1, 2, 3, 4, 5, 6]
l.remove(5)
print(l)
l.insert(8)
l.pop(2)
l.clear
print(l)
a=[1,[1,2,[1,2]]]
a.index(2)
print(len(a))
l=[11,12,13,14]
l.append(12)
print(l)
l.insert(3, 12)
print(l)

#1.Python program to interchange first and last elements in a list 
l=['a','b','c','d','e']
l1=[]
for i in l:
    if i=="a":
        print("e")
    else i=="e":
         print("a")    


