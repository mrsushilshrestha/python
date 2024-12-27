#To create a File and Write a something in file.
with open("file-handling(Assignment).txt","w") as file_obj:
    file_obj.write("Hello World!")

#To read the file data
f=open("file-handling(Assignment).txt","r")
data=f.read()
print(data)

#to read the line 
f=open("file-handling(Assignment).txt","r")
data =f.readlines()
print(data)


#to write the data in file
f=open("file-handling(Assignment).txt","w")
f.write('Hello Sushil shrestha')
f.write("\n")
f.write('Hello Sushil shrestha')
f.write("\n")
f.write('Hello Sushil shrestha')
f.write("\n")
f.write('Hello Sushil shrestha')
f.write("\n")

#Read the line of data store in file
f=open("file-handling(Assignment).txt","r")
data=f.readline()
print("This is Read the line Only",data)

# append data in file
# append add the data at the end

f= open("file-handling(Assignment).txt","a")
f.write("\nHello This is Append First \n")
f.write("Hello This is Append Second \n")
f.write("Hello This is Append Third \n")
f.write("Hello This is Append Fourth \n")


# #to read the line 
f=open("file-handling(Assignment).txt","r")
data =f.readline()
data =f.read()

print(data)

# w+ mode
# truncating the file
f=open("file-handling(Assignment).txt","w+")
f.write("Hello this is 'w+' file Mode..................12345678910.")
data =f.read()
print(data)

# r+ mode
# no truncating the file but replace the file
f=open("file-handling(Assignment).txt","r+")
f.write("Hello this is 'r+'file Mode We Check the operation.")
data =f.read()
print(data)

# a+ mode
# no truncating the file
#just allow to append file and allow to read and write
f=open("file-handling(Assignment).txt","a+")
f.write("\nHello this is 'a+' file Mode.\n")
data =f.read()
print(data)