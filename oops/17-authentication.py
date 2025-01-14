save_credential={
    'username':'mrsushilshrestha','password':'sushil@123'
}

def authenticator(funs):
    def inner(username,password):
        if username==save_credential['username'] and password==save_credential['password']:
            return funs(username,password)
        else:
            print("Invalid credential!!!")
    return inner




@authenticator
def facebook(username,password):
    print("Welcome to Sushil Shrestha Facebook")
    

user='mrsushilshrestha'
pas='sushil@123'
facebook(user,pas)
# facebook('mrsushilshr','sushil@123')

