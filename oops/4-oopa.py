# list_employee=[
#     {"name":"sushil","salary":"18000","bonus":"10"},
#     {"name":"ram","salary":"19000","bonus":"30"},
#     {"name":"hari","salary":"28000","bonus":"20"}
# ]

# # print(list_employee)
# def bonus_Calculation(salary,bonus):
#     bonus_amount= salary*bonus/100
#     net_salary = salary+ bonus_amount
#     return net_salary

# bonus_Calculation(1000,10)
# for items in list_employee:
#     name =items["name"]
#     salary =int(items["salary"])
#     bonus= int(items["bonus"])
    
#     net_salary_employee=bonus_Calculation(salary,bonus)   

#     print(f"The salary of {name} is: {salary} and bonus is: {bonus} the net salary is: {net_salary_employee}")

class Employee:

    def __init__(self,salary=0,bonus=0):
        self.list_employee=[
        {"name":"sushil","salary":"18000","bonus":"10"},
        {"name":"ram","salary":"19000","bonus":"30"},
        {"name":"hari","salary":"28000","bonus":"20"}]
        # print("Running Check....")
        self.salary=salary
        self.bonus =bonus

    def bonus_calculation(self):
        return self.salary*(100+self.bonus)/100


    def list_empoyee_detail(self):
        for items in self.list_employee:
            name =items["name"]
            salary =int(items["salary"])
            bonus= int(items["bonus"])
    
            emp=Employee(salary,bonus) 
            net_salary =emp.bonus_calculation()
            
            print(f"The salary of {name} is: {salary} and bonus is: {bonus} the net salary is: {net_salary}")

    
empy =Employee()
empy.list_empoyee_detail()





