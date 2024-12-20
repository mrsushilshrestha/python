# # list
# list_example=[]  #list creation
# list_example.append(input("Enter the Name of first Movie: "))
# list_example.append(input("Enter the Name of second Movie: "))
# list_example.append(input("Enter the Name of third Movie: "))
# list_example.append(input("Enter the Name of fourth Movie: "))

# print(list_example) #movie list print


# #list delete
# list_example.remove(input("Enter the Element to remove from the list: "))
# print("New movie list after the deletions:-",list_example)

# #search items 
# search_items =input("Enter the Element to search:- ")
# for items in list_example:
#     if(items==search_items):
#         print("Found!!!")
#     else:
#         print("Not Found!!!")        
        
# #update
# index_position = int(input("Enter the index to add element"))
# update_list =input("Enter the Element to search:- ")

# list_example.insert(index_position,update_list)
# print("New List is: ",list_example)

#dictionary
create_dictionary ={"name":"sushil","roll":"12","class":"bachelor"}



# delete update
delete_update=list(create_dictionary)
delete_items=input("Enter the element: ")
for items_delete in create_dictionary:
    if items_delete["name"]==delete_items:
        items_delete.remove(["name"])
        print("new element in dictionary is: ",delete_update)
        print(delete_update)
else:
    print("date Not found!")




