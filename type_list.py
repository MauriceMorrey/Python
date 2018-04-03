#l = ['magical unicorns',19,'hello',98.98,'world']
#l = [2,3,1,7,4,12]
l = ['magical','unicorns','not real']

tot_str = "" 
total = 0
string_count = 0
number_count = 0

for element in l:        
    if type(element) == str: 
        tot_str += element + ' '
        string_count += 1
    elif type(element) == int or type(element) == float: 
        total += element
        number_count += 1

if number_count > 0:
    if string_count > 0:
        emp_str = "mixed"
        print "The list you entered is of type"+emp_str+"\nString: "+tot_str+"\nSum: " + str(total)
    else:
        emp_str = "number"
        print "The list you entered is a"+emp_str+str(tot_str)+"\nSum: " + str(total)
elif string_count > 0:
    emp_str = "string"
    print "The list you entered is of type "+emp_str+"\nString: " + tot_str






        

        
