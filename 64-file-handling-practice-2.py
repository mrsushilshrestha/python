#WAP to search if the word "Learning" exits in the file or not
with open("practice.txt","r") as f:
    data =f.read()
    word ="learning"
    if data.find(word)!=-1:
        print("Found")
    else:
        print("Not Found")
        

#By Using the Functions
def search(word):
    with open("practice.txt","r") as f:
        data =f.read()
    if data.find(word)!=-1:
        print("Found ")
    else:
        print("Not Found ")


search_word=input("Enter the Data to search: ")
search(search_word)

#By using Class
class Search_engine:
    def __init__(self,path):
        self.path=path
    
    def search(self,word):
        with open(self.path,"r")as f:
            data = f.read()
        
        if data.find!=-1:
            print(f"Find Data {word} ")
        else:
            print("Data Does not exits!!!")
    

path="practice.txt" #path of file
search_obj =Search_engine(path)

word =input("Enter the search data: ")
search_obj.search(word)
    
    