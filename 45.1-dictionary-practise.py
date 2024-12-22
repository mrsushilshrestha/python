#Strore following word meaning in a python dictionary:
#table : "a piece of furniture","list of facts & figures"
#cat:"a small animal"

dictionary_store={"table":["a piece of furniture"," list of facts & figures"],
                  "cat":"a small animal"
                  }
print(dictionary_store)


#you are given a list  of subjects for students.Assume one classroom is requred for 1 subject .How many classrooms are needed by all students.
#python","java","C++","python","javascript","java","python","java","C++","C"

#dictionary and set do not allow duplication of data so that we store the value in set.

set_subject ={"python","java","C++","python","javascript","java","python","java","C++","C"}
print(f"There are {len(set_subject)} classes Are Requred")
print(set_subject)


#WAP to enter marks of 3 subjects from the user and store them in a dictionary
#start with an empty dictionary & add one by one. 
#use subject name as key & marks as value.

# dictionary_student_management={}
# list_student_management=[]
# print("Enter the Subject Name,Marks of Subject")
# # print(type(dictionary_student_management))
# for i in range(3):
#     dictionary_student_management["Subject_name"]=input("Enter the Subject Name:")
#     dictionary_student_management["mark"] =input("Enter the mark os subject")

#     list_student_management.append(dictionary_student_management)

# print(list_student_management)


#figure out a way to store 9 and 9.0 as separate values in the set.
#(you can take help of built-in data types)

set_values ={9,"9.0"}
print(set_values)

#another ways
set_valuess={
    ("int values",9),
    ("float values",9.0)
}
print(set_valuess)
