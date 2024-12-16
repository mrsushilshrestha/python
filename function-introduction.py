#Function In Python

#Make sum function with arguments
def calculation_sum(a,b): #make Function Using Key Word "def"
    sum =a+b
    print(sum)    
    

calculation_sum(4,10) #function call with parameters
calculation_sum(10,20)


# no argument function created
def display_text():
    print("HEllO WORLD...")
        
display_text() #function call without any argument/parameters
display_text()


#function with return types
def sum(a,b):
    return a+b   

print(sum(2,3))