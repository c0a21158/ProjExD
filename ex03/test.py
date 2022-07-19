import random
u = []
print("hello world")
l = ["a","b","c","d"]
for t in range(2):
    i= l.pop(random.randint(0,2))
    u += i
print(u)