
import random
import string
from tokenize import _all_string_prefixes

# spam = 7
# if spam > 5:
#     print("Five")
# if spam > 8:
#     print ("Eight")
    
    #Answer is 5 because 7 is greater than 5 but lesser than 8. So the First condition is met but the second isn't
    
    #Store5 names in an array named Joy and print the array using foreach.
    
# Joy = ['Seun', 'Peace', 'Sharon', 'Titilayo', 'Tayo']
# for friends in Joy:
#         print(friends)
        

# def multiply():
#     value1 = eval(input("First digit "))
#     value2 = eval(input("Second digit "))
#     process = (value1) * (value2)
#     return process
# print(multiply())
    
    
    
#Random Password generator




all_strings = string.ascii_letters+string.digits+string.punctuation
def RPGenerator():
    password = ""
    length = eval(input("Password Length? "))
   
    for p in range(length):
        password += random.choices(all_strings)
    return password
print(RPGenerator())
    
    