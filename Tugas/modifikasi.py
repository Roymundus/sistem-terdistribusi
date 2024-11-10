import threading
import time

def read_file_part(filename, start, end, shared_data, index):
    with open(filename, 'r') as file:
        file.seek(start)
        data = file.read(end - start) 
        shared_data[index] = data
    time.sleep(1) 


def display_data(shared_data):
    while not all(shared_data): 
        time.sleep(0.1)
    print("Data dari file:")
    for part in shared_data:
        print(part)

filename = 'file.txt'
with open(filename, 'r') as file:
    file_size = len(file.read())

num_threads = 4
chunk_size = file_size // num_threads

shared_data = [None] * num_threads
threads = []
for i in range(num_threads):
    start = i * chunk_size
    end = (start + chunk_size) if i < num_threads - 1 else file_size 
    thread = threading.Thread(target=read_file_part, args=(filename, start,
end, shared_data, i))
    threads.append(thread)
    thread.start()

display_thread = threading.Thread(target=display_data, args=(shared_data,))
display_thread.start()

for thread in threads:
    thread.join()

display_thread.join()
print("Finish")