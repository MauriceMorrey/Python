words = "It's thanksgiving day. It's my birthday too!"
print words.find('day')
print words.replace('day', 'month')

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

y = ["hello",2,54,-2,7,12,98,"world"]
print y[0]
print y[len(y)-1]

w = []
w.append(y[0])
w.append(y[len(y)-1])
print w

x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x
x.sort()
print x

b = x[0:len(x)/2]
print b

c = x[len(x)/2+1:]
print c

d = []
d.append(b)
#d = d + c
#d.insert(len(d), c)
d.append(c)

print d

