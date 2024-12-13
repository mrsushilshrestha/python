option = 1
total_data = []
while option == 1:
    welcome_message = """
    ***Welcome The College Management System***
    1) Create record
    2) Read Student
    3) Update Student
    4) Delete Student
    5) Exit From System
    """
    print(welcome_message)

    num = int(input("Enter the Options: "))
    list_student_detail = []
    

    if num == 1:
        dic_student = {}
        dic_student["id"] = int(input("Enter the ID of Student: "))
        dic_student["name"] = input("Enter the Name: ")
        dic_student["roll"] = input("Enter the Roll No: ")
        dic_student["subject"] = input("Enter the Subject: ")

        total_data.append(dic_student)  

    elif num == 2:
        search_input = input("Enter the element you want to search: ")
        found = False 
        for items in total_data:
            if search_input == items["name"]:
                print("Search found!!!")
                print(items) 
            else:
                print("Not found")
                
    elif num== 4:
        
        id=int(input("Enter the name for remove"))
        if id in (total_data):
            del total_data[id]
        else:
            print("Id Not Found")

    else:
        print("Invalid Option or No Data Found!!!")
        


    option = int(input("Enter 1 to continue or 0 to end: "))
