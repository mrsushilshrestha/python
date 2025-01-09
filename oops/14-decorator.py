# Task: Create an Authentication Decorator
# Write a Python program that uses a decorator to simulate an authentication mechanism in plain Python.
 
# Requirements:
 
# Create a dictionary to store valid credentials, e.g., {'user1': 'password123', 'admin': 'adminpass'}.
# Implement a decorator named authenticate:
# Accepts a username and password as parameters.
# Verifies the credentials against the dictionary.
# If valid, allows access to the decorated function.
# If invalid, prints "Access Denied" and prevents execution of the function.
 
# Patterns:
 
 
# Dictionary of valid credentials

VALID_CREDENTIALS = {

    'userName': 'password123',

    'password': 'adminpass'

}
 
# Authentication decorator
 
def authenticate(func):
    
   if VALID_CREDENTIALS['userName']== and VALID_CREDENTIALS['password']== password:

  #check username and password
 
 
# Function protected by authentication

@authenticate
def view_account(username,password):
    username
    print("Welcome to your account, user1!")
 
@authenticate
def transfer_funds(username,password):
    print("Funds transferred successfully!")
    
# Testing the functions

view_account(username='user1', password='password123')
transfer_funds(username='user1', password='password123')
