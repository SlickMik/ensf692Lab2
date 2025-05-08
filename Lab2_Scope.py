# ENSF 692 Spring 2025
# May 8 Lab 2
# Exercise 2
# Ibrahim Khan





# Trace through the execution of the following program. 
# Answer the questions in the comments with your group members.
# After discussing, use print statements to confirm your answers.

foo = 100
bar = foo
foo + bar


# print ("Point 1")
# print ("foo = ", foo)
# print ("bar = ", bar)


# POINT 1
# What is the value of foo at this point?
# The type of foo is 100

# What is the type of foo at this point?
# The type of foo is int

# What is the value of bar at this point?
#The value of bar is 100

# What is the type of bar at this point?
# The type of bar is int



spam = foo + bar
foo += 50
eggs = foo + bar
ham = [1, 2, 3]
baz = ham
ham.append(bar)


# print ("Point 2")
# print ("foo = ", foo)
# print ("bar = ", bar)
# print ("spam = ", spam)
# print ("eggs = ", eggs)
# print ("ham = ", ham)
# print ("baz = ", baz)


# POINT 2
# What is the value of foo at this point?
# The value of foo is 150

# What is the value of bar at this point?
# The value of bar is 100


# What is the value of spam at this point?
#   The value of spam is  200 
# What is the value of eggs at this point?
#   The vaue of eggs is 250

# What is the value of ham at this point?
#   The value of ham is [1, 2, 3, 100]


# What is the value of baz at this point?
#   The value of baz is [1,2,3,100]



eggs = "Python is very flexible!"
spam = ham
ham = bar
bar += bar
foo = eggs
eggs = bar + ham
baz.append(bar)


# print ("Point 3")
# print("ham:", ham)
# print("baz:", baz)
# print("eggs:", eggs)
# print("foo:", foo)
# print("bar:", bar)
# print("spam:", spam)


# POINT 3
# What is the value of foo at this point?
#   The value of foo is "Python is very flexible!"

# What is the value of bar at this point?
#   The value of bar is 200

# What is the value of spam at this point?
#   The value of spa is [1, 2, 3, 100,200]

# What is the value of eggs at this point?
#   The value of eggs is 300

# What is the value of ham at this point?
#   The value of ham is 100

# What is the value of baz at this point?
#   The value of baz is [1, 2, 3,100, 200]


# Print out the types and final values of each variable.

print("The final value of foo:", foo, "and the final type is type:", type(foo))
print("The final value of bar:", bar, "and the final type is type:", type(bar))
print("The final value of spam:", spam, "and the final type is type:", type(spam))
print("The final value of eggs:", eggs, "and the final type is type:", type(eggs))
print("The final value of ham:", ham, "and the final type is type:", type(ham))
print("The final value of baz:", baz, "and the final type is type:", type(baz),"\n")

print("This is Ibrahim Khan's Lab 2")
print ("My best skill is Web Development")



