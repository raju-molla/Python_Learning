# word =['cat', 'bat', 'molla']

# for w in word:
#     print(w, len(w))

# range

# for i in range(5):
#     print(i)

# prime number

for i in range(2,20):
    for j in range(2,i):
        if i%j==0:
            print(i, " is not prime")
            break
    else:
        print(i," is a prime number")
