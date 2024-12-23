#file Handling in Python.
#read the file 
f = open("62-file-handling.txt","r")
data =f.read()
print(data)
print(type(data))

f.close()