print("Hello")
print("Are you solving for leg or hypotenuse?")
question1 = input()
if question1 == "hypotenuse":
    print("What is your first leg?") 
    leg1 = int(input())
    print("What is your second leg?")
    leg2 = int(input())
    print("The hypotenuse is " + str((((leg1**2) + (leg2**2)) ** (1/2))))
else:
    print("What is the hypotenuse?")
    hypotenuse2 = int(input())
    print("What is the first leg?")
    leg3 = int(input())
    print("The missing leg is " + str((((hypotenuse2**2) - (leg3**2)) ** (1/2))))
# if   " What is your first sidelength?":
#     print("sidelength=A")
# if "What is your second sidelength":
#     print("second sidelength = b")
# if "What is the Pythagorean theroum?":
#     print("a**2 + b**2 = c**2 (pythagorean theorum)")

# #what is your first sidelength? a
# #what is your second side length? b 
# #pythagorean theroum? (a**2 + b**2 = c**2)

# #formula is ((a**2 + b**2) ** (1/2))

# if "What is the length of a?":
#     print 


#for finding out length a or b 

#formula is ((leg3**2 - leg2**2) ** (1/2)

