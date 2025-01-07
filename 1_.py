# #FUNCTIONS ARE WAYS TO WRAP YOUR CODE
# #INTO REUSABLE UNITS
from determineEligiblity import determineEligiblity_tograduate,listOfMovies
# #define function wuth def
# #only define the function once
# #when i pass in a parameter,
# #i am passing in a palceholder for future information 
# def say_hello(name,age,address):
#     print(f"hello{name}")
#     print(f'how are you{name} ')
#     print(f"{name} are {age}years old")
#     print(f"{name}loive in {address}")
# #call function also known as invoking a function
# #pass info called an agrument
# say_hello('alice',22,'main ST')
# say_hello('paul',34,'side ST')
# say_hello('bob',56,'upside down')
# say_hello('Altair',45,'101 main st')

determineEligiblity_tograduate('alice',120,2.0,800)
determineEligiblity_tograduate('bob',119,1.9,799)

listOfMovies('the matrix',10,'action')
listOfMovies('the hangpver',5,'comedy')
listOfMovies('the ring',3,'horror')