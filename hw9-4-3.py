# Author: SCT (AMDG) 1/18/22

def count_e(word):
    num = 0
    for x in word:
        if x == "e":
            num += 1
    
    return num

a = count_e("me")
b = count_e("tree")
c = count_e("heeeee")
print(a,b,c)