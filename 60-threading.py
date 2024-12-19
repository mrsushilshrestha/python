import time
import threading

def tasks_1(task_number):
    print("task one is ongoing.....")
    # num=input("Enter the number:")
    print(task_number)
    time.sleep(5)

def tasks_2():
    print("task two ongoing....")
    time.sleep(5)
    

# tasks_1()
# tasks_2()

t1 = threading.Thread(target=tasks_1(5))
t1.start()

t2 =threading.Thread(target=tasks_2)
t2.start()