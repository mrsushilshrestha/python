# class Student:
#     def __init__(self,che,phy,math):
#         self.phy=phy
#         self.che=che
#         self.math=math

#         self.percentage=str((self.phy+self.math+self.che)/3)+"%"
    
#     def calculation(self):
#         # self.percentage = "{:.2f}".format((self.phy + self.math + self.che) / 3) + "%"
#         self.percentage = f"{(self.phy + self.math + self.che) / 3:.2f}%" 

#         return self.percentage

        
# obj =Student(90,40,80)
# print(f"Without using the Function:- {obj.percentage}")

# obj.phy=80
# print(f"Without using the Function update mark:- {obj.percentage}")

# print(f"With using the Function update mark:- {obj.calculation()}")
# print(f"updated percentage:- {obj.percentage}")



# #-----------------using-decorator-------------------
class Student:
    def __init__(self,che,phy,math):
        self.phy=phy
        self.che=che
        self.math=math

    @property
    def calculation(self):
        return f"{(self.phy + self.math + self.che) / 3:.2f}%" 

        
obj =Student(90,40,80)

obj.phy=30
print(f"updated percentage:- {obj.calculation}")


# @getattr
# @setattr