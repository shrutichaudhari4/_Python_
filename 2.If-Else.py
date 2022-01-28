age=int(input("enter the age"))
if age>=18:
   print("you can vote")
else:
    print("you can't vote") 

#number gussing game
#NESTED IF-ELSE

a=24
guess=int(input("enter the number:"))
if guess == a :
    print("YOU WIN")
else:    
    if guess<a:
        print("TOO LOW")
    else:
        print("TOO HIGH")




