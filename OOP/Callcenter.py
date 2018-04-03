class Call():
    def __init__(self,unique_id,caller_name,caller_phn_num,time_of_call,reason_for_call):
        self.unique_id = unique_id
        self.caller_name = caller_name
        self.caller_phn_num = caller_phn_num
        self.time_of_call = time_of_call
        self.reason_for_call = reason_for_call

    def display(self):
        print "Unique caller ID is: " + self.unique_id
        print "Caller name is: " + self.caller_name
        print "Caller phone number is: " + self.caller_phn_num
        print "Time of call: " + self.time_of_call
        print "Reason for call: " + self.reason_for_call
        return self

call1 = Call( "005", "Mikey", "123-666-777", "9:15 am",  "Looking for manager" )
call1.display()
print "..end of class call...."
        
class CallCenter():
    def __init__(self,calls=[],queue_size=0):
        self.calls = []
        self.queue_size = 0

    def add(self,new_calls):
        self.calls.append(new_calls)#adds a new call to the end of the call list
        self.queue_size += 1
        return self

    def remove(self):
        if self.queue_size >0:
            del self.calls[0]# removes the call from the beginning of the list (index 0)
            self.queue_size -= 1
        return self

    def info(self):
        for i in self.calls:
            i.display()#prints the name and phone number for each call in the queue as well as the length of the queue.
        print "The queue size is: " + str(self.queue_size)

test = CallCenter()
test.add(call1).info()

