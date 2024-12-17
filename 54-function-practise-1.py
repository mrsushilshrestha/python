#1.WAF to print the length of the list, or any string
def length_finder(length):
    total_length = len(length)
    print(total_length)
      
list_items =["apple", "ball", "cat","mouse"]
list_items1=["a",2,3,1,4,5,6,3,2,4,"a",'v',1,2,3]
string_variables ="sushil shrestha, I am IT student."


length_finder(list_items)
length_finder(list_items1)
length_finder(string_variables)


#2.WAF to print the element of the list
def print_function(list_items3):
    for items in list_items:
        print(items , end=" ")
    
print_function(list_items)
print()


#3.WAF to find the factorial (1*2*3*4*5 =5!)
def factorial(number):
    fact =1
    for i in range(1,number+1):
        fact *=i  #calculated factorial
    
    print(f"Factorial Of {number} is:",fact) 
        
factorial(5) #passing value to the factorial function


#4.WAP to calculate the USD to NP
def forex_Convert(USD):
    NP = USD*135.71
    print(f"Currect Price OF USD: {USD} Into NP: {NP}")

forex_Convert(2)

#WAF to find the ODD EVEN
def odd_even(number):
    if number%2 ==0:
        print("Even Number")
    else:
        print("Odd Number")
        
odd_even(3)
odd_even(108)


