class Call:
    def __init__(self, id, name, number, time, reason):
        self.id = id
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason

    def display(self):
        print ("Id: ",self.id, "Caller name: ", self.name, "Caller number: ", self.number, "Time of call: ", self.time, "Reason for calling: ", self.reason)

Jacky = call(1234, "jack", 1234432, 12:30, "hello")

print (jacky.display())
