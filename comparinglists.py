list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

list_three = [1,2,5,6,5]
list_four = [1,2,5,6,5,3]

list_five = [1,2,5,6,5,16]
list_six = [1,2,5,6,5]

list_seven = ['celery','carrots','bread','milk']
list_eight= ['celery','carrots','bread','cream']

def compare_list(list_a,list_b):
    if list_a == list_b:
        print "The lists are the same"
    else:
        print  "The lists are not the same."
compare_list(list_seven,list_eight)
