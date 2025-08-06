#introduction of string in python
str1= "Hello Sushil"
str2 = 'Hello sushil'
str3 = """Hello sushil"""

print(str1)
print(str2)
print(str3)

#if we need to print somthing like " " '' in display we use diffrent "" '' """  """ in our code
str4= "Hello what's up "
str5 ='Hello this is "021710" My symbol Number'
str6= """Hello this is "021710" My symbol Number. Hi what's up"""

print(str4)
print(str5)
print(str6)
print("\n") #for next line or gap


#string concatenation 
str7 ="sushil"
str8 ="shrestha"

finalString = str7 + " "+ str8 
print(finalString,"\n")

#using input()
print("Enter the Two String")
str9 = input()
str10 = input()

print(f" String First {str9} and String Second {str10} and It's concatenation is: ",str9+ ' ' + str10)


#To finding string Length
str11 ="Hello World!"
print(len(str11))
print(len(str9))

length=len(str10)
print(length)


#index string
str12 ="Om Namah Shivaya"
ch= str12[0]
ch= str12[3]

print(ch)

#slice in string
#str[starinf-idx : end-idx]
#str[0:]
#str[:12]
#str[0:12]
str13 = "Sushil Shrestha"
sliceString= str13[0:6]
print(sliceString)

