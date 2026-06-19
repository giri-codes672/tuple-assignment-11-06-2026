#Create a Python script that generates a tuple containing the names of 5 different cities.
t1=("hyderabad","chennai","bengaluru","kadapa","tirupati")
#Write a function that takes a tuple as an argument and returns the first and last elements of the tuple.
def first_last_elements(t1):
    return t1[0],t1[-1]
print(first_last_elements(t1))
#Create a tuple of tuples, where each inner tuple contains a student's name and their corresponding grade (e.g., ( ("John", 85), ("Alice", 92) )).
t2=(("madhu",89),("giri",90),("sudheep",90),("niru",88))
#Implement a function that takes the tuple of tuples from the previous task and returns a new tuple with the students' names sorted in alphabetical order.
t3=sorted(t2)
print(t3)
#Practice tuple unpacking by writing a function that takes a tuple of 3 elements and assigns each element to a separate variable, then prints out the values of these variables.
t4=("hyderabad","chennai","bengaluru")
a,b,c=t4
print("first element:",a)
print("second element:",b)
print("third element:",c)
