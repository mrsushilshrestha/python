#WAP to ask the user to enter names of their 3 favorite Movies & store them in a list
print("Enter the 3 Movie Name: ")

movie_name =[] #making empty list

movie_name.append(input("Enter the First Movie "))
movie_name.append(input("Enter the Second Movie "))
movie_name.append(input("Enter the Third Movie "))

print("The Name Of the Movie is Listed:")
print(movie_name)

print("\n The Movie Name in Ascending Order:")
movie_name.sort()
print(movie_name)

