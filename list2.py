first_list =["apple", "ball",1,2]
print(first_list[1:4])
print(first_list[::-1]) #print reverse order

list_constructor=list((5,9,"cat","dog")) # second method create list
list_constructor.append("mango") 
print(list_constructor)

for item in first_list: #loop in list
    print(item)
    

#WAP to remove duplication item from list ["apple","ball", "cat","5"."7","5"]

list_duplication = ["apple","ball","ball", "cat","5""7","5"]

for items in list_duplication:
    if(items==list_duplication):
        continue
    
print(items)
      
     
