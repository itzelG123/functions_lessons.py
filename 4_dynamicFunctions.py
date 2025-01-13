# Dynamic Functions Practice #
#def check_3_digits(number):#parameter defing function
      #  return number in range (100,1000)

#result= check_3_digits(68) #arugment and both are needed to work
#print(result)


# def check_3_dijits(list1):
#     for n in list1:#iteration
#         if n in range(100,1000):
#             print( True)
#         else:
#             return False
# result=check_3_dijits([555,99,600])
# print((result))

# def check_3_dijits(list1):
#     three_digits_list=[]

#     for n in list1:#iteration
#         if n in range(100,1000):
#             three_digits_list.append(n)
#         else:
#             pass

#     return three_digits_list
    
# result=check_3_dijits([555,99,600])
# print((result))


# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.

# Don't call the function, you just need to define it.
# def all_positives(numbers): #def function with paramenter
#     for n in numbers:
#         if n in range(1,1001): #range that is acceptable
#             print(True)  
#         else:
#             return False
        
# result=all_positives([8,-370,723])#arugment 

# numbers=[8,-370,723]#list of number
# print((result)) #it will print whther its ttue or false 

# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list as long as they are greater than 0 and less than 1000, and returns the result of said sum. Create a numbers variable, storing a list of numbers so we can test it.
# def sum_less(num):#defines function
#     empty = []#empty list 
#     for n in num:
        
#         if n in num:
#             empty.append(n)#for while loop 
          
#         else:
#             pass#if n isnt in num then it will pass
   
#     return(num) #returns result to sum

# result=sum_less([1,200,999])#agruemnt
# num=[1,200,999] # List of numbers (argument)
# x=sum(num,0) #sum method
# print((x))#print sum


# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.
num=[1,2,3,4,5,6]
def count_even(numbers): #defines function
     empty=[] #empty list

     for n in numbers: #for loop
         
        if num % 2 == 0: #checking if the numbers in the list are even
            
            empty.append(n)
        
        else:
            pass
result=count_even([1,2,3,4,5,6])
print((result))
             






        