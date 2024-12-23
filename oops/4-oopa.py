dictionary_employee={}
list_employee=[]
new_salary=[]
for i in range(3):
    dictionary_employee["name"]=input("Enter the Name of employee: ")
    dictionary_employee["salary"]=input("Enter the Salary of employee: ")
    dictionary_employee["bonus"]=input("Enter the Bonus of employee: ")
    
    list_employee.append(dictionary_employee)

for items in dictionary_employee:
    print(items["salary"])

    

    



