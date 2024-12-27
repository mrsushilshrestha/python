#syntax

# Read the data from the text file
with open("file-handling(Assignment).txt","r") as file_obj:
    file =file_obj.read()
    print(file)

#Write in the file
with open("file-handling(Assignment).txt","w") as file_obj:
    file_obj.write("This is Sushil Shrestha File Update From 63-file-handling syntax.py")

