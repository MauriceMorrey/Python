class bike():
    def  __init__(self,price,max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayinfo(self):
        print "Price is: " + str(self.price)
        print "Max-peed is: " + str(self.max_speed)
        print "Total miles:" + str(self.miles) + " miles"
        return self
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing"
        #keep miles out of negative
        if (self.miles >= 5):
            self.miles -= 5
        return self
bike("$300", "55 mph").ride().reverse().displayinfo()
