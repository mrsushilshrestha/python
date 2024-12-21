#list in python

marks =[20,21,22,23] #identify list

print(marks)  # to print the list
print(marks[0])  #print list value staring from 0
print(type(marks)) #check the types of the variable 
print(len(marks)) #check the lengt

print(marks.index(23))#to print occurance idex position

#In python we can store diffrent data type in one variable 
std_detail = [1,"Sushil Shrestha","Kathmandu_Nepal"]
print(std_detail) #print [1, 'Sushil Shrestha', 'Kathmandu_Nepal']
print(std_detail[1])


#In python List is Mutable and String are Immutable
std_detail[1]="Shiva Shrestha" #in python list is mutable or can change the value of the variables
print(std_detail[1])


#slice in list
numbers= [20,30,40,50,60,70]
print(numbers[1:5]) #print number from 1 to 4 index
print(numbers[:5]) #print from the first index
print(numbers[0:]) #print untill the last index if we miss the end

#negative index
print(numbers[-3:-1]) #print negative index (-5,-4,-3,-2,-1)
