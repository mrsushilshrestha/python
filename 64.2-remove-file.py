import os 
options ="y"

# option =input("Enter the options 1/0 to Create and Delete file ")
while options=="y":
    option =input("Enter the options 1/0 to Create and Delete file ")
    if option=="1":
        with open("delete_file.txt","w"): #to create a file 
            pass
    elif option=="0":
    #to delete the file
        os.remove("delete_file.txt")
    else:
        print("Invalid option!!!")
    options=input("Do you want to continue:")
    



