#WAP to find the data and print the line if data found at or if not found print -1(return -1)
def search(word):
    data=True
    line=1
    with open("practice.txt","r")as f:
        while data:
            data=f.readline()
            if word in data:
                print(line)
                return
            
            line+=1
        return print("-1")
            


word=input("Enter the Word of data ")
search(word)

