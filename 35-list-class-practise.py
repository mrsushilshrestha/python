#WAP to remove duplication item from list ["apple","ball", "cat","5"."7","5"]

list_duplication = ["apple","ball","ball", "cat","5","7","5"]
list_duplication_remove =[]

for items in list_duplication:
    if items in list_duplication_remove:
        continue
    list_duplication_remove.append(items)
    
print(list_duplication_remove)
    

      