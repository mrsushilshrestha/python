list_employee=[
    {"name":"sushil","salary":"18000","bonus":"10"},
    {"name":"ram","salary":"19000","bonus":"30"},
    {"name":"hari","salary":"28000","bonus":"20"}
]

# print(list_employee)
def bonus_Calculation(salary,bonus):
    bonus_amount= salary*bonus/100
    net_salary = salary+ bonus_amount
    return net_salary

bonus_Calculation(1000,10)
for items in list_employee:
    name =items["name"]
    salary =int(items["salary"])
    bonus= int(items["bonus"])
    
    net_salary_employee=bonus_Calculation(salary,bonus)   

    print(f"The salary of {name} is: {salary} and bonus is: {bonus} the net salary is: {net_salary_employee}")


    

    



