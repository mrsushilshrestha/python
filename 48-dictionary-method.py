# Python program to demonstrate dictionary methods
student_detail ={
    "name":"sushil",
    "address":"Kathmandu",
    "age":20
}

#Return the all key use in the dictionary
print(student_detail.keys())

#to know the length of the dictionary
print(len(student_detail))


#typecasting the dictionary to list 
print(list(student_detail))


#print value only
print(student_detail.values())

#return all(key,val) pairs as tuples
print(student_detail.items())

#return the key according to value
print(student_detail["name"])   #it give error if any keys are mistake
print(student_detail.get("name")) #it does not give any error if mistake keys

#inserts the specified items to the dictionary
student_detail.update({"city":"kathmandu"})
print(student_detail)




