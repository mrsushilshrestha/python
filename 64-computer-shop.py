import os
class Computer_shop:

    def __init__(self,path): 
        self.path =path

    def write_function(self,name,brand,id): #wite function 
        self.name =name
        self.brand =brand
        self.id =id

        with open(self.path,"a+")as file:
            file.write(self.name+", ")
            file.write(self.brand+", ")
            file.write(self.id) 
            file.write("\n")           

    def read_function(self,word): #read function
        with open(self.path,"r")as file:
            data = True
            # line=1
            while data:
                data=file.readline()
                if word in data:
                    print(data)
                    return
                else:
                    # line+=1
                    pass
            return print("Not Found!!!")     

    def update_function(self,old_name,update_name): #update function
        self.old_name = old_name
        self.update_name =update_name

        # with open(self.path,"a+")as file: #to update and Read data using the [a+] append mode
        #     file.write(self.update_name+", ")
        #     file.write(self.update_brand+", ")
        #     file.write(self.update_id+", ")
        #     file.write("\n")
        
        with open(self.path,"r") as f:
            data =f.read()            
            new_data=data.replace(self.old_name,self.update_name) 
            # print(new_data) 
        
        with open(self.path,"w+") as f:
            f.write(new_data)
            
    #DANGER!!!
    def delete_function(self): #delete function
        # os.remove(path)
        print("Sorry This Feature Not Available At The Moment!!! ")
        pass




#---------value passing section------------------------------------------------------

message="""
Enter the Option
1>Write Data
2>Read Data
3>Update Data
4>Delete Data 
"""    

option =input(message)
path ="Computer_shop.txt"
computer_shop_obj =Computer_shop(path)

#condition for Operations
if option=='1': #Write data
    print("Enter the Required Data... ")
    name =input("Enter the Name Of Customer:- ")
    brand =input("Enter the Brand Of Computer:- ")
    id =input("Enter the Id of Customer:- ")
    computer_shop_obj.write_function(name,brand,id)

elif option=='2': #for read data
    word=input("Enter the Name to search: ")
    computer_shop_obj.read_function(word)
    
elif option=='3': #for read data
    print("You Click Update Option...")
    old_name =input("Enter the Old Name Of Customer: ")
    update_name =input("Enter the Name Of Customer: ")    
    computer_shop_obj.update_function(old_name,update_name)
    
elif option=='4': #for read data
    computer_shop_obj.delete_function()
    
else:
    print("Invalid Option !!!")