#Topic explanation:
#Function is a line or block of code that allows user to use it again and again to perform the same or certain task whenever needed
#It works by defining the function and calling the function afterwards

#Key Vocabulary:
#Functions: A reusable block of codes that allows user to perform task
#Parameter: Variable or a placeholder that is inside the function
#Argument: The value that is stored to a function once called
#Return Value: The return sends back the result using function

def organize (numbers):
 organized = sorted(numbers)
 return organized

numbers = [100, 3223, 112, 2222, 52029, -2]

result = organize(numbers)

print("Unsorted Numbers",numbers)
print("Organized Numbers",result)

#Output:
#Unsorted Numbers [100, 3223, 112, 2222, 52029, -2]
#Organized Numbers [-2, 100, 112, 2222, 3223, 52029]

#Reflection:
#I know what a function can do as a block of code that can be reused,
#but I was confused about how parameters, arguments, return value works.
#while searching, I find it difficult to understand, despite searching for exact words I needed
#for me to understand better, I still got confused, but then I tried copying one example I find.
#I read the code itself and then read the definitions across the internet again and I began to comprehend 
#the codes that I usually confused with. I did try several function for me to understand the topic as well as
#making more mistakes for parameters, arguments and return value. I learned that parameters are used to define
#a function, argument are the values that given to function when called and return value sends 
# a result back from the function, I initially made a mistake by not using the (numbers) causing an error.
# The return value was miscalled and the argument have a different variable name, after analyzing it
# I finally found the mistake I made.
