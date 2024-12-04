#WAP to ask the user to enter names of their 3 favorite Movies & store them in a list
print("Enter the 3 Movie Name:")

movie_name =[] #making empty list

movie_1 = input()
movie_name.append(movie_1)

movie_2 = input()
movie_name.append(movie_2)

movie_3 = input()
movie_name.append(movie_3)

print("The Name Of the Movie is Listed:")
print(movie_name)

print("\n The Movie Name in Ascending Order:")
movie_name.sort()
print(movie_name)

