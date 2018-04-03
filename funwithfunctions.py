def odd_even():
    for i in range(1, 11):#(start,end+1)
        if i % 2 == 0:
            print "Number is {}. This is an even number.".format(i)
        else:
            print "Number is {}. This is an odd number.".format(i)
odd_even()

print "..end of odd_even function.."

def multiply(list_a, y):
    for i in range(len(list_a)):
        list_a[i] *= y
    print list_a
    return list_a
list_b = [2,4,10,16]
print list_b
multiply(list_b, 5)

print "..end of multiply function.."

def layered_multiples(arr):
    list_arr = []
    multipliers = multiply(arr[0], arr[1])
    for i in range(len(multipliers)):
        new_list_arr = []
        for i in range(multipliers[i]):
            new_list_arr.append(1)
        list_arr.append(new_list_arr)
    print list_arr

    
arr = ([2,4,5],3)
layered_multiples(arr)

print "..end of layered multiplier.."
