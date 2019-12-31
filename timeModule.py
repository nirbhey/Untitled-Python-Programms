import time

start_time = time.time() # start var, i.e. time.time(), is to calculate how much time a particular part of program is right now.
print(start_time)

for x in range(10):
    print(x)
    time.sleep(1) # time.sleep is used for making a program sleep(wait) for seconds of time mentioned in the ().

print('Time taken ', time.time() - start_time, 'current time: ', time.time()) # time.time gives the current time
