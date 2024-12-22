# Write a program that prints the following pattern:
# *
# **
# ***
# ****
# *****

for i in range(6):
    for j in range(i):
        print("*",end="")
    print()