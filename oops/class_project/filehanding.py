strings = []
print("Enter strings to save to the file.")

command = True
while command:
    user_input = input("Enter a string: ")
    strings.append(user_input)

    with open("data.txt", "w") as file:
        for line in strings:
            file.write(line + "\n")

    command = input("Do you want to continue? (y/n): ")
    if command== "n":
        command = False

with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())
