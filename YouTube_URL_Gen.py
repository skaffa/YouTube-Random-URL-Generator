import random
import string
import time
limit = 50 #How many URLs to generate
delay = 0.1  #Delay between each generation
c = 0
print("\n Generating",limit,"URLs with a delay of",delay,"seconds\n")
time.sleep(3)
while c != limit:
    ran = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + "-_", k = 11))
    print("https://youtu.be/watch?v=" + str(ran))
    time.sleep(delay)
    c += 1
else:
    print("\n Done!",limit,"URLs generated")