list = [1,3,2]
string_list = ["Sushil" ,"Sailendra" , "Ashish"]

list.append(4)#adds one element at the end
print(list)

list.sort() #sorts in ascending order
string_list.sort() #sort string in ascending order
print(list)
print(string_list)

print("reverse")
list.sort(reverse=True) #sort descending order
print(list)

list.reverse() #reverses list
print(list)


#.insert(index,Element) #insert element at index 
#It add the element at the particular index or position
#If we want to add Element 5 at the position 2 
list.insert(2,5)
print(list)


#remove occurance of element
list.remove(5) #remove five occurance of element
print(list)

#remove element at index
list.pop(1)
print(list)
