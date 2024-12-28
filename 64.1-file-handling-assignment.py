#Create a file "practice.txt" using python.Add the following data in it:
"""
    Hi everyone
    we are learning File I/O
    using Java.
    I like programming In Java
"""

#to create a file
with open("practice.txt","w")as f:
    f.write( "Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming In Java")
    
    
with open("practice.txt","r")as f:
    print(f.read())


    