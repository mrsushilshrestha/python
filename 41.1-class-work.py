#create a list
list_create= [] #null list create
list_create=[1,2,4,"sushil"]

print(list_create)

#using the for loop access List 
list_items =[2,3,"sushil","shrestha"]
i = 0
while i < len(list_items):
    print(list_items[i])
    i += 1
    
#using for loop access List
for i in list_items:
    print(i)

#how to add items and remove from list?
#add items in list
list_add =[]
num=int(input("enter the Number of items you add: "))
for i in range(0,num):    
   list_add.append(input("Enter the Items: ")) #add item in the list
   
print(list_add)


#remove items from list
items=input("Enter the Items to remove: ")
list_add.remove(items)
print(f"after the items Remove from the list: {list_add}")

#update items in list
index =int(input("Enter the index position you want to add element: "))
element =input(f"Enter the Element you add in index position{index}: ")
list_add.insert(index,element)
print(f"New list is:{list_add}")

#change Items in this list
print("You want to change element press (1/0)")
num =int(input())
if 1==num:
   index =int(input("enter the index position: "))
   element =input("enter the elements: ")
   list_add[index]=element
   print(list_add)
else:
    pass

#what is dictionary with example? how to create dictionary?
#create dictionary
create_dict ={} 
create_dict={"name":"sushil","class":"bachelor","subject":{
    "english":90,"math":95
}}


#access items in dictionary
print(create_dict["name"])
print(create_dict["subject"]["english"])

#add key and value to dictionary
create_dict["surname"]= "shrestha"

#change value of specific key in dictionary
create_dict["name"]="Shayam"
print(create_dict)