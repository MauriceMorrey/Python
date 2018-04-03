# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
#new_list = ['hello','world']
new_list = []

for i in word_list:
    if (i.count("o") != 0):
        new_list.append(i)

print new_list
