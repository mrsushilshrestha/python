list = [1,3,2]
string_list = ["Sushil" ,"Sailendra" , "Ashish"]

list.append(4)#adds one element at the end
print(list)

list.sort() #sorts in ascending order
string_list.sort() #sort string in ascending order
print(list)
print(string_list)

list.sort(reverse=True) #sort descending order
print(list)

list.reverse() #reverses list
print(list)

#list.insert(idx,el) #insert element at index 