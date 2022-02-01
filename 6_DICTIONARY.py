#dictiionaries
#{'key':'value'}
#why we use dict == list is not enough to represent real data


a={'name':'shruti','colour':'black'}
print(a['name'])
print(a['colour'])

user_info={'name':'shruti',
'age': '19',
'degree':'b.tech',
'sub':['m1','m2','m3'],
'fav_movies':['RAAZI','YJHD']}
print(user_info['fav_movies'])

# #how to add data to empty dict
user_info2={}
user_info2["name"]="priya"
print(user_info2)

#looping and in keyword in dict

user_info={'name':'shruti',
'age': 19,
'degree':'b.tech',
'sub':['m1','m2','m3'],
'fav_movies':['RAAZI','YJHD']}

#check if key exist in dict
if 'name' in user_info:
    print("present")
else:
    print("not present")


#<<<<<key method
user_info=user_info.keys()
print(user_info)

#check if values exist in dict
if 19 in user_info.values():
     print("present")
else:
    print("not present")

#<<<<<values method
user_info=user_info.values()
print(user_info)

#Loop
<<<keys
for i in user_info:
    print(i)
<<<values
for i in user_info.values():
    print(i)    

for i in user_info:
     print(user_info[i]) 

#<<<< ITEM METHOD>>>>

user_items=user_info.items()
print(user_items)
print(type(user_items))

# # it use for looping
for key,value in user_info.items(): #key=i and value =j
    print(f"key is {key} and value is {value}")

#add and delete data

user_info={'name':'shruti',
'age': 19,
'degree':'b.tech',
'sub':['m1','m2','m3'],
'fav_movies':['RAAZI','YJHD']}

 how to add data
user_info['fav_song']=['song1','song2']
print(user_info)

#delete or pop method
popped_items=user_info.pop('fav_movies')
print(f" popped items is {popped_items}")
print(user_info)

#popitem method when we want to delete random key value pair
popped_item=user_info.popitem()
print(user_info)
print(popped_item)

update

user_info={'name':'shruti',
'age': 19,
'degree':'b.tech',
'sub':['m1','m2','m3'],
'fav_movies':['RAAZI','YJHD']}
more_info={'state':'maharastra',
'hobbies':['coding','reading']}
user_info.update(more_info)
print(user_info)

#fromkeys,get,clear,copy

#fromkeys use to create dictionary
#different keys same values
d={'name':'unknown','age':'unknown'}
d=dict.fromkeys(['name','age','height'],'unknown')
print(d)
d=dict.fromkeys(range(1,11),'unknown')
print(d)

#get method
#use to acess the key

d={'name':'unknown','age':'unknown'}
print(d['names'])
print(d.get('name'))

if 'name' in d:
    print('p')
else:
    print('np')
#<<<orrr
if d.get('name'):
    print('p')
else:
    print('np')  
if none------> false else ---------->true

# in dict two keys are same then
user={'name':'shruti','age':20}
print(user.get('names'))
agar none nahi print karna hai toh yese karte hai
print(user.get('fav','not found !'))

# #clear and copy
d={'name':'unknown','age':'unknown'}
d.clear()
print(d)

# #copy
d1=d.copy()
print(d1)

#example
#cube finder
def cube_finder(n):
    cubes={}
    for i in range(1,n+1):
        cubes[i]=(i**3)
    return cubes
print(cube_finder(10))   


#word counter
def word_counter(s):
    count={}
    for i in s:
        count[i]=s.count(s)
    return count
print(word_counter('harshit'))  

#user input data
user={}
name=input('enter the name :')
age=input("enter the age : ")
fav_movies=input("your fav movies separated by,").split(',')
user['name']=name
user['age']=age 
user['fav_movies']=fav_movies
for key,values in user.items():
    print(f"{key}:{values}")



a = "w3resource"
for i in range(len(a)):
    print(f"Current character {a[i]} position at {i}")

