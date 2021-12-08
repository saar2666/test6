import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
#passlen = input("choose pw length: ")
p = "".join(random.sample(s,8))
print("8 char pw: ")
print p