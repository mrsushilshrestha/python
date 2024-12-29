#Perform the CRUD(Create , Read , Update ,Delete) in Python using List ,Dictionary,Tupple
command ='y'
total_result=[]
while command =='y':
    welcome_message = """
    ***Welcome The College Management System***
    1) Create record
    2) Read Student
    3) Update Student
    4) Delete Student
    5) Exit From System
    """
    print(welcome_message)
    
    option =int(input("Enter The Following Option[1,2,3,4]: ")) #take user input
        
    if option == 1: #create Record     
        dic_student={}
        dic_student["id"] = input("Enter the ID of Student: ")
        dic_student["name"] = input("Enter the Name: ")
        dic_student["roll"] = input("Enter the Roll No: ")
        dic_student["subject"] = input("Enter the Subject: ")
    
        total_result.append(dic_student)
        print(total_result)
    
    elif option ==2: #read Record
        user_search = input("Enter the Name For Search ")
        for items in total_result:
            if user_search ==items["name"]:
                print(items)
            else:
                print("No Any Data Found!!!")
                
    elif option==3: #update record(Rename or Update Name)
        user_update =input("Enter the name for update!!! ")
        for items_update in total_result:
            if user_update == items_update["name"]:
                items_update["name"] =input("Enter New Name For Modification ")
                print("Update Successfully !!! ")
                print(f"New Update: {items_update}")
                
            else:
                print("Data Doesn't Exit!!! ")
    
    elif option ==4: #delete Record
        user_delete =input("Enter the Name for delete ")
        for items_delete in total_result:
            if user_delete ==items_delete["name"]:
                # del items_delete["id"]
                # del items_delete["name"]
                # del items_delete["roll"]
                # del items_delete["subject"]
                total_result.remove(items_delete)
                
                print("Deteled Successfully!")
                print(items_delete)
            else:
                print("No Data Found !!!")
    else:
        print("invalid!!!") #This Execute if option not [1,2,3,4]
        
    
    command=input("Do You Want To continue ") #for continue opeation or Control while loop
    if command =='y':
        print("Welcome Back!!!")
        command='y'        
    elif command =='n':       
        print("Thank You For Using Our service!!!")
        command='n'
    else:
        print("Invalid Options")
