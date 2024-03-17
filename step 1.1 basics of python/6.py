"""
    Functions
"""

def print_message():
    # function with no argument .
    print("Hello world")

def print_name(name):
    print("your name is : ", name)
    

""" 
    *args 
    This way the function will receive a tuple of arguments, and can access the items accordingly:
"""
def my_function(*kids):
  print("The youngest child is " + kids[2])
  
    
"""
    keyword argument
    You can also send arguments with the key = value syntax.
    This way the order of the arguments does not matter.
"""
def my_function_2(child3, child2, child1):
  print("The youngest child is " + child3)


"""
    **kwargs
    This way the function will receive a dictionary of arguments, and can access the items accordingly:
"""
def my_function_3(**kid):
  print("His last name is " + kid["lname"])
    
"""
    default parameter 
    If we call the function without argument, it uses the default value:
"""
def default_param(country = "Norway"):
  print("I am from " + country)

# This is the driver code of the python
if __name__ == "__main__":
    pass    # pass keyword execute the next line in the file . 
    # print_message() # invoke the print message funtion 
    # print_name("abhishek") # invoke the print name function 
    # my_function("Emil", "Tobias", "Linus") # invoke the my_function
    # my_function_2(child1 = "Emil", child2 = "Tobias", child3 = "Linus") # invoke function my_function_2
    # my_function_3(fname = "Tobias", lname = "Refsnes")
    
    default_param("delhi")  # invoke function default_param
    default_param()  # invoke function default_param

    