#WAF that replace all occurrences of "java" with "python"in above file.

with open("practice.txt","r") as f:
    data=f.read()
    # print(data)

new_data=data.replace("Java","python")
print(new_data)

with open("practice.txt","w+") as f:
    f.write(new_data)
    