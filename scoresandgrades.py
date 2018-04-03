import random
for i in range (10):
    random_scores = random.randint(60,100)
    #random.randint(a, b)
    #Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
    grade = ""
    if random_scores >=60 and random_scores < 70:
        grade = "D"
        print "Score: {}; Your grade is {}".format(str(random_scores),grade)
    elif random_scores >=70 and random_scores < 80:
        grade = "C"
        print "Score: {}; Your grade is {}".format(str(random_scores),grade)
    elif random_scores >=80 and random_scores < 90:
        grade = "B"
        print "Score: {}; Your grade is {}".format(str(random_scores),grade)
    else:
        random_scores >=90 and random_scores < 100
        grade = "A"
        print "Score: {}; Your grade is {}".format(str(random_scores),grade)

