import time

seconds= int (input("How many seconds do you want to wait for?"))

for i in range(seconds):
    print(str(seconds - i) + " seconds remaining")
    time.sleep(1)

print ("Time's up!")