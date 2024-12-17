#dictionary is a mutable

dict = {}
print(type(dict)) #to know types

user_data_detail ={"name":"skill shikshy","location":"ktm" ,"number":"980808"}
print(user_data_detail["name"]) #print user name
print(user_data_detail["location"]) #print user location
print(user_data_detail["number"]) #print user number


#using loop to print the detail and add +977 to number
for key in user_data_detail:
    if(key=='number'):
        user_data_detail[key]="+977"+user_data_detail[key]
print(user_data_detail)

    
    
    