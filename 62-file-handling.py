#file Handling in Python.
#read the file 
# f = open("62-file-handling.txt","r")
# data =f.read()
# print(data)
# print(type(data))

# f.close()

# mod =['w','r',a]

with open("readme.txt","w") as file_obj:  #create and read data in file
    file_obj.write("Hello World")
    
with open("readme.txt","r") as file_obj: #read the file data 
    print(file_obj.read())

with open("readme.txt","a") as file_obj:
    data=file_obj.write("Hello This is Second Lines")    

with open("readme.txt","r") as file_obj: #read the file data 
    print(file_obj.read())

