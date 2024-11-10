import threading
import time

def read_file(filename, shared_data):
    with open(filename, 'r') as file:

        data = file.read()
        shared_data.append(data)
    time.sleep(1) 

def display_data(shared_data):
    while not shared_data: 
        time.sleep(0.1)
    print("Data dari file:")
    print(shared_data[0])

filename = 'file.txt'

shared_data = []

thread1 = threading.Thread(target=read_file, args=(filename, shared_data))
thread2 = threading.Thread(target=display_data, args=(shared_data,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("Finish.")