class Call():
    def __init__(self, id, name, number, time, reason):
        self.id = id
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason

    def display(self):
        print ("Id: ",self.id, "Caller name: ", self.name, "Caller number: ", self.number, "Time of call: ", self.time, "Reason for calling: ", self.reason)

Jacky = Call(1234, "jack", 1234432, 12.30, "hello")
jason = Call(123, "jason", 123462, 12.2, "hi")


class Callcenter:
    def __init__(self):
        self.calls = []
        self.queue = len(self.calls)

    def addcall(self, *callers):
        self.calls.append(callers)
        return self
    def callinfo(self):
        for x in self.calls:
            print (x.name, x.number)
    def remove(self):
        self.calls.pop(0)
        return self
        
call1 = Call(123,"kyle",1234567,12,"lol")

control = Callcenter()

(control.addcall(Jacky,jason,call1))

print (control.calls, control.queue)



