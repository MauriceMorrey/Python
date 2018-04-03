import random
random_num = random.random()

def coinTosses(times):
    headscount = 0
    tailscount = 0
    result = ["heads", "tails"]
    for i in range (0, times):
        toss_result = result[random.randint(0,1)]
        print "Throwing a coin..." + " It's a " + toss_result + " ... " + "Got " + str(headscount) + " heads and " + str(tailscount) + " tails so far."
        if (toss_result == "heads"):
            headscount += 1
        elif (toss_result == "tails"):
            tailscount += 1

coinTosses(10)